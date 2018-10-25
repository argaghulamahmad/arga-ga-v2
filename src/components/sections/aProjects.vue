<template>
  <section class="resume-section p-3 p-lg-5 d-flex flex-column" id="projects">
    <div class="my-auto">
      <h2 class="mb-5">Projects</h2>
      <div v-for="(project, index) in projects" :key="index"
           class="resume-item d-flex flex-column flex-md-row mb-5">
        <div class="resume-content mr-auto">
          <h3 class="mb-0 weight">{{project.name}}</h3>
          <div class="subheading mb-3 weight">
            <a :href="project.project_url" target="_blank">
            {{project.project_url}}
            </a>
          </div>
          <!--<div class="div&#45;&#45;stacks">
            <div class="tag" v-for="(stack, index) in project['stacks']" :key="index">
              {{stack}}
            </div>
          </div>-->
          <br>
          <!--<ul>
            <li v-for="(desc, index) in project['description']" :key="index"
                class="weight">
              {{desc}}
            </li>
          </ul>-->
          <pre style="white-space: pre-line; word-wrap: break-word; text-align: justify;">
            {{project.description}}
          </pre>
        </div>
        <div class="resume-date text-md-right weight">
          <span class="text-primary">{{project.start_date}} - {{project.end_date}}</span>
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
      .get('/api/project/')
      .then((response) => {
        this.projects = response.data;
        this.projects.reverse();
        this.loading = false;
      })
      .catch((e) => {
        console.log(e);
      });
  },
};
</script>
