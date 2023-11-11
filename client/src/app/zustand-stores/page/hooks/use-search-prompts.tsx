"use client";
import axios from "axios";
import {setPrompts, useLLMStore} from "../store/LLM-store";
import { useEffect } from "react";
import { getCookie } from "@/app/utils/cookies";

// Custom hook with useEffect
const useSearchPrompts = () => {
  const { phase, role, searchInput } = useLLMStore.use.promptSearch();

  // Initialize an array to hold query parts
  let queryParts = [];

  // Append the query parameters only if they are not empty
  if (phase) queryParts.push(`sdlc_phase=${encodeURIComponent(phase)}`);
  if (role) queryParts.push(`role=${encodeURIComponent(role)}`);
  if (searchInput)
    queryParts.push(`description=${encodeURIComponent(searchInput)}`);

  // Join the query parts using the '&' character
  const queryString = queryParts.join("&");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const csrftoken = getCookie("csrftoken");

        const apiClient = axios.create({
          baseURL: "http://127.0.0.1:8000/",
          headers: {
            "content-type": "application/json",
            "X-CSRFToken": csrftoken,
          },
        });

        // Make the GET request using the constructed query string
        const response = await apiClient.get(`prompts/search/?${queryString}`);

        const data = response.data.prompts;

        setPrompts(data);
      } catch (err) {
        console.log(err);
      }
    };

    if (phase || role || searchInput) {
      fetchData(); // Call the fetchData only if there is some search input
    }
  }, [phase, role, searchInput]);
};

export default useSearchPrompts;
