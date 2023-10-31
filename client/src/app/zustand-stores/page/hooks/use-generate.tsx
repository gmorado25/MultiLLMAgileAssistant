"use client";
import * as React from "react";
import { setOutputData, getCookie } from "../store/LLM-store";
import { setPrompts } from "../store/LLM-store";
const axios = require('axios').default;

const useGenerate = async () => {
  try {
    const csrftoken = getCookie('csrftoken');

    const body = JSON.stringify({
      models: ["GPT3.5", "Bard", "Claude", "Test"],
      prompt:
        "You are a helpful assistant who solves math problems. Write the following equation using algebraic symbols then show the steps to solve the problem:",
      data: "x^3 + 7 = 12",
    })

    // make an API call the the /generate endpoint, pass in the prompts, list of models to query, etc.
    const config = {
      headers: {
          'content-type': 'application/json',
          'X-CSRFToken': csrftoken,
      }
    }
    axios.post("/generate.json", body, config).then((response: any) => {
      const data = response.data;
      console.log(response)
      setOutputData(data);
    });

    // const res = await fetch("http://localhost:8000/generate/", {
    //   method: "POST",
    //   body: JSON.stringify({
    //     models: ["GPT3.5", "Bard", "Claude", "Test"],
    //     prompt:
    //       "You are a helpful assistant who solves math problems. Write the following equation using algebraic symbols then show the steps to solve the problem:",
    //     data: "x^3 + 7 = 12",
    //   }),
    //   headers: {
    //     "Content-type": "application/json; charset=UTF-8",
    //     'X-CSRFToken': csrftoken
    //   },
    // });

    // parse the returned json
  } catch (err) {
    console.log(err);
  }
  return;
};

export default useGenerate;
