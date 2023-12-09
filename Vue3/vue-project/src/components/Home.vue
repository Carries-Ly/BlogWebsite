<template>
  <div class="full_page_container">
    <NavBar />
    <canvas id="stars"></canvas>
    <div class="content-container">
      <div class="left-container">

      </div>
      <div class="center-container">
        <ArticleList />
      </div>
      <div class="right-container">
        <Player />
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import ArticleList from "./ShowArticle.vue"
import Player from "./MusicPlayer.vue"
export default{
  components:{
    NavBar,
    ArticleList,
    Player
  },
  mounted() {
    this.createStarryBackground();
  },
  methods : {
    createStarryBackground() {
      const canvas = document.getElementById("stars");
      const ctx = canvas.getContext("2d");

      function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
      }
      window.addEventListener("resize", resizeCanvas);
      resizeCanvas();

      const stars = []; // Array to hold our stars
      function addStar() {
        const x = Math.random() * canvas.width;
        const y = Math.random() * canvas.height;
        const radius = Math.random() * 1.5;
        const opacity = Math.random();
        stars.push({ x, y, radius, opacity });
      }

      // Create 100 stars
      for (let i = 0; i < 520; i++) {
        addStar();
      }

      function drawStars() {
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
        ctx.fillStyle = "#000";
        ctx.fillRect(0, 0, canvas.width, canvas.height); // Fill the background with black

        // Draw each star
        stars.forEach((star) => {
          ctx.beginPath();
          ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2, false);
          ctx.fillStyle = `rgba(255, 255, 255, ${star.opacity})`;
          ctx.fill();
        });
      }

      function updateStars() {
        stars.forEach((star) => {
          star.opacity += (Math.random() - 0.5) * 0.2; // Randomly change the opacity
          if (star.opacity < 0) star.opacity = 0;
          if (star.opacity > 1) star.opacity = 1;
        });
      }

      function animate() {
        updateStars();
        drawStars();
        requestAnimationFrame(animate); // Animate the stars
      }

      animate();
    },
  }
}
</script>

<style scoped>
body,
html {
  margin: 0;
  padding: 0;
  height: 100%;
  font-size: 0.625em;
}

#starCanvas {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0;
  left: 0;
  z-index: -1; /* Ensure the canvas is behind your content */
}
.full_page_container {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  min-height: 100vh;
  /* width: 100vw; */
  overflow: hidden;
}
.content-container{
  display: flex;
  margin-top: 8em;
}
#stars {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0;
  left: 0;
  z-index: -1; /* Ensure the canvas is behind your content */
}
.center-container{
  display: flex;
  background-color: transparent;
  justify-content: center;  
}

</style>