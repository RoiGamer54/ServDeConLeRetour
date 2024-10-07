// main.js
import { createApp } from 'vue'; // Change this line
import App from './App.vue';
import router from './router';

const app = createApp(App); // Use createApp instead of new Vue
app.use(router); // Use app.use() to install the router
app.mount('#app'); // Mount the app to the DOM
