"use client";
import * as React from "react";
import { setOutputData } from "../store/LLM-store";
import { setPrompts } from "../store/LLM-store";

const useGenerate = async () => {
  try {
    // make an API call the the /generate endpoint, pass in the prompts, list of models to query, etc.
    const res = await fetch("http://localhost:8000/generate/", {
      method: "POST",
      body: JSON.stringify({
        models: ["GPT3.5", "Bard", "Claude", "Test"],
        prompt:
          "You are a helpful assistant who solves math problems. Write the following equation using algebraic symbols then show the steps to solve the problem:",
        data: "x^3 + 7 = 12",
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8",
      },
    });

    // parse the returned json
    const data = await res.json();
    setOutputData(data);
  } catch (err) {
    console.log(err);
  }
  return;
};

export default useGenerate;
