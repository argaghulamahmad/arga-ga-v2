<template>
  <div class="contactContainer p-3 p-lg-5 d-flex flex-column my-auto">
    <h2 class="mb-5">Contact</h2>
    <b-list-group>
      <b-list-group-item v-for="(contact, index) in contacts" :key="index">
        <i :class="iconClass(contact.icon)"></i>
        {{contact.content}}
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
/* eslint-disable no-console,array-callback-return */

import axios from 'axios';
import bListGroup from 'bootstrap-vue/es/components/list-group/list-group';
import bListGroupItem from 'bootstrap-vue/es/components/list-group/list-group-item';

export default {
  name: 'aContact',
  components: {
    bListGroup,
    bListGroupItem,
  },
  methods: {
    iconClass(icon) {
      return `fa fa-${icon}`;
    },
  },
  data() {
    return {
      contacts: [],
    };
  },
  beforeCreate() {
    axios
      .get('/data/contact-me/contact.json')
      .then((response) => {
        const data = response.data;
        const contacts = [];
        Object.keys(data).map((key) => {
          const item = data[key];
          item.id = key;
          contacts.push(item);
        });
        this.contacts = contacts;
      })
      .catch((e) => {
        console.log(e);
      });
  },
};
</script>
