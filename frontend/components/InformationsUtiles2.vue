<template>
    <div class="border p-5 overflow-x-auto ">
      <!-- {{ analyseResultData.top }} -->
      {{ topFilms }}
      {{ topFilms }}
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
                  <td>Date</td> 
                  <td>moyenne note maxi</td>
                  <!-- <td>Note global après analyse</td> -->
                </tr>
              </thead> 
              <tbody>
                <tr v-for="(c, index) in topFilms" :key="index">
                  <th>{{index + 1}}</th> 
                  <td>{{ topFilms[index].title }}</td> 
                  <td>
                    {{topFilms[index].sum_min_highest}}
                  </td>
                  <td>
                    <!-- {{topFilms[index].sum_min_highest}} -->
                  </td>
                </tr>
              </tbody> 
              <tfoot>
                <tr>
                  <th></th> 
                  <td>Date</td> 
                  <td>Note</td>
                </tr>
              </tfoot>
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
    
    if (titleOccurrences[title]) {
      titleOccurrences[title] += 1;
    }else {
      titleOccurrences[title] = 1;
    }
  };

</script>