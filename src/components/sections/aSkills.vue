<template>
  <section class="resume-section p-3 p-lg-5 d-flex flex-column" id="skills">
    <div class="my-auto">
      <h2 class="mb-5">Skills</h2>
      <div class="weight">
        <div class="subheading mb-3">Programming Languages &amp; Tools</div>
        <div>
          <ul class="list-inline list-icons">
            <li v-for="(item, index) in programmingLanguagesTools" :key="index"
                class="list-inline-item">
              <i :class="item['icon-class']"></i>
            </li>
          </ul>
        </div>
        <div class="subheading mb-3">Workflow</div>
        <ul class="fa-ul mb-0">
          <li v-for="(workflow, index) in workflows" :key="index">
            <i class="fa-li fa fa-check"></i>
            {{workflow['title']}}
          </li>
        </ul>
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
  name: 'aSkills',
  data() {
    return {
      programmingLanguagesTools: [],
      workflows: [],
      loading: true,
    };
  },
  components: {
    aSpinner,
  },
  beforeCreate() {
    axios
      .get('/data/skills/programming-languages-tools.json')
      .then((response) => {
        const data = response.data;
        const programmingLanguagesTools = [];
        Object.keys(data).map((key) => {
          const item = data[key];
          item.id = key;
          programmingLanguagesTools.push(item);
        });
        this.programmingLanguagesTools = programmingLanguagesTools;
      })
      .catch((e) => {
        console.log(e);
      });

    axios
      .get('/data/skills/workflows.json')
      .then((response) => {
        const data = response.data;
        const workflows = [];
        Object.keys(data).map((key) => {
          const item = data[key];
          item.id = key;
          workflows.push(item);
        });
        this.workflows = workflows;
        this.loading = false;
      })
      .catch((e) => {
        console.log(e);
      });
  },
};
</script>
