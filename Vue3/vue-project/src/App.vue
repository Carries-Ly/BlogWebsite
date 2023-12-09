<template>
  <div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {
    // If you have separate nav bar component, import and declare it here
  },
};
</script>

<style>
#app {
  padding: 0 !important;
  margin: 0 !important;
}
.el-header {
  background-color: rgb(0, 0, 0,0.5);

  line-height: 60px;
}

.el-menu-demo {
  background-color: transparent;
  color: white;
  border: none;
}
</style>
