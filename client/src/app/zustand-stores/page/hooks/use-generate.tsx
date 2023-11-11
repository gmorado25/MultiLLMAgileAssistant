"use client";
import {
  setOutputData,
  useLLMStore,
  setIsGeneratedLoading,
} from "../store/LLM-store";
import { getCSRFHeader } from "@/app/utils/cookies";

const axios = require("axios").default;

const useGenerate = async () => {
  const prompt = useLLMStore.use.selectedPrompt();
  const data = useLLMStore.use.inputData();
  const models = useLLMStore.use.selectedModels();

  const generate = () => {
    try {
      setIsGeneratedLoading(true);
      const body = JSON.stringify({
        models: models,
        prompt: prompt.description,
        data: data,
      });

      // make an API call the the /generate endpoint, pass in the prompts, list of models to query, etc.
      const config = getCSRFHeader()
      axios.post("/generate.json", body, config).then((response: any) => {
        setOutputData(response.data);
        setIsGeneratedLoading(false);
      });
    } catch (err) {
      console.log(err);
    }
  };
  return generate;
};

export default useGenerate;

