<template>
    <DashboardLayout class="">
        <div class="">
            <LaunchStopScrapp :scrappingOn="scrappingOn" :analyseOn="analyseOn"  @on-scrapping-state="setScrappingState" @on-analyse-state="setAnalyseState" @on-analyse-result="analyseModelResult" @on-scrapping-result="allocineScrapResult" />

            <Logs v-if="scrappResult" :scrappResultData="scrappResultData" />
            
            <div class="">

                <div class="mt-10">
                    <AlertScrapping v-if="scrappingOn" />
                    <AlertEndOfScraping v-if="alertEndOfScraping"/>
                </div>
                
                <div v-if="analyseResult">
                  <div class=" mt-10 p-5">
                      <InformationsUtiles :analyseResultData="analyseResultData" />
                      <!-- <InformationsUtiles2 :analyseResultData="analyseResultData" /> -->
                      
                      <NouveauxResultats v-if="disabled" />
                  </div>

                  <div v-if="disabled" class="p-5 flex flex-col md:flex-row items-center justify-center ">
                      <button class="btn btn-success md:w-initial">Valider le résultat</button>
                      <button class="btn btn-error mt-2 md:mt-0 md:ml-2 md:w-initial">Refuser le résultat</button>
                  </div>
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
        
    </DashboardLayout>
</template>

<script setup lang="ts">

  import { ref } from 'vue';
  const scrappingOn = ref(false);
  const analyseOn = ref(false);

  const alertEndOfScraping = ref(false);

  const analyseResult = ref(false);
  const analyseResultData = ref(null)

  const scrappResult = ref(false);
  const scrappResultData = ref(null);

  const disabled = ref(false);


  function setScrappingState(state: {scrappingState: boolean}) {
    console.log(state.scrappingState)
    scrappingOn.value = state.scrappingState
    if(state.scrappingState == false) {
      alertEndOfScraping.value = true;
      setTimeout(() => {
        alertEndOfScraping.value = false;
      }, 10000);
    }
  }

  function allocineScrapResult(result: any) {
    scrappResult.value = true;
    console.log(result)
    scrappResultData.value = result;
  }

  function analyseModelResult(result: any) {
    analyseResult.value = true;
    analyseResultData.value = result;
  }


  function setAnalyseState(state: {analyseState: boolean}) {
    analyseOn.value = state.analyseState
  }

</script>