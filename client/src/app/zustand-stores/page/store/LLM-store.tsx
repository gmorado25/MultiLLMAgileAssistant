import { create } from "zustand";
import { createSelectors } from "@/app/utils/zustand-utils";

type PromptType = {
  Title: string;
  description: string;
  sdlc_phase: string;
  role: string;
};

type OutputType = { model: string; response: string };

export type LLMStoreProps = {
  prompts: PromptType[];
  inputData: string;
  outputData: OutputType[];
};

const initialState: LLMStoreProps = {
  prompts: [],
  inputData: "",
  outputData: [],
};

export const resetLLMStore = (): void =>
  useLLMStore.setState(() => ({ ...initialState }));

export const setPrompts = (prompts: PromptType[]): void =>
  useLLMStore.setState(() => ({ prompts }));

export const setInputData = (inputData: string): void =>
  useLLMStore.setState(() => ({ inputData }));

export const setOutputData = (outputData: OutputType[]): void =>
  useLLMStore.setState(() => ({ outputData }));

const useLLMStoreBase = create<LLMStoreProps>()(() => ({
  ...initialState,
}));

export const useLLMStore = createSelectors(useLLMStoreBase);
