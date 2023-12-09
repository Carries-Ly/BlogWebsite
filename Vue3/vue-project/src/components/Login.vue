<template>
  <div class="full_page_background">
    <NavBar />
    <canvas id="starCanvas"></canvas>
    <div class="quote">
      <h1>{{ quote }}</h1>
    </div>
    <div class="auth_box">
      <h2>{{ isLoginMode ? "用户登录" : "用户注册" }}</h2>
      <form @submit.prevent="isLoginMode ? loginUser() : registerUser()">
        <div v-if="!isLoginMode">
          <label for="name">用户名：</label>
          <input type="text" id="name" v-model="user.name" required />
        </div>
        <div>
          <label for="email">邮箱：</label>
          <input type="email" id="email" v-model="user.email" required />
        </div>
        <div v-if="!isLoginMode">
          <button type="button" @click="sendVerificationCode">
            发送验证码
          </button>
        </div>
        <div>
          <label for="password" class="label_password">密码：</label>
          <input
            type="password"
            id="password"
            v-model="user.password"
            required
          />
        </div>
        <div v-if="!isLoginMode">
          <label for="password_confirm">确认密码：</label>
          <input
            type="password"
            id="password_confirm"
            v-model="user.password_confirm"
            required
          />
        </div>
        <div v-if="!isLoginMode">
          <label for="verify">验证码：</label>
          <input type="text" id="verify" v-model="user.verify" required />
        </div>
        <button type="submit">{{ isLoginMode ? "登录" : "注册" }}</button>
        <button type="button" @click="toggleAuthMode">
          {{ isLoginMode ? "注册账号" : "已有账号，去登录" }}
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "@/plugins/axiosInstance.js";
import NavBar from "@/components/NavBar.vue";
import "element-plus/dist/index.css";

export default {
  data() {
    return {
      user: {
        name: "",
        email: "",
        password: "",
        password_confirm: "",
        verify: "",
      },
      quote:'"Only two things are infinite, the universe and human stupidity, and I\'m not sure about the former."',
      isLoginMode: true, // Toggle between login and register
      isCodeSent: false,
    };
  },
  components:{
    NavBar
  },
  mounted() {
    this.createStarryBackground();
  },
  methods: {
    createStarryBackground() {
      const canvas = document.getElementById("starCanvas");
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
    toggleAuthMode() {
      this.isLoginMode = !this.isLoginMode;
    },
    loginUser() {
      axios
        .post("/account/login", {
          email: this.user.email,
          password: this.user.password,
        })
        .then((response) => {
          console.log(response.data);
          // Redirect to dashboard or home page after login
          this.$router.push({ name: "Home" });
        })
        .catch((error) => {
          console.error(error);
        });
    },
    // 没有加上成功、错误信息提示！
    registerUser() {
      if (this.user.password !== this.user.password_confirm) {
        alert("密码和确认密码不一致");
        return;
      }
      axios
        .post("/account/register", this.user)
        .then((response) => {
          console.log(response.data);
          this.isLoginMode = true; // Switch to login mode after successful registration
        })
        .catch((error) => {
          console.error(error);
        });
    },
    sendVerificationCode() {
      axios
        .get(`/account/send_verify?email=${this.user.email}`)
        .then((response) => {
          console.log(response.data);
          this.isCodeSent = true;
        })
        .catch((error) => {
          console.error(error);
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

#starCanvas {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0;
  left: 0;
  z-index: -1; /* Ensure the canvas is behind your content */
}
.full_page_background {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  /* background-image: url("@/images/4398.jpg"); */
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  min-height: 100vh;
  /* width: 100vw; */
  overflow: hidden;
}
.quote {
  margin-top: 5em;
  margin-bottom: 5em; /* 在 quote 和 auth_box 之间添加一些空间 */
  color: white;
  text-align: center; /* 使文本居中显示 */
  font-size: 0.8rem;
  z-index: 1;
  /* text-shadow: #FC0 1px 0 10px; */
}

.auth_box {
  max-width: 100rem;
  padding: 2rem;
  margin-bottom: 80px;
  background: rgba(0, 0, 0, 0.2); /* 调整背景颜色的透明度 */
  border-radius: 1rem;
  box-shadow: 0 0 2rem rgba(255, 255, 255, 0.8);
  z-index: 2;
}

input[type="email"],
input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 1rem;
  margin: 1rem 0;
  border: 1px solid #ddd;
  box-shadow: 0 0 1rem rgba(255, 255, 255, 0.8);
  border-radius: 5px;
  background-color: rgba(0, 84, 178, 0.1);
  color: white;
  font-size: 0.8rem;
}

button {
  width: 100%;
  padding: 1.2em;
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

label {
  color: white;
  font-size: 1rem;
}

h2 {
  text-align: center;
  color: white;
  font-size: 2em; /* 显著增加标题字体大小 */
  text-shadow: 1px 1px 2px pink;
}
</style>
