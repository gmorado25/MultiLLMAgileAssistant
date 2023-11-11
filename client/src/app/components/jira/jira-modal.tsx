"use client";
import * as React from "react";
import Button from "@mui/joy/Button";
import Stack from "@mui/joy/Stack";
import Modal from "@mui/joy/Modal";
import ModalClose from "@mui/joy/ModalClose";
import ModalDialog, { ModalDialogProps } from "@mui/joy/ModalDialog";
import DialogTitle from "@mui/joy/DialogTitle";
import DialogContent from "@mui/joy/DialogContent";
import { Divider, TextField } from "@mui/material";
import useGetPrompts from "@/app/zustand-stores/page/hooks/use-get-prompts";
import {useLLMStore} from "@/app/zustand-stores/page/store/LLM-store";
import JiraSearchBar from "./jira-issues-search_box";

export default function JiraModal() {
  //Lazy loading the hooks to get the prompts and place in zustand store for retrieval
  useGetPrompts();

  const [open, setOpen] = React.useState(false);
  const handleOpen = () => {
    setOpen(true);
  };
  const handleClose = () => {
    setOpen(false);
  };

  const promptData = useLLMStore.use.prompts();

  const [selectedPromptTitle, setSelectedPromptTitle] = React.useState<
    string | null
  >(null);

  const [layout, setLayout] = React.useState<
    ModalDialogProps["layout"] | undefined
  >(undefined);
  return (
    <div className="border border-spacing-20 border-blue-600">
      <React.Fragment>
        <div className="flex justify-center items-center">
          <Button
            variant="solid"
            color="primary"
            onClick={() => {
              setLayout("fullscreen");
            }}
          >
            Connect
          </Button>
        </div>
        <Modal open={!!layout} onClose={() => setLayout(undefined)}>
          <ModalDialog layout={layout}>
            <ModalClose />
            <DialogContent>
              <div className="flex flex-row w-full">
                <div className="flex w-1/6">
                  <div className="flex flex-col">
                    <JiraSearchBar/>
                  </div>
                </div>
                <Divider orientation="vertical" className="mx-4" />
                <div className="flex flex-col w-5/6">
                  <h1>Issue ID: Variable here </h1>
                  <div className="flex flex-col w-full">
                    <label htmlFor="">Summary</label>
                    <TextField
                      className="w-full"
                      label="Summary"
                      placeholder="Enter a summary for the issue"
                    />
                    <div className="flex justify-end items-end">
                      <button> Add to Input </button>
                      <button> Copy </button>
                    </div>
                  </div>
                  <div className="flex flex-col w-full">
                    <label htmlFor="">Description</label>
                    <TextField
                      className="w-full"
                      label="Description"
                      placeholder="Describe the issue"
                      multiline
                    />
                    <div className="flex justify-end items-end">
                      <button> Add to Input </button>
                      <button> Copy </button>
                    </div>
                  </div>
                  <div className="flex flex-col w-full">
                    <label htmlFor="">Acceptance Criteria</label>
                    <TextField
                      className="w-full"
                      label="Acceptance Criteria"
                      placeholder="Define the acceptance criteria"
                      multiline
                    />
                    <div className="flex justify-end items-end">
                      <button> Add to Input </button>
                      <button> Copy </button>
                    </div>
                  </div>
                </div>
              </div>

              <Divider />
            </DialogContent>
          </ModalDialog>
        </Modal>
      </React.Fragment>
    </div>
  );
}
