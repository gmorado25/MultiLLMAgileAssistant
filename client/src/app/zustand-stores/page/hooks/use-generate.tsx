"use client";
import axios from "axios";
import { setOutputData, setPrompts } from "../store/LLM-store";
import { getCSRFHeader } from "../../../utils/cookies"

const useGenerate = async () => {
  try {

    const body = JSON.stringify({
      models: ["GPT3.5", "Bard", "Claude", "Test"],
      prompt:
        "You are a helpful assistant who solves math problems. Write the following equation using algebraic symbols then show the steps to solve the problem:",
      data: "x^3 + 7 = 12",
    })

    // make an API call the the /generate endpoint, pass in the prompts, list of models to query, etc.
    axios.post("/generate.json", body, getCSRFHeader()).then((response: any) => {
      const data = response.data;
      console.log(response)
      setOutputData(data);
    });

  } catch (err) {
    console.log(err);
  }
  return;
};

export default useGenerate;
