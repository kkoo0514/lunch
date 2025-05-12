import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import {router} from './router'

// Vuetify 관련 import
import { createVuetify } from "vuetify";
import 'vuetify/styles';
import { aliases, mdi } from 'vuetify/iconsets/mdi'; // Materail Design Icons

// Vuetify 인스턴스 생성
const vuetify = createVuetify({
    icons: {
      defaultSet: 'mdi', // 기본 아이콘 설정
        aliases,
        sets: {
          mdi,
        },
    },
});

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(vuetify);

app.mount('#app');
