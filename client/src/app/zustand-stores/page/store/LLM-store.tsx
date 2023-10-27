import { create } from "zustand";
import { createSelectors } from "@/app/utils/zustand-utils";

type PromptType = {
  Title: string;
  description: string;
  sdlc_phase: string;
  role: string;
};

export type LLMStoreProps = {
  prompts: PromptType[];
};

const initialState: LLMStoreProps = { prompts: [] };

export const resetLLMStore = (): void =>
  useLLMStore.setState(() => ({ ...initialState }));

export const setPrompts = (prompts: PromptType[]): void =>
  useLLMStore.setState(() => ({ prompts }));

const useLLMStoreBase = create<LLMStoreProps>()(() => ({
  ...initialState,
}));

export const useLLMStore = createSelectors(useLLMStoreBase);
