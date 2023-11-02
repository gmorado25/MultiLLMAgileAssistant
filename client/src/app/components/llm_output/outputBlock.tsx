"use client";
import * as React from "react";
import Card from "@mui/joy/Card";
import Textarea from "@mui/joy/Textarea";
import Button from "@mui/joy/Button";
import "./styles.css"; // Import the CSS file
import Snackbar from "@mui/material/Snackbar";
import { jsPDF } from "jspdf";
import { CSVLink } from "react-csv";

interface OutputBlock {
  llm: string;
  output: string;
}

const OutputBlock: React.FC<OutputBlock> = ({ llm, output }) => {
  const [open, setOpen] = React.useState(false);

  const handleCopyClick = () => {
    navigator.clipboard.writeText(output);
    setOpen(true);
  };

  const handleExportClick = () => {
    const doc = new jsPDF();
    const maxWidth = doc.internal.pageSize.getWidth();
    const lines = doc.splitTextToSize(output, maxWidth);
    const multiLineText = `${llm}',s Output:\n\n` + lines.join("\n");
    doc.setFontSize(12); // Adjust the font size as needed
    doc.text(multiLineText, 10, 10);
    doc.save(`${llm}'s-output.pdf`);
  };

  const handleExportClick2 = () => {
    const data = `${output}`
    return <CSVLink data={data} filename={`${llm}'s-output.csv`} style={{ textDecoration: 'none', color: '#0b6bcb' }}>CSV</CSVLink>;
  };

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
    <div className="OutputBlock">
      <Card sx={{ width: 440, height: 500 }}>
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
        <div className="Buttons">
          <Button  variant="outlined" onClick={handleCopyClick}>
            Clipboard
          </Button>
          <div>
            <Button variant="outlined" onClick={handleExportClick}>
              PDF
            </Button>
            <Button variant="outlined">
              {handleExportClick2()}
            </Button>
          </div>
        </div>
        <Snackbar
          open={open}
          autoHideDuration={3000}
          onClose={handleClose}
          message={`${llm}'s output copied!`}
        />
      </Card>
    </div>
  );
};

export default OutputBlock;
