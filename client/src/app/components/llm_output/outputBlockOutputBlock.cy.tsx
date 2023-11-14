import React from 'react'
import OutputBlock from './outputBlock'

describe('<OutputBlock />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-react
    cy.mount(<OutputBlock llm={'Unit Test'} output={'testing...'} />)
  })
})