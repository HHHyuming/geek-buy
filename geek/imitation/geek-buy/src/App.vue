<template>
  <div id="app">
    <div class="tabMenu">
      <TabMenu></TabMenu>
    </div>
    <div>
      <keep-alive>
        <router-view></router-view>
      </keep-alive>
    </div>
  </div>
</template>

<script>
import TabMenu from "./components/TabMenu";
export default {

  name: 'App',
  components: {
    TabMenu
  }
}
</script>

<style>
  body{
    height: 100vh;

  }
  .tabMenu{

  }

</style>
