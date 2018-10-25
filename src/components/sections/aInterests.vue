<template>
  <section class="resume-section p-3 p-lg-5 d-flex flex-column" id="interests">
    <div class="my-auto">
      <h2 class="mb-5">Interests</h2>
      <ul class="weight">
        <li v-for="(interest, index) in interests" :key="index">{{interest.content}}</li>
      </ul>
    </div>
    <aSpinner v-if="loading"></aSpinner>
  </section>
</template>

<script>
/* eslint-disable no-console,array-callback-return */

import axios from 'axios';
import aSpinner from '../partials/aSpinner';

export default {
  name: 'aInterests',
  data() {
    return {
      interests: [],
      loading: true,
    };
  },
  components: {
    aSpinner,
  },
  beforeCreate() {
    axios
      .get('/api/interest/')
      .then((response) => {
        this.interests = response.data;
        this.loading = false;
      })
      .catch((e) => {
        console.log(e);
      });
  },
};
</script>
