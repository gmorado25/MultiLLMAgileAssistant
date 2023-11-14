"use client";
import React, { FC } from "react";
import { Divider, FormControl, MenuItem, Select } from "@mui/material";
import Button from "@mui/joy/Button";
import Textarea from "@mui/joy/Textarea";
import Option from "@mui/joy/Option";
import * as yup from "yup";
import PromptModal from "./prompt-modal";
import {
  setInputData,
  setSelectedModels,
} from "../../zustand-stores/page/store/LLM-store";
import useGenerate from "@/app/zustand-stores/page/hooks/use-generate";
import { Controller, useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import useGetModels from "@/app/zustand-stores/page/hooks/use-get-models";
import JiraConnect from "../jira/jira-connect-modal";

const names = ["ChatGPT", "Claude", "Llama", "Perplexity", "Test"];

type InputSearchFormSchema = {
  format?: string;
  modifier?: string;
  language?: string;
  models: string[];
};

const initialInputSearchFormValues: InputSearchFormSchema = {
  format: "",
  modifier: "",
  language: "",
  models: [],
};

const LLMSearchToolbar: FC = () => {
  // Lazy Loading
  useGetModels();

  const generate = useGenerate();

  const GENERATE_REQUEST_FORM_SCHEMA = yup.object().shape({
    format: yup.string().notRequired(),
    modifier: yup.string().notRequired(),
    language: yup.string().notRequired(),
    models: yup.array().of(yup.string()),
  });

  const { register, control, getValues } = useForm({
    mode: "onSubmit",
    resolver: yupResolver(GENERATE_REQUEST_FORM_SCHEMA),
    defaultValues: { ...initialInputSearchFormValues },
  });

  // Event handler using the generate function from the hook
  const handleSubmit = async () => {
    (await generate)();
  };

  return (
    <div className="w-full p-4">
      <form className="flex flex-col w-full pr-8 space-y-4 border-Primary rounded-lg xl:pr-0 py-4 ">
        <Divider></Divider>
        <div className="p-4">
          <div className="flex flex-row">
            <PromptModal />
            {/* <select
              className=" ml-4 mr-4"
              placeholder="Output Format"
              {...register("format")}
            >
              <option value="graph">Graph</option>
              <option value="table">Table</option>
              <option value="text">Text</option>
            </select>
            <select
              className="mr-4"
              placeholder="Output Modifier"
              {...register("modifier")}
            >
              <option value="dog">1</option>
              <option value="cat">2</option>
            </select>
            <select
              className="mr-4"
              placeholder="Coding Language"
              {...register("language")}
            >
              <option value="C++">C++</option>
              <option value="Go">Go</option>
              <option value="Java">Java</option>
              <option value="Javascript">Javascript</option>
              <option value="Python">Python</option>
            </select> */}
            <Controller
              name="models"
              control={control}
              render={({ field }) => (
                <FormControl sx={{ m: 1, width: 300 }}>
                  <Select
                    labelId="multiple-name-label"
                    id="multiple-name"
                    multiple
                    value={field.value}
                    onChange={(event) => {
                      // This will pass the selected values to React Hook Form's controller
                      const selected = event.target.value;
                      // Ensure only string[] is passed, even if empty
                      const validModels = Array.isArray(selected)
                        ? selected.filter(
                            (model): model is string =>
                              typeof model === "string"
                          )
                        : [];
                      // Update the selected models in the store
                      setSelectedModels(validModels);
                      // Update the form state
                      field.onChange(validModels);
                    }}
                    renderValue={(selected) => selected.join(", ")}
                  >
                    {names.map((name) => (
                      <MenuItem key={name} value={name}>
                        {name}
                      </MenuItem>
                    ))}
                  </Select>
                </FormControl>
              )}
            />
            <div className="flex justify-end items-end">
              <JiraConnect />
            </div>
          </div>

          <Textarea
            className="overflow-auto h-60"
            placeholder="Input text here..."
            onChange={(value) => {
              setInputData(value.target.value);
            }}
            data-testid="input-search_text-area" // Add this line
          ></Textarea>
          <div className="flex items-end justify-end py-4">
            <div className="px-4">
              <Button className="" disabled={false} variant="outlined" data-testid="input-search_clear-button">
                Clear
              </Button>
            </div>
            <Button
              // eslint-disable-next-line react-hooks/rules-of-hooks
              onClick={handleSubmit}
              className=""
              disabled={false}
              variant="solid"
              data-testid="input-search_submit-button"
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
