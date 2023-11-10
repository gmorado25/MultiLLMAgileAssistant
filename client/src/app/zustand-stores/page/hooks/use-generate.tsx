"use client";
import * as React from "react";
import {
  setOutputData,
  getCookie,
  useLLMStore,
  setIsGeneratedLoading,
} from "../store/LLM-store";
import { setPrompts } from "../store/LLM-store";
const axios = require("axios").default;

const useGenerate = async () => {
  const prompt = useLLMStore.use.selectedPrompt();
  const data = useLLMStore.use.inputData();
  const models = useLLMStore.use.selectedModels();

  const generate = () => {
    try {
      setIsGeneratedLoading(true);
      const csrftoken = getCookie("csrftoken");

      const body = JSON.stringify({
        models: models,
        prompt: prompt.description,
        data: data,
      });

      // make an API call the the /generate endpoint, pass in the prompts, list of models to query, etc.
      const config = {
        headers: {
          "content-type": "application/json",
          "X-CSRFToken": csrftoken,
        },
      };
      axios.post("/generate.json", body, config).then((response: any) => {
        const data = response.data;

        setOutputData(data);
        setIsGeneratedLoading(false);
      });
    } catch (err) {
      console.log(err);
    }
  };
  return generate;
};

export default useGenerate;
