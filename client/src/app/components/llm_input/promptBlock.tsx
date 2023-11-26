"use client";
import React, { useState } from "react";
import Card from "@mui/joy/Card";

interface PromptBlock {
  title: string;
  output: string;
  sdlc_phase: string;
  role: string;
}

const PromptBlock: React.FC<
  PromptBlock & { isSelected: boolean; onSelect: () => void }
> = ({ title, output, sdlc_phase, role, isSelected, onSelect }) => {
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
      <Card
        data-testid={title}
        sx={{
          width: 300,
          height: 170,
          display: "flex", // Ensures the items inside are flex items, which can then be aligned properly
          flexDirection: "column", // Stacks children vertically
          justifyContent: "center", // Centers children along the vertical axis
          alignItems: "center", // Centers children along the horizontal axis
          backgroundColor: isSelected ? "lightblue" : "white",
          cursor: "pointer",
          padding: "16px", // Adds padding inside the card to prevent content from touching the edges
          boxSizing: "border-box", // Ensures padding does not add to the overall width or height of the element
          overflow: "hidden", // Prevents content from overflowing
          textOverflow: "ellipsis", // Adds an ellipsis to text that overflows
        }}
        onClick={onSelect}
      >
        <h1
          style={{
            margin: "0",
            overflow: "hidden",
            whiteSpace: "nowrap",
            textOverflow: "ellipsis",
          }}
        >
          {title}
        </h1>
        <p
          style={{ margin: "0", overflow: "hidden", textOverflow: "ellipsis" }}
        >
          {output}
        </p>
      </Card>
    </div>
  );
};

export default PromptBlock;
