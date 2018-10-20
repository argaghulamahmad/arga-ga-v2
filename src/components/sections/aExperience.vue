<template>
  <section class="resume-section p-3 p-lg-5 d-flex flex-column" id="experience">
    <div class="my-auto">
      <h2 class="mb-5">Experience</h2>
      <div v-for="(experience, index) in experiences" :key="index">
        <div class="resume-item d-flex flex-column flex-md-row mb-5">
          <div>
            <div class="image"><img :src="experience['company-logo']"
                                    :alt="experience['company']"></div>
          </div>
          <div class="resume-content mr-auto">
            <h3 class="mb-0 weight">{{experience['title']}}</h3>
            <div class="subheading mb-3 weight">
              <a :href="experience['company-url']"
                 target="_blank">{{experience['company']}}</a>
            </div>
            <div class="div--stacks">
              <div class="tag" v-for="(stack, index) in experience['stacks']" :key="index">
                {{stack}}
              </div>
            </div>
            <br>
            <ul>
              <li v-for="(desc, index) in experience['description']" :key="index" class="weight">
                {{desc}}
              </li>
            </ul>
          </div>
          <div class="resume-date text-md-right weight">
            <span class="text-primary">
              {{experience['location']}}
            </span>
            <br>
            <span class="text-primary">
              {{experience['from']}} - {{experience['to']}}
            </span>
          </div>
          <br>
        </div>
      </div>
    </div>
    <aSpinner v-if="loading"></aSpinner>
  </section>

</template>

<script>
/* eslint-disable no-console,array-callback-return */
import axios from 'axios';
import aSpinner from '../partials/aSpinner';

export default {
  name: 'aExperience',
  data() {
    return {
      experiences: [],
      loading: true,
    };
  },
  components: {
    aSpinner,
  },
  beforeCreate() {
    axios
      .get('/data/experience.json')
      .then((response) => {
        const data = response.data;
        const experiences = [];
        Object.keys(data).map((key) => {
          const experience = data[key];
          experience.id = key;
          experiences.push(experience);
        });
        this.experiences = experiences.reverse();
        this.loading = false;
      })
      .catch((e) => {
        console.log(e);
      });
  },
};
</script>
