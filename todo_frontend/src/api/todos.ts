import axios from "axios";

const api_url = "http://127.0.0.1:8000/api/todos/";

interface todoParamType {
  title: string;
  description: string;
  is_completed: boolean;
  created_at?: string;
  updated_at?: string;
}

/** get all todos */
export async function getAllTodosAPI() {
  const res = await fetch(api_url);
  return res.json();
}

/** create a new todo */
export async function createTodoAPI(title: string,) {
  const params: todoParamType = {
    title: title,
    description: "",
    is_completed: false,
  };

  const res = await axios.post(api_url, params, {
    headers: {
      'Content-Type': 'application/json',
    },
  })
  return res.data;
}