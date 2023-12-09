
<template>
  <div class="full_page_background">
    <div class="register_box">
      <h2>用户注册</h2>
      <form @submit.prevent="registerUser">
        <div>
          <label for="email">邮箱：</label>
          <input type="email" id="email" v-model="user.email" required />
          <button @click="sendVerificationCode">发送验证码</button>
        </div>
        <div>
          <label for="name">用户名：</label>
          <input type="text" id="name" v-model="user.name" required />
        </div>
        <div>
          <label for="password">密码：</label>
          <input
            type="password"
            id="password"
            v-model="user.password"
            required
          />
        </div>
        <div>
          <label for="password_confirm">确认密码：</label>
          <input
            type="password"
            id="password_confirm"
            v-model="user.password_confirm"
            required
          />
        </div>
        <div>
          <label for="verify">验证码：</label>
          <input type="text" id="verify" v-model="user.verify" required />
        </div>
        <button type="submit">注册</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "@/plugins/axiosInstance.js";

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
      isCodeSent: false,
    };
  },
  methods: {
    registerUser() {
      if (this.user.password !== this.user.password_confirm) {
        alert("密码和确认密码不一致");
        return;
      }

      axios
        .post("/account/register", this.user)
        .then((response) => {
          console.log(response.data);
          // this.$router.push("/login"); // 假设有一个登录的路由
          window.location.href = 'Login.html';
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
body, html {
  margin: 0;
  padding: 0;
  height: 100%;
}

.full_page_background {
  display: flex;
  justify-content: center;
  align-items: center;
  background-image: url("@/images/4398.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  min-height: 100vh;
  width: 100vw;
}

.register_box {
  max-width: 500px;
  padding: 20px;
  background: rgba(255, 255, 255, 0.8); /* 调整背景颜色的透明度 */
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.8);
}

input[type="email"],
input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ddd;
  border-radius: 5px;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

h2 {
  text-align: center;
}
</style>
