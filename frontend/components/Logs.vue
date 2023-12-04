<template>
    <div class="mockup-window border bg-base-300">
        <div class="px-4 py-16 bg-base-200 h-96 overflow-auto py-10">
            <p>
                Nombre de commentaires scrappés par film : {{ scrappResultData.result.max_reviews_per_film }}
            </p>
        </div>
    </div>
</template>

<script setup lang="ts">

const props = defineProps({
    scrappResultData: {
        required: false,
    }
});

</script>