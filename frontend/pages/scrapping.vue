<template>
    <DashboardLayout class="">
        <div class="">
            <div class="p-5 flex flex-col md:flex-row items-center justify-center ">
                <button class="btn btn-primary mt-2 md:mt-0 md:ml-2 md:w-initial">Lancer le scrapping</button>
                <button class="btn btn-primary mt-2 md:mt-0 md:ml-2 md:w-initial">Arrêter le processus</button>
            </div>

            <div class="mockup-window border bg-base-300">
                <div class="px-4 py-16 bg-base-200 h-96 overflow-auto py-10">
                    <p>Hello!</p>
                    <p>Hello!</p>
                </div>
            </div>
            
            <div class="">

                <div class="mt-10">
                    <div class="alert alert-info">
                        <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                        <span>Scrapping en cours</span>
                        <span class="loading loading-spinner loading-lg"></span>
                    </div>
                    <div class="alert alert-success mt-1">
                        <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                        <span>Scrapping Terminé</span>
                    </div>
                </div>
                
                <div class="grid gap-4 grid-cols-1 lg:grid-cols-2 grid-rows-2 mt-10 p-5">

                    <div class="border p-5 overflow-x-auto ">
                        <div class="my-2">
                            <h3 class="font-bold text-3xl">Informations utiles</h3>
                        </div>
                        <div>
                            <p>Nombre de films analysés : <span>...</span> </p>
                            <p>Nombre de commentaires analysés : <span>...</span> </p>
                        </div>
                        <div class="my-2 mt-5   ">
                            <h3 class="text-2xl">Top 10 des films après analyse</h3>
                        </div>
                        <div class="overflow-x-auto overflow-y-auto h-96">
                            <table class="table table-xs table-pin-rows table-pin-cols">
                              <thead>
                                <tr>
                                  <th></th>
                                  <td>Date</td> 
                                  <td>Note global allocine</td>
                                  <td>Note global après analyse</td>
                                </tr>
                              </thead> 
                              <tbody>
                                <tr v-for="(c, index) in [1,1,1,1,1,1,1,1,1,1]" :key="index">
                                  <th>1</th> 
                                  <td>Cy Ganderton</td> 
                                  <td>
                                    <div class="rating rating-sm">
                                        <input type="radio" :name="'rating-7-2'+index" class="mask mask-star-2 bg-orange-400" checked />
                                        <input type="radio" :name="'rating-7-2'+index" class="mask mask-star-2 bg-orange-400" />
                                        <input type="radio" :name="'rating-7-2'+index" class="mask mask-star-2 bg-orange-400" />
                                        <input type="radio" :name="'rating-7-2'+index" class="mask mask-star-2 bg-orange-400" />
                                        <input type="radio" :name="'rating-7-2'+index" class="mask mask-star-2 bg-orange-400" />
                                    </div>
                                  </td>
                                  <td>
                                    <div class="rating rating-sm">
                                        <input type="radio" :name="'rating-6-4'+index" class="mask mask-star-2 bg-orange-400" />
                                        <input type="radio" :name="'rating-6-4'+index" class="mask mask-star-2 bg-orange-400" />
                                        <input type="radio" :name="'rating-6-4'+index" class="mask mask-star-2 bg-orange-400" checked />
                                        <input type="radio" :name="'rating-6-4'+index" class="mask mask-star-2 bg-orange-400" />
                                        <input type="radio" :name="'rating-6-4'+index" class="mask mask-star-2 bg-orange-400" />
                                    </div>
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
                </div>

                <div class="p-5 flex flex-col md:flex-row items-center justify-center ">
                    <button class="btn btn-success md:w-initial">Valider le résultat</button>
                    <button class="btn btn-error mt-2 md:mt-0 md:ml-2 md:w-initial">Refuser le résultat</button>
                </div>
            </div>
        </div>

        <dialog id="more_details" class="modal modal-bottom sm:modal-middle">
            <div class="modal-box">
                <h3 class="font-bold text-2xl">Changements</h3>
                <p class="py-4">Press ESC key or click the button below to close</p>
                <div class="modal-action">
                <form method="dialog">
                    <!-- if there is a button in form, it will close the modal -->
                    <button class="btn">Close</button>
                </form>
                </div>
            </div>
        </dialog>

        <!-- Page content here -->
        <label for="dashboard-layout" class="btn btn-primary drawer-button lg:hidden">Open drawer</label>
        
    </DashboardLayout>
</template>