"use client";
import React, { FC } from "react";
import { Divider } from "@mui/material";
import Button from "@mui/joy/Button";
import Textarea from "@mui/joy/Textarea";
import Select from "@mui/joy/Select";
import Option from "@mui/joy/Option";

import PromptModal from "./prompt-modal";

import {
  setOutputData,
  useLLMStore,
} from "../../zustand-stores/page/store/LLM-store";
import UseGenerate from "@/app/zustand-stores/page/hooks/use-generate";
import useGenerate from "@/app/zustand-stores/page/hooks/use-generate";

const LLMSearchToolbar: FC = () => {
  return (
    <div className="w-full p-4">
      <form className="flex flex-col w-full pr-8 space-y-4 border-Primary rounded-lg xl:pr-0 py-4 ">
        <Divider></Divider>
        <div className="p-4">
          <div className="flex flex-row">
            <PromptModal />
            <Select className=" ml-4 mr-4" placeholder="Output Format">
              <Option value="graph">Graph</Option>
              <Option value="table">Table</Option>
              <Option value="text">Text</Option>
            </Select>
            <Select className="mr-4" placeholder="Output Modifier">
              <Option value="dog">1</Option>
              <Option value="cat">2</Option>
            </Select>
            <Select className="mr-4" placeholder="Coding Language">
              <Option value="C++">C++</Option>
              <Option value="Go">Go</Option>
              <Option value="Java">Java</Option>
              <Option value="Javascript">Javascript</Option>
              <Option value="Python">Python</Option>
            </Select>
            <Select className="mr-4" placeholder="Select up to 3 LLM's">
              <Option value="bard">Bard</Option>
              <Option value="chatGpt">ChatGPT</Option>
              <Option value="claude">Claude</Option>
              <Option value="java">Llama</Option>
              <Option value="perplexity">Perplexity</Option>
            </Select>
          </div>

          <Textarea
            className="overflow-auto h-60"
            placeholder="Input text here..."
          ></Textarea>
          <div className="flex items-end justify-end py-4">
            <div className="px-4">
              <Button className="" disabled={false} variant="outlined">
                Clear
              </Button>
            </div>
            <Button
              // eslint-disable-next-line react-hooks/rules-of-hooks
              onClick={() => useGenerate()}
              className=""
              disabled={false}
              variant="solid"
            >
              Submit
            </Button>
          </div>
        </div>
      </form>
    </div>
  );
};

export default LLMSearchToolbar;
