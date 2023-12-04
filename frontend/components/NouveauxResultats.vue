<template>
    <div class="border p-5 overflow-x-auto ">
        <div class="my-2">
            <h3 class="font-bold text-3xl">Nouveaux résultat(s)</h3>
        </div>


        <div class="my-2">
            <h4 class="text-2xl">Commentaires</h4>
        </div>
        <div class="overflow-x-auto overflow-y-auto h-96">
            <table class="table table-xs table-pin-rows table-pin-cols">
              <thead>
                <tr>
                  <th></th>
                  <td>Date</td> 
                  <td>Note commentateur</td>
                  <td>Note modèle</td>
                  <th></th>
                </tr>
              </thead> 
              <tbody>
                <tr v-for="(c, index) in [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]" :key="index">
                  <th>1</th> 
                  <td>Cy Ganderton</td> 
                  <td>
                    <div class="rating rating-sm">
                        <input type="radio" :name="'rating-7-1'+index" class="mask mask-star-2 bg-orange-400" checked />
                        <input type="radio" :name="'rating-7-1'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-7-1'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-7-1'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-7-1'+index" class="mask mask-star-2 bg-orange-400" />
                    </div>
                  </td>
                  <td>
                    <div class="rating rating-sm">
                        <input type="radio" :name="'rating-6-1'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-6-1'+index" class="mask mask-star-2 bg-orange-400" checked />
                        <input type="radio" :name="'rating-6-1'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-6-1'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-6-1'+index" class="mask mask-star-2 bg-orange-400" />
                    </div>
                  </td>
                  <td><button class="btn btn-sm btn-primary" onclick="more_details.showModal()">Voir</button></td>
                </tr>
              </tbody> 
              <tfoot>
                <tr>
                  <th></th> 
                  <td>Date</td> 
                  <td>Note</td>
                  <th></th>
                </tr>
              </tfoot>
            </table>
          </div>

        <div class="my-2">
            <h4 class="text-2xl">Films</h4>
        </div>
        <div class="overflow-x-auto overflow-y-auto h-96">
            <table class="table table-xs table-pin-rows table-pin-cols">
              <thead>
                <tr>
                  <th></th>
                  <td>Date</td> 
                  <td>Nouvelle note commentateurs</td>
                  <td>Nouvelle note de la press</td>
                  <td>Ancienne note commentateurs</td>
                  <td>Ancienne note de la press</td>
                </tr>
              </thead> 
              <tbody>
                <tr v-for="(c, index) in [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]" :key="index">
                  <th>1</th> 
                  <td>Cy Ganderton</td> 
                  <td>
                    <div class="rating rating-sm">
                        <input type="radio" :name="'rating-7'+index" class="mask mask-star-2 bg-orange-400" checked />
                        <input type="radio" :name="'rating-7'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-7'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-7'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-7'+index" class="mask mask-star-2 bg-orange-400" />
                    </div>
                  </td>
                  <td>
                    <div class="rating rating-sm">
                        <input type="radio" :name="'rating-6'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-6'+index" class="mask mask-star-2 bg-orange-400" checked />
                        <input type="radio" :name="'rating-6'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-6'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-6'+index" class="mask mask-star-2 bg-orange-400" />
                    </div>
                  </td>
                  <td>
                    <div class="rating rating-sm">
                        <input type="radio" :name="'rating-6-2'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-6-2'+index" class="mask mask-star-2 bg-orange-400" checked />
                        <input type="radio" :name="'rating-6-2'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-6-2'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-6-2'+index" class="mask mask-star-2 bg-orange-400" />
                    </div>
                  </td>
                  <td>
                    <div class="rating rating-sm">
                        <input type="radio" :name="'rating-6-3'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-6-3'+index" class="mask mask-star-2 bg-orange-400" checked />
                        <input type="radio" :name="'rating-6-3'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-6-3'+index" class="mask mask-star-2 bg-orange-400" />
                        <input type="radio" :name="'rating-6-3'+index" class="mask mask-star-2 bg-orange-400" />
                    </div>
                  </td>
                </tr>
              </tbody> 
              <tfoot>
                <tr>
                  <th></th> 
                  <td>Date</td> 
                  <td>Note</td>
                  <th></th>
                </tr>
              </tfoot>
            </table>
          </div>
    </div>
</template>