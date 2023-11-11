import React from 'react'
import multiLLM from './page'

describe('<multiLLM />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-react
    cy.mount(<multiLLM />)
  })
})