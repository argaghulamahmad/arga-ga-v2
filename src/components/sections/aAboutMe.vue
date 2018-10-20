<template>
  <section class="resume-section p-3 p-lg-5 d-flex d-column" id="about">
    <div class="my-auto weight center">
      <h1 class="mb-0">Hi, Everyone! My name is
        <br>
        <span class="text-primary">{{this.firstName}} {{this.lastName}}</span>
      </h1>
      <p class="mb-5">{{this.description}}</p>
      <b-container>
        <b-row>
          <b-col v-for="social in socials" :key="social['name']">
            <a :href="social['url']" target="_blank">
              <i :class="getSocialIconClass(social['name'])"></i>
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
      firstName: '',
      lastName: '',
      email: '',
      description: '',
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
      .get('/data/about-me.json')
      .then((response) => {
        // console.log(response.data);
        this.firstName = response.data['first-name'];
        this.lastName = response.data['last-name'];
        this.email = response.data.email;
        this.description = response.data.description;
      })
      .catch((e) => {
        console.log(e);
      });

    axios
      .get('/data/social.json')
      .then((response) => {
        // console.log(response.data);
        const data = response.data;
        const socials = [];
        Object.keys(data).map((key) => {
          const social = data[key];
          social.id = key;
          socials.push(social);
        });
        this.socials = socials;
        this.loading = false;
        // console.log(this.socials);
      })
      .catch((e) => {
        console.log(e);
      });
  },
};
</script>
