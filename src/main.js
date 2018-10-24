import Vue from 'vue'
import App from '@/App.vue'
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import VueRouter from 'vue-router';
import axios from 'axios';
import firebase from 'firebase/app';
import 'firebase/auth';
import { routes } from './router/routes';
import { store } from './store/store';
import './sass/init.scss';
import $backend from '@/backend'
Vue.prototype.$backend = $backend
Vue.config.productionTip = false

Vue.use(BootstrapVue);
Vue.use(VueRouter);

axios.defaults.baseURL = 'https://arga-ga-backend.firebaseio.com/';
axios.defaults.headers.get.Accepts = 'application/json';

const config = {
  apiKey: 'AIzaSyDKkCGqULqtZnbfeEWpZwp7xXbCKlH3xX0',
  authDomain: 'arga-ga-backend.firebaseapp.com',
  projectId: 'arga-ga-backend',
};

firebase.initializeApp(config);
firebase.auth.Auth.Persistence.NONE;

const router = new VueRouter({
  routes,
  mode: 'history',
});

const vue = new Vue({
  store,
  router,
  render: h => h(App)
})

vue.$mount('#app')
