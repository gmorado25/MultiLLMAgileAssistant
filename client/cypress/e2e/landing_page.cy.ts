describe('MultiLLM Button Test', () => {
    it('should click on the MultiLLM button successfully', () => {
      // Visit the specified URL
      cy.visit('http://127.0.0.1:8000/');
  
      // Assert that the page contains a button with the text "MultiLLM"
      cy.contains('MultiLLM').should('exist');
  
      // Click on the MultiLLM button
      cy.contains('MultiLLM').click();
  
      // Assert that the expected action has occurred after clicking the button
      // For example, you might want to check for a specific change on the page
      // or navigate to a new page.
      cy.url().should('include', '/dashboard'); // Adjust the URL accordingly


    // Go back to the previous page (assuming the logo is a link to the home page)
    cy.go('back');

    // Assert that the logo is present and clickable
    // cy.get('[data-testid="argo-logo-image"]').click();

    // Assert that the expected action has occurred after clicking the logo
    // For example, you might want to check for a navigation or a new window being opened.
    // cy.url().should('eq', 'https://https://argodata.com/'); // Adjust the expected URL accordingly
    });
  });