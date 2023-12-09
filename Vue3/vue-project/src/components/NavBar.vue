<template>
    <div class="container">
        <div class="nav-bar">
        <el-header class="el-header">
        <el-menu
            default-active="2-4"
            class="el-menu"
            mode="horizontal"
            @select="handleSelect"
            background-color="rgb(84,92,100,0.1)"
            text-color="white"
            active-text-color="#ffd04b"
            router="true"
        >
            <el-menu-item index="1" route="/">Home Page</el-menu-item>
            <el-menu-item index="2" route="/article_editor">Article-Editor</el-menu-item>
            <el-menu-item index="3" route="/login">Login</el-menu-item>
            <el-sub-menu index="4">
            <template #title>Workspace</template>
            <el-menu-item index="4-1" >item one</el-menu-item>
            <el-menu-item index="4-2">item two</el-menu-item>
            <el-menu-item index="4-3">item three</el-menu-item>
            <el-sub-menu index="4-4">
                <template #title>item four</template>
                <el-menu-item index="4-4-1">item one</el-menu-item>
                <el-menu-item index="4-4-2">item two</el-menu-item>
                <el-menu-item index="4-4-3">item three</el-menu-item>
            </el-sub-menu>
            </el-sub-menu>
            
        </el-menu>
        </el-header>
    </div>
    </div>
</template>
<script>
export default{
    data(){
        return {}
    },
    methods:{

    },
};
</script>
<style scoped>
/*虽然会有高度塌陷，但是这样可以解决navbar的背景颜色问题*/
.container{
    /* height: 5em; */  
}
.nav-bar {
  position: fixed;
  height: 5em;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 10; /* Higher than other elements to stay on top */
}
.el-header{
    background-color: transparent !important;
    width: 100%;

}
</style>