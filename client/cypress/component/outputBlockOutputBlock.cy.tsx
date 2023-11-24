import React from "react";
import OutputBlock from "../../src/app/components/llm_output/outputBlock";

describe("<OutputBlock />", () => {
  it("renders", () => {
    // see: https://on.cypress.io/mounting-react
    cy.mount(<OutputBlock llm={"Unit Test"} output={"testing..."} />);
  });
});
