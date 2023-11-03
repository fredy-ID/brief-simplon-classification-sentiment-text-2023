<template>
    <DashboardLayout>
        <div>
                <div class="hero min-h-screen bg-base-200">
                    <div class="overflow-x-auto hero-content text-center w-full">
                        <div class="overflow-x-auto overflow-y-auto w-full md:w-full h-120">
                            <table class="table table-xs table-pin-rows table-pin-cols">
                            <thead>
                                <tr>
                                    <th></th>
                                    <td>Date - heure</td>
                                    <td>Validé</td>
                                    <td>Site</td>
                                    <td>Note globale</td>
                                    <td>Note après analyse</td>
                                    <td></td>
                                </tr>
                            </thead> 
                            <tbody>
                                <tr v-for="(c, index) in [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]" :key="index">
                                    <th>1</th> 
                                    <td>30 avril 1996 - 16h15</td>
                                    <td>Non</td>
                                    <td>AlloCiné</td>
                                    <td>
                                        <div class="rating rating-sm">
                                            <input type="radio" :name="'rating-6-3'+index" class="mask mask-star-2 bg-orange-400" />
                                            <input type="radio" :name="'rating-6-3'+index" class="mask mask-star-2 bg-orange-400" checked />
                                            <input type="radio" :name="'rating-6-3'+index" class="mask mask-star-2 bg-orange-400" />
                                            <input type="radio" :name="'rating-6-3'+index" class="mask mask-star-2 bg-orange-400" />
                                            <input type="radio" :name="'rating-6-3'+index" class="mask mask-star-2 bg-orange-400" />
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
                                    <td><a href="/online-games" class="btn btn-sm btn-info grow">Détails</a></td>
                                </tr>
                            </tbody> 
                            <tfoot>
                                <tr>
                                    <th></th> 
                                    <td>Auteur</td> 
                                    <td></td>
                                </tr>
                            </tfoot>
                            </table>
                        </div>
                    </div>
                </div>
        </div>
    </DashboardLayout>
</template>

<style scoped>
            
.h-120 {
    height: 34rem; /* 384px */
}

</style>