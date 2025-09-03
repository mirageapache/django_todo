<script setup lang="ts">
import { ref, onMounted } from "vue";

interface Todo {
  id: number;
  title: string;
  is_completed: boolean;
}

const todos = ref<Todo[]>([]);

onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/api/todos/");

  console.log(res);
  todos.value = await res.json();
});
</script>

<template>
  <h1>待辦清單（Vue + Django API）</h1>
  <ul>
    <li v-for="todo in todos" :key="todo.id">
      {{ todo.title }} - {{ todo.is_completed ? "✅ 已完成" : "⏳ 未完成" }}
    </li>
  </ul>
</template>
