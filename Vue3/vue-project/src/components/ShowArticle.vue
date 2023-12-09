<template>
    <div class="blog-list-container">
      <el-scrollbar style="height: 100%;">
        <el-card
          v-for="article in articles"
          :key="article.id"
          class="article-card"
          @click="readArticle(article.id)"
        >
          <div slot="header" class="clearfix">
            <h2>{{ article.title }}</h2>
            
          </div>
          <div class="article-cover">
            <img :src="article.cover" alt="Article cover" />
          </div>
          <div slot="foot" class="footbutton">
            <el-button style=" padding: 3px 0" type="text">click to read</el-button>
          </div>
        </el-card>
      </el-scrollbar>
    </div>
  </template>
  
  <script>
  import { ref, onMounted, defineComponent } from 'vue';
  import axios from '../plugins/axiosInstance';
  
  export default defineComponent({
    name: 'ArticleList',
  
    setup() {
      const articles = ref([]);
  
      onMounted(async () => {
        try {
          const response = await axios.get('/article/get_all_articles');
          articles.value = response.data;
          console.log(articles.value)
        } catch (error) {
          console.error('Error fetching articles:', error);
        }
      });
  
      const readArticle = async (articleId) => {
        try {
          const response = await axios.get(`/article/get_article/${articleId}`);
          // Handle reading the article, e.g., opening a modal or navigating to a page with the article content
          console.log(response.data);
        } catch (error) {
          console.error('Error fetching article:', error);
        }
      };
  
      // Export the reactive state and methods
      return {
        articles,
        readArticle
      };
    }
  });
  </script>
  
  <style scoped>
  .blog-list-container {
    display: inline-block;
    height: 80em; /* Adjust as needed */
    padding: 2em;
    width: 60%;
    border-radius: 15px;
    background-color: rgb(255,255,255,1);
  }
  
  .article-card {
    cursor: pointer;
    margin-bottom: 1em;
    box-shadow: 0 0 2rem rgba(0, 0, 0, 0.8);;
  }
  
  .article-cover img {
    width: 100%;
    height: auto;
    max-height: 50em; /* Adjust as needed */
    padding: auto;
    object-fit: cover;
    border-radius: 15px;
    box-shadow: 0 0 10px rgba(255, 255, 255, 0.8);;
  }
  .clearfix h2{
    text-align: center;
    font-size: 2em;
    border:0.5em solid red;
    border-radius: 15px;
    margin-bottom: 1em;
  }
  .footbutton{
    text-align: center;
  }
  </style>
  