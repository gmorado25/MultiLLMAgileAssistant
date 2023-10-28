"use client";
import axios from "axios";
import { setPrompts, getCookie } from "../store/LLM-store";

const useGetPrompts = async () => {
  try {
    const csrftoken = getCookie('csrftoken');
    // make an API call the the /generate endpoint, pass in the prompts, list of models to query, etc.
    const config = {
      headers: {
          'content-type': 'application/json',
          'X-CSRFToken': csrftoken,
      }
    }
    axios.get("/prompts.json", config).then((response: any) => {
      const data = response.data;
      console.log(response)
      setPrompts(data);
    });
  } catch (err) {
    console.log(err);
  }
  return;
};

export default useGetPrompts;
