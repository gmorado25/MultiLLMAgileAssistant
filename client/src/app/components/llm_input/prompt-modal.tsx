"use client";
import * as React from "react";
import Button from "@mui/joy/Button";
import Stack from "@mui/joy/Stack";
import Modal from "@mui/joy/Modal";
import ModalClose from "@mui/joy/ModalClose";
import ModalDialog, { ModalDialogProps } from "@mui/joy/ModalDialog";
import DialogTitle from "@mui/joy/DialogTitle";
import DialogContent from "@mui/joy/DialogContent";
import { Divider } from "@mui/material";
import PromptBlock from "./promptBlock";
import useGetPrompts from "@/app/zustand-stores/page/hooks/use-get-prompts";
import {
  setInputData,
  setSelectedPrompt,
  useLLMStore,
} from "@/app/zustand-stores/page/store/LLM-store";
import PromptSearchToolbar from "@/app/components/llm_input/prompt-search-toolbar";

export default function LayoutModalDialog() {
  //Lazy loading the hooks to get the prompts and place in zustand store for retrieval
  useGetPrompts();

  const promptData = useLLMStore.use.prompts();

  const [selectedPromptTitle, setSelectedPromptTitle] = React.useState<
    string | null
  >(null);

  const [layout, setLayout] = React.useState<
    ModalDialogProps["layout"] | undefined
  >(undefined);
  return (
    <React.Fragment>
      <Stack direction="row" spacing={1}>
        <Button
          variant="solid"
          color="primary"
          onClick={() => {
            setLayout("fullscreen");
          }}
        >
          Select Prompt
        </Button>
      </Stack>
      <Modal open={!!layout} onClose={() => setLayout(undefined)}>
        <ModalDialog layout={layout}>
          <ModalClose />
          <DialogTitle>Select Prompt</DialogTitle>
          <DialogContent>
            <PromptSearchToolbar />
            <Divider />
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 overflow-y-auto max-h-[60vh] m-4 justify-start">
              {promptData.map(({ title, description, sdlc_phase, role }) => (
                <PromptBlock
                  key={title}
                  title={title}
                  output={description}
                  sdlc_phase={sdlc_phase}
                  role={role}
                  isSelected={selectedPromptTitle === title}
                  onSelect={() => setSelectedPromptTitle(title)}
                ></PromptBlock>
              ))}
            </div>
            <Divider />
            <div className="flex justify-end">
              <Button
                onClick={() => {
                  if (selectedPromptTitle) {
                    const selectedPrompt = promptData.find(
                      (prompt) => prompt.title === selectedPromptTitle
                    );
                    if (selectedPrompt) {
                      setSelectedPrompt(selectedPrompt);
                    }
                  }
                  setLayout(undefined);
                }}
              >
                Save
              </Button>
            </div>
          </DialogContent>
        </ModalDialog>
      </Modal>
    </React.Fragment>
  );
}
