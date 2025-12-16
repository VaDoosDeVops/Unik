import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import loadLayoutMiddleware from '@/router/middleware/loadLayout';
import LoadPage from '@/views/LoadPage.vue';
import ComparisonsPage from '@/views/ComparisonsPage.vue';
import { AppLayoutsEnum } from '@/layouts/layouts.types';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'login',
    component: LoadPage,
  },
  {
    path: '/load',
    name: 'load',
    component: LoadPage,
  },
  {
    path: '/differences',
    name: 'differences',
    component: ComparisonsPage,
    meta: {
      layout: AppLayoutsEnum.main,
    },
  },

];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

router.beforeEach(loadLayoutMiddleware);
export default router;
