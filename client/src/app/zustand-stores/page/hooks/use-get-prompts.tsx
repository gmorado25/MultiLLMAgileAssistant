"use client";
import { setPrompts } from "../store/LLM-store";

const useGetPrompts = async () => {
  try {
    // make an API call the the /generate endpoint, pass in the prompts, list of models to query, etc.
    const res = await fetch("http://localhost:8000/prompts/", {
      method: "GET",
      headers: {
        "Content-type": "application/json; charset=UTF-8",
      },
    });

    // parse the returned json
    const data = await res.json();
    setPrompts(data);
  } catch (err) {
    console.log(err);
  }
  return;
};

export default useGetPrompts;
