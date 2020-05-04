// Author: Albert
// Created: 04-05-2020
// Updated: 04-05-2020
// note: placeholder for Joel's code


import React from 'react';
import styled from 'styled-components';
const GridWrapper = styled.div`
  display: grid;
  grid-gap: 10px;
  margin-top: 1em;
  margin-left: 6em;
  margin-right: 6em;
  grid-template-columns: repeat(12, 1fr);
  grid-auto-rows: minmax(25px, auto);
`; 
export const About = () => (
  <GridWrapper>
    <h2>About Page</h2>
    <p>PLACEHOLDER</p>
    <p>PLACEHOLDER</p>
    <p>PLACEHOLDER</p>
    <p>PLACEHOLDER</p>
    <p>PLACEHOLDER</p>
  </GridWrapper>
)
