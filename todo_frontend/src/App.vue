<script setup lang="ts">
import { ref, onMounted } from "vue";
import TodoForm from "./views/TodoForm.vue";
import { getAllTodosAPI } from "./api/todos";

interface Todo {
  id: number;
  title: string;
  is_completed: boolean;
}

const todos = ref<Todo[]>([]);

/** get Todos */
const getTodos = async () => {
  const res = await getAllTodosAPI();
  console.log(res);
  todos.value = res;
};

onMounted(async () => {
  await getTodos();
});
</script>

<template>
  <TodoForm :refetchTodos="getTodos" />
  <h1>待辦清單（Vue + Django API）</h1>
  <ul>
    <li v-for="todo in todos" :key="todo.id">
      {{ todo.title }} - {{ todo.is_completed ? "✅ 已完成" : "⏳ 未完成" }}
    </li>
  </ul>
</template>
