"use client";
import axios from "axios";
import { setPrompts, setModels, getCookie } from "../store/LLM-store";
import { useEffect } from "react";

// Custom hook with useEffect
const useGetModels = () => {
  useEffect(() => {
    const fetchData = async () => {
      try {
        const csrftoken = getCookie("csrftoken");
        const config = {
          headers: {
            "content-type": "application/json",
            "X-CSRFToken": csrftoken,
          },
        };
        const response = await axios.get("/models", config);
        const data = response.data;
        setModels(data);
      } catch (err) {
        console.log(err);
      }
    };

    fetchData();
  }, []); // Empty dependencies array ensures this effect runs once on mount
};

export default useGetModels;
