<template>
    <div class="p-5 flex flex-col md:flex-row items-center justify-center ">
        <button v-if="scrappingOn==false" @click="startScraping" class="btn btn-primary mt-2 md:mt-0 md:ml-2 md:w-initial">Lancer le scrapping</button>
        <!-- <button v-if="scrappingOn==true && analyseOn==false" @click="stopScraping" class="btn btn-primary mt-2 md:mt-0 md:ml-2 md:w-initial">Arrêter le processus</button> -->
        <button v-if="scrappingOn==false && analyseOn==false"  @click="startAnalyse" class="btn btn-primary mt-2 md:mt-0 md:ml-2 md:w-initial">Analyser</button>
    </div>
</template>

<script setup lang="ts">

    const emit = defineEmits(['on-scrapping-state', 'on-analyse-state', 'on-analyse-result', 'on-scrapping-result'])

    const props = defineProps({
        scrappingOn: {
            type: Boolean,
            required: true,
        },
        analyseOn: {
            type: Boolean,
            required: true,
        },
    });


    async function startScraping() {
        emit('on-scrapping-state', {scrappingState: true})

        try {
            console.log("Scraping en cours...");
            let url = "http://127.0.0.1:8000/api/start_scraping/"
            fetch(url, {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            }
            })
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then((response) => {
                console.log(response)
                console.log('fin')
                emit('on-scrapping-state', {scrappingState: false})
                emit('on-scrapping-result', {result: response})
            })
            .catch((error) => {
                emit('on-scrapping-state', {scrappingState: false})
                console.error(error);
            });
        }
        catch (error) {
            emit('on-scrapping-state', {scrappingState: false})
            console.error('Erreur lors du lancement du scrapping', error);
        }
        
    }

    function stopScraping() {
        emit('on-scrapping-state', {scrappingState: false})
    }

    function startAnalyse() {
        emit('on-analyse-state', {analyseState: true})

        try {
            console.log("Prediction en cours...");
            let url = "http://127.0.0.1:8000/api/predict/"
            fetch(url, {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json',
                }
            })
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then((response) => {
                console.log(response)
                console.log('fin')
                emit('on-analyse-state', {analyseState: false})
                emit('on-analyse-result', response)
            })
            .catch((error) => {
                emit('on-analyse-state', {analyseState: false})
                console.error(error);
            });

            
        }
        catch (error) {
            emit('on-analyse-state', {analyseState: false})
            console.error('Erreur lors du lancement de la prediction', error);
        }
    }

</script>