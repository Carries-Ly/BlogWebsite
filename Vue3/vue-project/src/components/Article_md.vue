<template>
  <div id="full_page_container">
    <nav-bar></nav-bar>
    <!-- NavBar 组件 -->
    <canvas id="stars"></canvas>
    <div class="editor_container">
      <div id="editor"></div>
      <button @click="changeDialog">Submit</button>
      <el-dialog v-model="showDialog" title="Submit Article" width="40%">
        <div class="inDialog">
          <label for="title">Title:</label>
          <input type="text" id="title" v-model="articleTitle" />
        </div>
        <div class="inDialog">
          <label for="cover">Cover Image:</label>
          <input type="file" id="cover" @change="handleCoverChange" />
        </div>
        <span slot="footer" class="dialog-footer">
          <button @click="changeDialog">Cancel</button>
          <button @click="submitArticle">Confirm</button>
        </span>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import axios from "@/plugins/axiosInstance.js";
import Editor from "@toast-ui/editor";
import "element-plus/dist/index.css";
import "@toast-ui/editor/dist/toastui-editor.css";
import NavBar from "@/components/NavBar.vue";
import { ElDialog } from "element-plus";

export default {
  data() {
    return {
      editor: null,
      showDialog: false,
      articleTitle: "",
      coverImage: null,
    };
  },
  mounted() {
    this.createStarryBackground();
    this.initEditor();
  },
  components: {
    "nav-bar": NavBar,
    ElDialog,
  },
  methods: {
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
    changeDialog(){
        console.log(this.showDialog);
        this.showDialog = !this.showDialog;
    },
    initEditor() {
      this.editor = new Editor({
        el: document.querySelector("#editor"),
        previewStyle: "vertical",
        height: "100%",
        theme: "dark",
      });
    },
    handleCoverChange(event) {
      this.coverImage = event.target.files[0];
    },
    submitArticle() {
      const formData = new FormData();
      formData.append("title", this.articleTitle);
      formData.append("content", this.editor.getMarkdown());
      if (this.coverImage) {
        formData.append("cover", this.coverImage);
      }
      axios
        .post("/article/create_article", formData, {
          headers: { "Content-Type": "multipart/form-data" },
        })
        .then((response) => {
          // 成功处理
          console.log(response)
          this.showDialog = false;
          this.articleTitle = "";
          this.coverImage = null;
        })
        .catch((error) => {
          console.log(error)
        });
    },
  },
};
</script>

<style scoped>
body,
html {
  margin: 0;
  padding: 0;
  height: 100%;
  font-size: 0.625em;
}
#full_page_container {
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
  /* overflow: hidden; */
}

#stars {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0;
  left: 0;
  z-index: -1; /* Ensure the canvas is behind your content */
}



.editor_container {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 70%;
  height: 80%;
  margin-top: 20em;
  margin-bottom: 14em;
  padding: 2em;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0px 0.5em 1em rgba(0, 0, 0, 0.1);
  background-color: rgb(255, 255, 255, 0.6);
}

#editor {
  width: 100%;
  height: 100%;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 2em;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

button {
  width: 10%;
  margin-top: 0.8em;
  padding: 0.8em;
  background-color: rgba(0, 0, 0, 0.2);
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
}

button:hover {
  background-color: rgba(0, 0, 0, 0.2);
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
}
#title,
#cover {
  margin-bottom: 1em;
  width: 100%;
  padding: 0.5em;
  border: 1px solid #ddd;
  border-radius: 5px;
}
.inDialog label{
  color: black;
  font-size: 1rem;

}
span button{
    width: 30%;
    margin-top: 2em;
    padding: 1em 1em 1em ;
    background-color: rgba(198, 192, 192, 0.2);
    border: 0;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
    color: black;
}
</style>
