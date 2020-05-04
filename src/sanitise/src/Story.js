// Author: Albert
// Created: 04-05-2020
// Updated: 04-05-2020
// note: story is the home or landing page

import React from 'react';
import styled from 'styled-components';

const GridWrapper = styled.div`
  display: grid;
  float: right;
  grid-gap: 10px;
  margin-top: 1em;
  margin-left: 6em;
  margin-right: 6em;
  grid-template-columns: minmax(25px, auto);;
  grid-auto-rows: repeat(5, 1fr)
`;

export const Story = (props) => (
  <GridWrapper>
    <p>SANITISE MEDIA @ UTS</p>
    <p>Virus Visualising Media</p>
    <p>Scroll to visualise the pandemic scenario...</p>
    <p>3,132,363</p>
    <p>TOTAL CONFIRMED CASES</p>
  </GridWrapper>
)
