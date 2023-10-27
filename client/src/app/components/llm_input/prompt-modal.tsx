"use client";
import * as React from "react";
import Button from "@mui/joy/Button";
import Stack from "@mui/joy/Stack";
import Modal from "@mui/joy/Modal";
import ModalClose from "@mui/joy/ModalClose";
import ModalDialog, { ModalDialogProps } from "@mui/joy/ModalDialog";
import DialogTitle from "@mui/joy/DialogTitle";
import DialogContent from "@mui/joy/DialogContent";
import Select from "@mui/joy/Select";
import Option from "@mui/joy/Option";
import { Divider } from "@mui/material";
import { Input } from "@mui/joy";
import SearchIcon from "@mui/icons-material/Search";
import PromptBlock from "./promptBlock";
import useGetPrompts from "@/app/zustand-stores/page/hooks/use-get-prompts";

export default function LayoutModalDialog() {
  //Lazy loading the hooks to get the prompts and place in zustand store for retrieval
  useGetPrompts();

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
            <div className="flex justify-between">
              <div className="flex">
                <Select className="m-4" placeholder="Role">
                  <Option value="Develoepr">Developer</Option>
                  <Option value="Manager">Manager</Option>
                  <Option value="Tester">Tester</Option>
                  <Option value="QA">QA</Option>
                </Select>
                <Select className="m-4" placeholder="SDLC">
                  <Option value="Analysis">Analysis</Option>
                  <Option value="Design">Design</Option>
                  <Option value="Implementation">Implementation</Option>
                  <Option value="Maintenance">Maintenance</Option>
                  <Option value="Planning">Planning</Option>
                  <Option value="Testing">Testing</Option>
                </Select>
              </div>
              <div>
                <Input startDecorator={<SearchIcon />} placeholder="Search" />
              </div>
            </div>
            <Divider />
            <div className="flex flex-row max-h-60 m-4 justify-between">
              <PromptBlock llm={"card 1"} output={"test"} />
              <PromptBlock llm={"card 2"} output={"test"} />
              <PromptBlock llm={"card 3"} output={"test"} />
              <PromptBlock llm={"card 4"} output={"test"} />
            </div>
            <div className="flex flex-row max-h-60 m-4 justify-between">
              <PromptBlock llm={"card 5"} output={"test"} />
              <PromptBlock llm={"card 6"} output={"test"} />
              <PromptBlock llm={"card 7"} output={"test"} />
              <PromptBlock llm={"card 8"} output={"test"} />
            </div>
            <Divider />
            <div className=" flex justify-end">
              <Button>Save</Button>
            </div>
          </DialogContent>
        </ModalDialog>
      </Modal>
    </React.Fragment>
  );
}
