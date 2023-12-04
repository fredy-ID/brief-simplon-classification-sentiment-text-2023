<template>
    <div class="border p-5 overflow-x-auto ">
      <!-- {{ analyseResultData.top }} -->
      <!-- {{ topFilms }} -->
        <div class="my-2">
            <h3 class="font-bold text-3xl">Informations utiles</h3>
        </div>
        <!-- <div>
            <p>Nombre de films analysés : <span>...</span> </p>
            <p>Nombre de commentaires analysés : <span>...</span> </p>
        </div> -->
        <div class="my-2 mt-5   ">
            <h3 class="text-2xl">Top 25 des commentaires après analyse</h3>
        </div>
        <div class="overflow-x-auto overflow-y-auto h-96">
            <table class="table table-xs table-pin-rows table-pin-cols">
              <thead>
                <tr>
                  <th></th>
                  <td>Film</td> 
                  <td>Note global allocine</td>
                  <td>Note global après analyse</td>
                  <td>Moyenne de la note maxi</td>
                </tr>
              </thead> 
              <tbody>
                <tr v-for="(c, index) in topFilms" :key="index">
                  <th>{{index + 1}}</th> 
                  <td>{{ topFilms[index].title }}</td> 
                  <td>
                    <div class="rating rating-sm">
                        <input type="radio" :name="'rating-7-2'+(topFilms[index].rating == 0 ? 0 : '')" class="mask mask-star-2 bg-orange-400" checked />
                        <input type="radio" :name="'rating-7-2'+(topFilms[index].rating == 1 ? 1 : '')" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-7-2'+(topFilms[index].rating == 2 ? 2 : '')" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-7-2'+(topFilms[index].rating == 3 ? 3 : '')" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-7-2'+(topFilms[index].rating == 4 ? 4 : '')" class="mask mask-star-2 bg-orange-400" />
                    </div>
                    {{topFilms[index].rating}}
                  </td>
                  <td>
                    <div class="rating rating-sm">
                        <input type="radio" :name="'rating-6-4'+(topFilms[index].predicted_rating == 0 ? 0 : '')" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-6-4'+(topFilms[index].predicted_rating == 0 ? 1 : '')" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-6-4'+(topFilms[index].predicted_rating == 0 ? 2 : '')" class="mask mask-star-2 bg-orange-400" checked />
                        <input type="radio" :name="'rating-6-4'+(topFilms[index].predicted_rating == 0 ? 3 : '')" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-6-4'+(topFilms[index].predicted_rating == 0 ? 4 : '')" class="mask mask-star-2 bg-orange-400" />
                      </div>
                      {{topFilms[index].predicted_rating}}
                  </td>
                  <td>
                    {{topFilms[index].sum_min_highest}}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          
          <div class="overflow-x-auto overflow-y-auto h-96 mt-20">
            <div class="my-2 mt-5 mb-10">
              <h3 class="text-2xl">Listing des films pour les 25 commentaires les mieux notés</h3>
            </div>
            <table class="table table-xs table-pin-rows table-pin-cols">
              <thead>
                <tr>
                  <td>Film</td>
                </tr>
              </thead> 
              <tbody>
                <tr v-for="(c, index) in titleOccurrences" :key="index">
                  <th>{{index + 1}}</th> 
                  <td>
                    {{titleOccurrences[index] }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
    </div>
</template>

<script setup lang="ts">
  import { ref } from 'vue';

  const props = defineProps({
      analyseResultData: {
          required: false,
      }

  });

  const topFilms: any = ref([])
  const top: any = ref([])
  const titleOccurrences: any = ref({});

  for(let i:number=0; i<props.analyseResultData.top.film_title.length; i++){
    const title = props.analyseResultData.top.film_title[i];
    const rating = props.analyseResultData.top.rating[i];
    const predicted_rating = props.analyseResultData.top.predicted_rating[i];
    const sum_min_highest = props.analyseResultData.top.sum_min_highest[i]

    topFilms.value.push({
      "title": title,
      "rating": rating,
      "predicted_rating": predicted_rating,
      "sum_min_highest": sum_min_highest
    })
    
    if (titleOccurrences.value[title]) {
      titleOccurrences.value[title] += 1;
    }else {
      titleOccurrences.value[title] = 1;
    }
  };


</script>