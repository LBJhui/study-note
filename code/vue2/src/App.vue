<template>
  <div id="app">
    <my-button type="success" @click="output">我的按钮</my-button>
  </div>
</template>

<script>


export default {
  name: 'App',
  methods: {
    output (e) {
      console.log(e)
    }
  }
}
</script>
