<template>
  <section class="resume-section p-3 p-lg-5 d-flex d-column" id="about">
    <div class="my-auto weight center">
      <h1 class="mb-0">Hi, Everyone! My name is
        <br>
        <span class="text-primary">Arga Ghulam Ahmad</span>
      </h1>
      <p class="mb-5">A computer science student at Fasilkom, Universitas Indonesia. Who is eager to learn software development and try to develop an useful application. I am driven to be a software engineer.</p>
      <b-container>
        <b-row>
          <b-col v-for="social in socials" :key="social.name">
            <a :href="social.link" target="_blank">
              <i :class="getSocialIconClass(social.name)"></i>
            </a>
          </b-col>
        </b-row>
      </b-container>
    </div>
    <aSpinner v-if="loading"></aSpinner>
  </section>
</template>

<script>
/* eslint-disable no-console,array-callback-return */

import axios from 'axios';
import aSpinner from '../partials/aSpinner';

export default {
  name: 'aAboutMe',
  data() {
    return {
      socials: [],
      loading: true,
    };
  },
  components: {
    aSpinner,
  },
  methods: {
    getSocialIconClass(socialName) {
      return `fa fa-${socialName}`;
    },
  },
  beforeCreate() {
    axios
      .get('/api/social/')
      .then((response) => {
        this.socials = response.data;
        this.loading = false;
      })
      .catch((e) => {
        console.log(e);
      });
  },
};
</script>
