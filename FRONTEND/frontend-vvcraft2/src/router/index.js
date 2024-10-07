import { createRouter, createWebHistory } from 'vue-router'; 
import Accueil from '@/pages/AcceuilPage.vue';
import Serveurs from '@/pages/ServeurPage.vue';
import Test from '@/pages/TestPage.vue';

const routes = [
  {
    path: '/',
    name: 'Accueil',
    component: Accueil
  },
  {
    path: '/serveurs',
    name: 'Serveurs',
    component: Serveurs
  },
  {
    path: '/test',
    name: 'test',
    component: Test
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
