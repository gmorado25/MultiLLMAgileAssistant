"use client";
import axios from "axios";
import { setPrompts } from "../store/LLM-store";
import { useEffect } from "react";
import { getJSONHeader } from "@/app/utils/cookies";

// Custom hook with useEffect
const useGetPrompts = () => {
  useEffect(() => {
    const fetchData = async () => {
      try {
        const config = getJSONHeader()
        const response = await axios.get("/prompts.json", config);
        setPrompts(response.data);
      } catch (err) {
        console.log(err);
      }
    };

    fetchData();
  }, []); // Empty dependencies array ensures this effect runs once on mount
};

export default useGetPrompts;
