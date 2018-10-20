<template>
  <div>
    <b-embed type="iframe"
             src="https://calendly.com/argaghulamahmad"
             style="width:100%;height:100%;"
             aspect="16by9"
             tag="div"
             allowfullscreen
    ></b-embed>
  </div>
</template>

<script>
import bEmbed from 'bootstrap-vue/es/components/embed/embed';

export default {
  name: 'aCalendly',
  components: {
    bEmbed,
  },
};
</script>
