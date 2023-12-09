// router.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/components/Home.vue';
import Login from '@/components/Login.vue';
import Register from '@/components/Register.vue';
import Article_md from '@/components/Article_md.vue';
import ShowArticle from '@/components/ShowArticle.vue';
import MusicPlayer from '@/components/MusicPlayer.vue';
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/article_editor',
    component: Article_md
  },
  {
    path: '/article_show',
    component: ShowArticle
  },
  {
    path: '/music_player',
    component: MusicPlayer
  }
  // 可以继续添加更多的路由规则
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
