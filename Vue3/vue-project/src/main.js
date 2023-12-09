import './assets/main.css'
//main.js
import { createApp } from 'vue'
import App from './App.vue'
import axios from '@/plugins/axiosInstance.js'
import router from '../router'; // 导入 router 配置
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';

// new Vue({
//   router, // 使用 router
//   render: h => h(App),
// }).$mount('#app');
const app = createApp(App);   //建立一个vue3app
app.use(router)
app.use(ElementPlus);
app.mount('#app');            //将这个vue3app全局挂载到#app元素上
app.config.globalProperties.$axios=axios;  //配置axios的全局引用

