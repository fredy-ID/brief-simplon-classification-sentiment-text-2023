from django.shortcuts import render
from rest_framework import generics, status
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import *
from .serializer import *
from collections import defaultdict
import json
import re
import sys
from django.db import IntegrityError, transaction

from bs4 import BeautifulSoup
import dateparser
# from etaprogress.progress import ProgressBar
import requests
import os
import pandas as pd

# Create your views here.

class FilmList(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmCreate(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class SpectatorCriticsList(generics.ListAPIView):
    queryset = SpectatorCritics.objects.all()
    serializer_class = SpectatorCriticsSerializer

class SpectatorCriticsCrud(generics.ListCreateAPIView):
    queryset = SpectatorCritics.objects.all()
    serializer_class = SpectatorCriticsSerializer

def parse_list_page(page_url):
    r = requests.get(page_url)
    soup = BeautifulSoup(r.text, 'html.parser')

    films = soup.find_all("a", {"class": "meta-title-link"})
    return [f.get('href') for f in films]

def get_film_urls(root_url, page_number = 2):
    list_url = "{root}/film/meilleurs".format(root=root_url)
    r = requests.get(list_url)
    soup = BeautifulSoup(r.text, 'html.parser')

    pagination = soup.find("div", {"class": "pagination-item-holder"})
    pages = pagination.find_all("span")
    page_number = int([page.text for page in pages][-1])

    out_urls = []


    for page_id in range(1, page_number+2):

        # Extend out list with new urls
        page_url = "{list_url}/?page={page_num}".format(
            list_url=list_url,
            page_num=page_id)
        print(page_url)
        film_urls = parse_list_page(page_url)
        out_urls.extend(film_urls)

    return out_urls

def format_text(comment):
    output_text = ""
    for content in comment.contents:
        content_str = str(content)
        content_soup = BeautifulSoup(content_str, 'html.parser')
        spoiler = content_soup.find("span", {"class": "spoiler-content"})
        if spoiler:
            output_text += spoiler.text.strip()
        else:
            output_text += content_str.strip()
    return output_text

def parse_film_page(page_url):
    ratings, reviews, dates, helpfuls = [], [], [], []
    r = requests.get(page_url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # We iterate on reviews to avoid other reviews (Meilleurs films à l'affiche)
    for rating_parent in soup.find_all("div", {"class": "review-card-review-holder"}):
        rating_raw = rating_parent.find("span", {"class": "stareval-note"})  # <span class="stareval-note">4,0</span>
        rating_str = str(rating_raw.contents)[2:5]  # "4,0"
        rating = float(rating_str.replace(',', '.'))  # 4.0
        ratings.append(rating)

    for review_raw in soup.find_all("div", attrs={"class": "content-txt review-card-content"}):
        review_text = format_text(review_raw)
        reviews.append(review_text)

    for date_raw in soup.find_all("span", attrs={"class": "review-card-meta-date light"}):
        date_str = date_raw.text.strip()  # Publiée le 24 mai 2011
        date_str = date_str[11:]  # 24 mai 2011
        date = dateparser.parse(date_str).date()  # 2011-05-24
        dates.append(date)

    for helpful_raw in soup.find_all("div", {"class": "reviews-users-comment-useful js-useful-reviews"}):
        helpful_str = helpful_raw.get("data-statistics")  # "{"helpfulCount":21,"unhelpfulCount":0}"
        helpful_dic = json.loads(helpful_str)  # {"helpfulCount": 21, "unhelpfulCount": 0}
        helpful = [helpful_dic["helpfulCount"], helpful_dic["unhelpfulCount"]]  # [21, 0]
        helpfuls.append(helpful)

    return ratings, reviews, dates, helpfuls

def parse_film(film_url, max_reviews=None):
    ratings, reviews, dates, helpfuls = [], [], [], []
    r = requests.get(film_url)
    # print(len(r.history))
    if r.status_code == requests.codes.not_found:
        # if url is not foud : film does not exist
        print("Error code {}. Skipping: {}".format(
            r.status_code,
            film_url
        ))
        return None
    elif len(r.history) > 2:
        # if there is more than one element in history, the request was redirected
        # and that means there are no "critiques/spectateurs" page
        return None

    soup = BeautifulSoup(r.text, 'html.parser')

    film_title = soup.find("div", {"class": "titlebar titlebar-page"})
    film_title = film_title.find('span', {"class": 'titlebar-link'})
    film_title = film_title.text.strip()


    # Find number of pages
    pagination = soup.find("div", {"class": "pagination-item-holder"})

    page_number = 1
    if pagination:
        pages = pagination.find_all("span")
        page_number = int([page.text for page in pages][-1])

    # Iterate over pages
    for page_id in range(1, page_number+1):
        page_url = "{film_url}/?page={page_num}".format(
            film_url=film_url,
            page_num=page_id)
        p_ratings, p_reviews, p_dates, p_helpfuls = parse_film_page(page_url)

        ratings.extend(p_ratings)
        reviews.extend(p_reviews)
        dates.extend(p_dates)
        helpfuls.extend(p_helpfuls)

        if max_reviews and len(ratings) > max_reviews:
            return (ratings[:max_reviews], reviews[:max_reviews],
                    dates[:max_reviews], helpfuls[:max_reviews])

    return (ratings, reviews, dates, helpfuls)

def title_film():
    root_url = "https://www.allocine.fr"
    urls = get_film_urls(root_url)

    films_titles = []
    for i, url in enumerate(urls):
        film_id = re.findall(r'\d+', url)[0]
        film_url = "{root}/video/player_gen_cmedia=19376882&cfilm={film_id}.html".format(
            root=root_url,
            film_id=film_id
        )
        r = requests.get(film_url)
        soup = BeautifulSoup(r.text, 'html.parser')

        film_title = soup.find("div", {"class": "titlebar-title titlebar-title-lg"})
        film_title = film_title.text.strip()

        media_info_div = soup.find('div', class_='media-info-serie light')
        
        date_element = media_info_div.find('span', class_=re.compile(r'ACrL2ZACrpbG0vYWdlbmRhL3NlbS0')).text.strip()

        films_titles.append((film_title, film_id,date_element))
        
        

    return films_titles


def get_film_reviews(root_url ="https://www.allocine.fr", max_reviews_per_film=10):
    urls = get_film_urls(root_url)
    allocine_dic = defaultdict(list)

    for i, url in enumerate(urls):

        film_id = re.findall(r'\d+', url)[0]
        film_url = "{root}/film/fichefilm-{film_id}/critiques/spectateurs".format(
            root=root_url,
            film_id=film_id
        )
        print(film_url)

        parse_output = parse_film(film_url, max_reviews_per_film)
        if parse_output:
            ratings, reviews, dates, helpfuls = parse_output

            # Rarely happens
            if not(len(ratings) == len(reviews) == len(dates) ==
                   len(helpfuls)):
                print("Error: film-url: " + film_url)
                continue

            allocine_dic['film-url'].extend(len(ratings)*[film_url])
            allocine_dic['stars'].extend(ratings)
            allocine_dic['text'].extend(reviews)
            allocine_dic['publication_date'].extend(dates)
            allocine_dic['helpful'].extend([h[0] for h in helpfuls])
            allocine_dic['unhelpful'].extend([h[1] for h in helpfuls])



    return allocine_dic


@csrf_exempt
@require_POST
def scrapping(request):
    data = get_film_reviews()

    title = title_film()
    df = pd.DataFrame.from_dict(data)

    # Insérer dans la table Film
    for i in title:
        
        title, ref, date_film = i[0],i[1], i[2] 
        parsed_date = dateparser.parse(date_film, languages=['fr'])
        formatted_date = parsed_date.strftime('%Y-%m-%d')
        
        # film_instance, created = Film.objects.get_or_create(
        #     title = title,
        #     reference = ref,
        #     release_date = formatted_date
        # )
        # try:
        #     film_instance.save()
        # except IntegrityError:
        #     # Le film existe déjà, effectuez une action appropriée (par exemple, mettez à jour les champs)
        #     existing_film = Film.objects.get(title=film_instance.title)
        #     existing_film.reference = ref
        #     existing_film.release_date = formatted_date
        #     existing_film.save()
        
        with transaction.atomic():
            film_instance, created = Film.objects.get_or_create(
                title=title,
                reference=ref,
                release_date=formatted_date
            )

            if not created:
                # Le film existe déjà, effectuez une action appropriée
                film_instance.reference = ref
                film_instance.release_date = formatted_date
                film_instance.save()

    # Add dans la table spectator
    selected_columns = df[['stars', 'text', 'publication_date','film-url']]
    pattern = r'film/fichefilm-(\d+)'
    for index, row in selected_columns.iterrows():
        rating = row['stars']
        review = row['text']
        date = row['publication_date']
        url = row['film-url']
        match = re.search(pattern, url)
        if match:
            ref_film = match.group(1)
            fk_film = Film.objects.filter(reference=ref_film).first()

            
        spect_instance = SpectatorCritics(
            text = review,
            stars = rating,
            publication_date = date,
            id_film = fk_film

        )
        spect_instance.save()
        
        
    return Response({"status": "success"}, status=status.HTTP_201_CREATED)