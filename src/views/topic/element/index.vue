<template>
  <el-tabs style="padding-left: 10px">
    <el-tab-pane label="Show words"><show></show></el-tab-pane>
    <el-tab-pane label="Study"><study></study></el-tab-pane>
  </el-tabs>
</template>

<script>
  import show from './part/showTable'
  import study from './part/Study'
  export default {
    name: 'index',
    components: {
      show,
      study
    }
  }
</script>

<style scoped>

</style>
