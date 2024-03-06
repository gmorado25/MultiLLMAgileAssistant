"use client";
import Image from "next/image";
import { NextPage } from "next";
import { Footer } from "../components/layouts/footer";
import Link from "next/link";
import OutputBlock from "../components/llm_output/outputBlock";
import LlmInputSearchToolbar from "../components/llm_input/llm-input-search-toolbar";
import { useLLMStore } from "../zustand-stores/page/store/LLM-store";
import {Dashboard} from './../components/dashboard/DashboardNew';

const multiLLM: NextPage = () => {
  return (
    <Dashboard/>
  );
};

export default multiLLM;
