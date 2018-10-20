<template>
  <section class="resume-section p-3 p-lg-5 d-flex flex-column" id="projects">
    <div class="my-auto">
      <h2 class="mb-5">Projects</h2>
      <div v-for="(project, index) in projects" :key="index"
           class="resume-item d-flex flex-column flex-md-row mb-5">
        <div class="resume-content mr-auto">
          <h3 class="mb-0 weight">{{project['name']}}</h3>
          <div class="subheading mb-3 weight">
            <a :href="project['url']" target="_blank">
            {{project['url']}}
            </a>
          </div>
          <div class="div--stacks">
            <div class="tag" v-for="(stack, index) in project['stacks']" :key="index">
              {{stack}}
            </div>
          </div>
          <br>
          <ul>
            <li v-for="(desc, index) in project['description']" :key="index"
                class="weight">
              {{desc}}
            </li>
          </ul>
        </div>
        <div class="resume-date text-md-right weight">
          <span class="text-primary">{{project['from']}} - {{project['to']}}</span>
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
  name: 'aProjects',
  data() {
    return {
      projects: [],
      loading: true,
    };
  },
  components: {
    aSpinner,
  },
  beforeCreate() {
    axios
      .get('/data/projects.json')
      .then((response) => {
        const data = response.data;
        const projects = [];
        Object.keys(data).map((key) => {
          const project = data[key];
          project.id = key;
          projects.push(project);
        });
        this.projects = projects;
        this.loading = false;
      })
      .catch((e) => {
        console.log(e);
      });
  },
};
</script>
