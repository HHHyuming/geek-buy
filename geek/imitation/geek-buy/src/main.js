import Vue from 'vue'
import App from './App.vue'

import router from "./router";
import store from "./store";

import './config/rem'

import VueAMap from 'vue-amap'
Vue.use(VueAMap)
VueAMap.initAMapApiLoader({
  key:"832ebb11d87f83efd01ab68b5a46a554",
  plugin: ['AMap.Geolocation']
})
Vue.config.productionTip = false;

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app');
