<template>
    <DashboardLayout>
        <div class="w-full">
            <div class="grid gap-4 grid-cols-1 md:grid-cols-3 lg:grid-cols-4  grid-rows-2 p-5">

                <div class="card bg-neutral shadow-2xl">
                    <figure>
                        <img src="images/allocine.png"  alt="Shoes" />
                    </figure>
                    <div class="card-body">
                        <h2 class="card-title">Films</h2>
                        <p>Nombre de films scrappés sur AlloCiné</p>
                        <p class="text-5xl">10</p>
                        <div class="card-actions justify-end">
                        <a href="https://www.allocine.fr/film/meilleurs/" target="_blank" class="btn btn-primary">Allociné</a>
                        <a href="https://colab.research.google.com/drive/1QJ8aFnQ7xTIjzn0aZMc-Cu7wtwVxjfXY?usp=sharing" target="_blank" class="btn btn-info ">Google Colab</a>
                        </div>
                    </div>
                </div>

                <div class="card bg-neutral shadow-2xl">
                    <figure>
                        <img src="images/allocine.png"  alt="Shoes" />
                    </figure>
                    <div class="card-body">
                        <h2 class="card-title">Commentaires</h2>
                        <p>Nombre de commentaires scrappés sur AlloCiné</p>
                        <p class="text-5xl">10</p>
                        <div class="card-actions justify-end">
                        <a href="https://www.allocine.fr/film/meilleurs/" target="_blank" class="btn btn-primary">Allociné</a>
                        <a href="https://colab.research.google.com/drive/1QJ8aFnQ7xTIjzn0aZMc-Cu7wtwVxjfXY?usp=sharing" target="_blank" class="btn btn-info ">Google Colab</a>
                        </div>
                    </div>
                </div>

                <div class="card bg-neutral shadow-2xl">
                    <figure>
                        <img src="images/huggingface.jpg"  alt="Shoes" />
                    </figure>
                    <div class="card-body">
                        <h2 class="card-title">Model BERT</h2>
                        <p>Nombre d'analyse du model BERT</p>
                        <p class="text-5xl">10</p>
                        <div class="card-actions justify-end">
                        <a href="https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment" target="_blank" class="btn btn-primary">Hugging Face</a>
                        <a href="https://colab.research.google.com/drive/1JLOGJI70MKOnlWe6dthAxqWATGy5cfaV?usp=sharing&pli=1#scrollTo=xKWLRpX_S6DN" target="_blank" class="btn btn-info ">Google Colab</a>
                        </div>
                    </div>
                </div>

                <div class="card bg-neutral shadow-2xl">
                    <figure>
                        <img src="images/huggingface.jpg"  alt="Shoes" />
                    </figure>
                    <div class="card-body">
                        <h2 class="card-title">Model DISTILBERT</h2>
                        <p>Nombre d'analyse du model DISTILBERT</p>
                        <p class="text-5xl">10</p>
                        <div class="card-actions justify-end">
                        <a href="https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student" target="_blank" class="btn btn-primary">Hugging Face</a>
                        </div>
                    </div>
                </div>
                
            </div>
        </div>
    </DashboardLayout>

</template>