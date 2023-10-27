"use client";
import React, { useState } from "react";
import Card from "@mui/joy/Card";
import Textarea from "@mui/joy/Textarea";
import Button from "@mui/joy/Button";
import Snackbar from "@mui/material/Snackbar";

interface PromptBlock {
  llm: string;
  output: string;
}

const PromptBlock: React.FC<PromptBlock> = ({ llm, output }) => {
  const [open, setOpen] = useState(false);

  const handleClose = (
    event: React.SyntheticEvent | Event,
    reason?: string
  ) => {
    if (reason === "clickaway") {
      return;
    }

    setOpen(false);
  };

  return (
    <div className="PromptBlock">
      <Card sx={{ width: 300, height: 150 }}>
        <h1>{llm}</h1>
        <Textarea
          color="neutral"
          minRows={15}
          size="lg"
          variant="soft"
          maxRows={10}
          value={output}
          sx={{
            height: 380,
          }}
        />
      </Card>
    </div>
  );
};

export default PromptBlock;
