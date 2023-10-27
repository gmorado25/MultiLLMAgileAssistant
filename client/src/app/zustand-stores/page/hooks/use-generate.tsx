"use client";
import * as React from "react";
import Button from "@mui/joy/Button";
import "./styles.css"; // Import the CSS file

class TestButton extends React.Component {
  fetchLLMOutput = async () => {
    try {
      // make an API call the the /generate endpoint, pass in the prompts, list of models to query, etc.
      const res = await fetch("http://localhost:8000/generate/", {
        method: "GET",
        body: JSON.stringify({
          models: ["GPT3.5", "Bard", "Claude", "Test"],
          prompt:
            "You are a helpful assistant who solves math problems. Write the following equation using algebraic symbols then show the steps to solve the problem:",
          data: "x^3 + 7 = 12",
        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8",
        },
      });

      // parse the returned json
      const data = await res.json();
      console.log(data);

      // we have the output queried from the server in the variable "data", now insert output 'cards'
      // for each response returned. (idk how to create those react components and add them dynamically)
      for (let i = 0; i < data.length; i++) {
        let linebreak = document.createElement("br");
        document
          .getElementsByClassName("Outputs")[0]
          .append(
            data[i].model,
            linebreak,
            data[i].response,
            linebreak,
            linebreak
          );
      }
    } catch (err) {
      console.log(err);
    }
  };

  render() {
    return <Button variant="outlined" onClick={this.fetchLLMOutput}></Button>;
  }
}

export default TestButton;
