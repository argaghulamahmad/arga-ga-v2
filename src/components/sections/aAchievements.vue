<template>
  <section class="resume-section p-3 p-lg-5 d-flex flex-column" id="awards">
    <div class="my-auto">
      <h2 class="mb-5">Achievements</h2>
      <ul class="fa-ul mb-0 weight">
        <li v-for="(achievement, index) in achievements" :key="index">
          <i class="fa-li fa fa-trophy text-warning"></i>
          {{achievement.title}}
        </li>
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
  name: 'aAwards',
  data() {
    return {
      achievements: [],
      loading: true,
    };
  },
  components: {
    aSpinner,
  },
  beforeCreate() {
    axios
      .get('/api/achievement/')
      .then((response) => {
        this.achievements = response.data;
        this.loading = false;
      })
      .catch((e) => {
        console.log(e);
      });
  },
};
</script>
