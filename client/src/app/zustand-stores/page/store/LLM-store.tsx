import { create } from "zustand";
import { createSelectors } from "@/app/utils/zustand-utils";

export function getCookie(name: string) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

type PromptType = {
  title: string;
  description: string;
  sdlc_phase: string;
  role: string;
};

type InputPromptSearch = {
  role: string;
  phase: string;
  searchInput: string;
};

type OutputType = { model: string; response: string };

export type LLMStoreProps = {
  prompts: PromptType[];
  models: String[];
  selectedModels: String[];
  inputData: string;
  outputData: OutputType[];
  selectedPrompt: PromptType;
  promptSearch: InputPromptSearch;
  isGeneratedLoading: boolean;
};

const initialState: LLMStoreProps = {
  prompts: [],
  models: [],
  selectedModels: [],
  inputData: "",
  outputData: [],
  selectedPrompt: { title: "", description: "", sdlc_phase: "", role: "" },
  promptSearch: { role: "", phase: "", searchInput: "" },
  isGeneratedLoading: false,
};

export const resetLLMStore = (): void =>
  useLLMStore.setState(() => ({ ...initialState }));

export const setPrompts = (prompts: PromptType[]): void =>
  useLLMStore.setState(() => ({ prompts }));

export const setModels = (models: String[]): void =>
  useLLMStore.setState(() => ({ models }));

export const setSelectedModels = (selectedModels: String[]): void =>
  useLLMStore.setState(() => ({ selectedModels }));

export const setInputData = (inputData: string): void =>
  useLLMStore.setState(() => ({ inputData }));

export const setOutputData = (outputData: OutputType[]): void =>
  useLLMStore.setState(() => ({ outputData }));

export const setSelectedPrompt = (selectedPrompt: PromptType): void =>
  useLLMStore.setState(() => ({ selectedPrompt }));

export const setPromptSearch = (promptSearch: InputPromptSearch): void =>
  useLLMStore.setState(() => ({ promptSearch }));

export const setIsGeneratedLoading = (isGeneratedLoading: boolean): void =>
  useLLMStore.setState(() => ({ isGeneratedLoading }));

const useLLMStoreBase = create<LLMStoreProps>()(() => ({
  ...initialState,
}));

export const useLLMStore = createSelectors(useLLMStoreBase);
