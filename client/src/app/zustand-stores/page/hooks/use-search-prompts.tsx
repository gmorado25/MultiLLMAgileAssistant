"use client";
import axios from "axios";
import {setPrompts, useLLMStore} from "../store/LLM-store";
import { useEffect } from "react";
import { getJSONHeader } from "@/app/utils/cookies";

// Custom hook with useEffect
const useSearchPrompts = () => {
  const { phase, role, searchInput } = useLLMStore.use.promptSearch();

  useEffect(() => {
    // Initialize an array to hold query parts
    let queryParts = [];

    // Append the query parameters only if they are not empty
    if (phase) queryParts.push(`sdlc_phase=${encodeURIComponent(phase)}`);
    if (role) queryParts.push(`role=${encodeURIComponent(role)}`);
    if (searchInput)
      queryParts.push(`description=${encodeURIComponent(searchInput)}`);

    // Join the query parts using the '&' character
    const queryString = queryParts.join("&");

    const fetchData = () => {
      const config = getJSONHeader();
      axios.get(`/prompts/search/?${queryString}`, config).then(r => {
        setPrompts(r.data.prompts)
      }).catch(e => {
        console.log(e);
      })
    }

    if (phase || role || searchInput) {
      fetchData(); // Call the fetchData only if there is some search input
    }
  }, [phase, role, searchInput]);
};

export default useSearchPrompts;
