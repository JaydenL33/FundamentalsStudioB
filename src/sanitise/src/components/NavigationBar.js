// Author: Albert
// Created: 04-05-2020
// Updated: 04-05-2020
// note: adds new components and "templating" REACT style to app

import React from 'react';
import { Nav, Navbar, Form, FormControl } from 'react-bootstrap';
import styled from 'styled-components';
import { NavLink } from 'react-router-dom';

// Albert: styles definition for Navbar hover, branding, spannig and general
// note: use spacing and flex utilities to size and position content
// https://react-bootstrap.github.io/components/navbar/
const Styles = styled.div`
  .navbar { background-color: #101010; }
  a, .navbar-nav, .navbar-light .nav-link {
    font-size: 1.2em;
    color: #FFFFFF;
    &:hover { color: #1D7CFF; }
  }
  .navbar-brand {
    font-size: 2.2em;
    color: #FFFFFF;
    &:hover { color: #EF1C45; }
    padding-left: 2em;
  }

  .vl {
    content: "";
    background-color: #FFFFFF;
    width: 2px;
    height: 1.5em;
    margin-right: 3em;
    margin-left: 1.5em;
    display: inline-block;
    vertical-align: middle;
  }
`;

// The navbar component, takes the style and creates a dynamic "object" for UX
export const NavigationBar = () => (
  <Styles>
    <Navbar expand="lg" sticky="top">
      <Navbar.Brand href="/">SANITISE.MEDIA</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav"/>
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mx-auto">
            <Nav.Item>
                <Nav.Link href="/Indicators"><div class="vl"/>Indicators</Nav.Link>
            </Nav.Item>

            <Nav.Item>
                <Nav.Link href="/Story"><div class="vl"/>Story</Nav.Link>
            </Nav.Item>
            
            <Nav.Item>
                <Nav.Link href="/AboutUs"><div class="vl"/>About Us</Nav.Link>
            </Nav.Item>
            
            <Nav.Item>
                <Nav.Link href="/ContactUs"><div class="vl"/>Contact Us</Nav.Link>
            </Nav.Item>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  </Styles>
)
