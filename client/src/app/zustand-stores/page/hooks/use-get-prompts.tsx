"use client";
import axios from "axios";
import { setPrompts } from "../store/LLM-store";
import { getCSRFHeader } from "../../../utils/cookies"

const useGetPrompts = async () => {
  try {
    axios.get("/prompts.json", getCSRFHeader()).then((response: any) => {
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
