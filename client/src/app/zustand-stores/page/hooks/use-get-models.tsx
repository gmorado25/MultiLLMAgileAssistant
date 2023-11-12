"use client";
import axios from "axios";
import { setModels } from "../store/LLM-store";
import { useEffect } from "react";
import { getCSRFHeader } from "@/app/utils/cookies";

// Custom hook with useEffect
const useGetModels = () => {

  const fetchData = async () => {
    try {
      const config = getCSRFHeader()
      const response = await axios.get("/models.json", config);
      setModels(response.data);
    } catch (err) {
      console.log(err);
    }
  };

  // Empty dependencies array ensures this effect runs once on mount
  useEffect(() => {fetchData();}, []);
};

export default useGetModels;
