
describe('Dashboard Buttons Test', () => {
    beforeEach(() => {
      // Visit the dashboard page before each test
      cy.visit('http://127.0.0.1:8000/dashboard/');
    });
  
    it('should click on the "clear" button successfully', () => {
      // Locate and click the "clear" button
      cy.get('[data-testid="input-search_clear-button"]').click();
    });
  
    it('should click on the "submit" button successfully', () => {
      // Locate and click the "submit" button
      cy.get('[data-testid="input-search_submit-button"]').click();
    });
  
    it('should type and assert on the content of the textarea', () => {
      const inputText = 'Hello, Cypress!';
  
      // Type text into the Textarea
      cy.get('[data-testid="input-search_text-area"]').type(inputText);
      
      // TODO: check if the value matches with teh input

    });

    // Add more tests as needed
  });