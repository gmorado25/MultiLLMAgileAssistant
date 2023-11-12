"use client";
import React, { FC } from "react";
import { Controller, useForm } from "react-hook-form";

import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";

import { Divider, FormControl, MenuItem, Select } from "@mui/material";
import Button from "@mui/joy/Button";
import Textarea from "@mui/joy/Textarea";

import PromptModal from "./prompt-modal";
import JiraConnect from "../jira/jira-connect-modal";
import AsyncSelector from "./async-selector";
import FormatDisplay from "./format-display";

import {
  setFormat,
  setInputData,
  setSelectedModels,
} from "../../zustand-stores/page/store/LLM-store";
import useGenerate from "@/app/zustand-stores/page/hooks/use-generate";
import useGetModels from "@/app/zustand-stores/page/hooks/use-get-models";

const names = ["GPT3.5", "Bard", "Llama", "Test"];

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
            <AsyncSelector 
              url="/formats.json" 
              placeholder="Select Format" 
              onChange={(value) => {
                setFormat(value);
              }} 
            />
            {/* <Controller
              name="models"
              control={control}
              render={({ field }) => (
                <FormControl sx={{ m: 1, width: 300 }}>
                  <Select
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
            /> */}
            <div className="flex justify-end items-end">
              <JiraConnect />
            </div>
          </div>
          <FormatDisplay />
          <Textarea
            className="overflow-auto h-60"
            placeholder="Input text here..."
            onChange={(value) => {
              setInputData(value.target.value);
            }}
          ></Textarea>
          <div className="flex items-end justify-end py-4">
            <div className="px-4">
              <Button className="" disabled={false} variant="outlined">
                Clear
              </Button>
            </div>
            <Button
              // eslint-disable-next-line react-hooks/rules-of-hooks
              onClick={handleSubmit}
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
