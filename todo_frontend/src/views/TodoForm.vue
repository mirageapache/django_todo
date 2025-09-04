<script setup lang="ts">
import { createTodoAPI } from "@/api/todos";
import { ref } from "vue";

const newTodo = ref("");
const emit = defineEmits<{
  (e: "refetchTodos"): void;
}>();

async function addTodo() {
  if (!newTodo.value) return;
  const res = await createTodoAPI(newTodo.value);
  console.log(res);
  emit("refetchTodos");
  newTodo.value = ""; // 清空輸入框
}
</script>

<template>
  <input v-model="newTodo" placeholder="輸入新任務" />
  <button @click="addTodo">新增</button>
</template>
