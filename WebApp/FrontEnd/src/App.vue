<template>
  <div id="app">
      {{ msg }}
      <div>
        <input type="text" v-model="info">
        <button v-on:click="handleClick">添加</button>
      </div>
    <ul>
        <todo-item v-for="item in list" :key="item" :item="item"></todo-item>
    </ul>
  </div>
</template>

<script>
import TodoItem from './components/TodoItem.vue'

export default {
  name: 'app',
  data(){
      return{
          msg: 'Hello Vue',
          info: '',
          list: [],
      }
  },
  methods:{
      handleClick(){
          this.list.push(this.info)
          this.info = ''
      }
  },
  components: {
      TodoItem
  }
}
</script>

<style>
    .item{
        color: red;
    }
</style>
