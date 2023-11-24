"use client";
import React, { FC } from "react";
import { Controller, useForm } from "react-hook-form";

import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";

import { Divider, FormControl } from "@mui/material";
import Button from "@mui/joy/Button";
import Textarea from "@mui/joy/Textarea";

import PromptModal from "./prompt-modal";
import JiraConnect from "../jira/jira-connect-modal";
import AsyncSelector from "./async-selector";
import OptionDisplay from "./option-display";

import {
  setSelectedFormat,
  setInputData,
  setSelectedModels,
  useLLMStore,
} from "../../zustand-stores/page/store/LLM-store";
import useGenerate from "@/app/zustand-stores/page/hooks/use-generate";
import useFormat from "@/app/zustand-stores/page/hooks/use-format";

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
  const generate = useGenerate();

  const GENERATE_REQUEST_FORM_SCHEMA = yup.object().shape({
    format: yup.string().notRequired(),
    modifier: yup.string().notRequired(),
    language: yup.string().notRequired(),
    models: yup.array().of(yup.string()),
  });

  const { control } = useForm({
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
              callback={(value) => {
                setSelectedFormat(value);
              }}
            />
            <Controller
              name="models"
              control={control}
              render={({ field }) => (
                <FormControl data-testid="selector">
                  <AsyncSelector
                    value={field.value}
                    url="/models.json"
                    placeholder="Select one or more LLMs"
                    required
                    callback={(selected) => {
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
                    multiple
                    renderValue={(selected) => selected.join(", ")}
                  />
                </FormControl>
              )}
            />
            <div className="flex justify-end items-end">
              <JiraConnect />
            </div>
          </div>
          <OptionDisplay
            heading="Prompt"
            hook={() => useLLMStore.use.selectedPrompt().description}
          />
          <OptionDisplay heading="Modify the output" hook={useFormat} />
          <Divider></Divider>
          <h4>Enter your data:</h4>
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
              <Button
                className=""
                disabled={false}
                variant="outlined"
                data-testid="input-search_clear-button"
              >
                Clear
              </Button>
            </div>
            <Button
              // eslint-disable-next-line react-hooks/rules-of-hooks

              onClick={handleSubmit}
              className=""
              disabled={useLLMStore.use.isGeneratedLoading()}
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
