// Author: Albert
// Created: 04-05-2020
// Updated: 04-05-2020
// note: If no page could be found to switch, essentially 404 lander

import React from 'react';
import styled from 'styled-components';
const Wrapper = styled.div`
  margin-top: 1em;
  margin-left: 6em;
  margin-right: 6em;
`;
export const NoMatch = () => (
  <Wrapper>
    <h2>No Match! 404</h2>
  </Wrapper>
)
