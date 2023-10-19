"use client";
import * as React from 'react';
import Card from '@mui/joy/Card';
import Textarea from '@mui/joy/Textarea';
import Button from '@mui/joy/Button';
import './styles.css'; // Import the CSS file
import Snackbar from '@mui/material/Snackbar';

interface OutputBlock {
    llm: string
    output: string;
  }

const OutputBlock: React.FC<OutputBlock> = ({ llm, output }) => {
    const [open, setOpen] = React.useState(false);

    const handleCopyClick = () => {
      navigator.clipboard.writeText(output)
      setOpen(true);
    }
    
    const handleClose = (event: React.SyntheticEvent | Event, reason?: string) => {
      if (reason === 'clickaway') {
        return;
      }
  
      setOpen(false);
    };

    return (
      <div className="OutputBlock">
        <Card sx={{ width: 440, height:500 }}>
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
              <Button variant="outlined" onClick={handleCopyClick}>
                Copy
              </Button>
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