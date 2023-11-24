import React from "react";
import PromptBlock from "../../src/app/components/llm_input/promptBlock";

describe("<PromptBlock />", () => {
  it("renders", () => {
    // see: https://on.cypress.io/mounting-react
    cy.mount(
      <PromptBlock
        title={"Cypress test"}
        output={"Cypress testing description"}
        sdlc_phase={"test"}
        role={"tester"}
        isSelected={false}
        onSelect={function (): void {
          throw new Error("Function not implemented.");
        }}
      />
    );
  });
});
