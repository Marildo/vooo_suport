import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue')
  },
  {
    path: '/client',
    name: 'Client',
    component: () => import('@/views/Client.vue')
  },
  {
    path: '/conectores',
    name: 'Conectores',
    component: () => import('@/views/About.vue')
  },
  {
    path: '/monitoramento',
    name: 'Monitoramento',
    component: () => import('@/views/About.vue')
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
