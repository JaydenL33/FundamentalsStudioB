// Author: Joel Morrision
// Re-factored by Jayden Lee
// Date: 18/05/2020

import React, { Component } from 'react';

//React Reveal imports
import Zoom from 'react-reveal/Zoom';
import Fade from 'react-reveal/Fade';
import Slide from 'react-reveal/Slide';
import Reveal from 'react-reveal/Reveal';
import makeCarousel from 'react-reveal/makeCarousel';
//styled components
import styled, { css } from 'styled-components';
import './AboutUs.css';
//Card Design 
import { Card } from '../components/card';
import Navbar from '../components/navbar';
//Images
import UtsCrest from '../images/UtsCrest.jpg'
import B11 from '../images/building11.png'


const width = '500px', height='250px';
// Styled Components Syntax
const Container = styled.div`  
  border: rgba(0,0,0, 0.5);
  position: relative;
  overflow: hidden;
  width: ${width};
  height: ${height};
  left:15%;
  right:15%;
`;
// Styled Components Syntax
const Arrow = styled.div `
  text-shadow: 1px 1px 1px #fff;
  z-index: 100;
  line-height: ${height};
  text-align: center;
  position: absolute;
  width: 10%;
  font-size: 3em;
  cursor: pointer;
  user-select: none;
  ${props => props.right ? css`left: 90%;` : css`left: 0%;`}
`;

//Carousel UI
const CarouselUI = ({ position, handleClick, children }) => (
  <Container>
      {children}
      <Arrow onClick={handleClick} data-position={position - 1}>{'<'}</Arrow>
      <Arrow right onClick={handleClick} data-position={position + 1}>{'>'}</Arrow>
  </Container>
);
const Carousel = makeCarousel(CarouselUI);

 
function Title() {
  return (
    <div className = "title">
         <Fade>
          <h1>About Us</h1>
        </Fade>
        <br></br>
        <Fade up>
            <img src={UtsCrest} alt="Uts Crest" height={620}/>
            
        </Fade>

      </div>
      
  );
}

function ParagraphOne() {
  return (
    <div className = "textStyle">

        <Zoom>
          <h3>About Us!</h3>
          <h2> Covid-19 Visualisation - Purpose</h2>
          <br></br>
        </Zoom>

        <Reveal ssrFadein>
          <p>
          The purpose behind this web application is to compare and visualises complex and dynamic data of the SARS-COV-2 
          (a.k.a. COVID or Coronavirus) outbreak promptly. The aim of the website is to hopefully effectively deliver and 
          convey this data in an easily understandable format.
          </p>
        </Reveal>

    </div>
      
  );
}

function ParagraphTwo() {
  return (
    <div className = "textStyle">
          <Zoom>
            <h2> What is This? </h2>
          </Zoom>
        
          <br></br>
          <Reveal ssrFadein>
            <p>
              
            This website application has been created by four university students, with the aim to not only educate
            those who view the site, but also provide an opportunity for mention students to develop the skills needed in 
            order be able to present important and current data in an effective and rememberable way as studying data engineers.

         	  </p>
          </Reveal>

        <br></br>
     
        <img src={B11} alt="Uts Building 11" height={420} />
     

        
    </div>
      
  );
}


function ParagraphThree() {
  return (
    <div className = "textStyle">
      <Zoom>
        <h2>The Problem at Hand?</h2>
      </Zoom>
      <br></br>

      <Reveal ssrFadein>
        <p>
        The inspiration behind why this site has been developed was as the world is currently in the age of 
        information there is a widespread problem of the publishing misinformation as seen currently in the 
        non-factual spread of ‘rumours’ on the origins and effects of COVID-19 with conspiring theorist are running 
        rampant with ideas that SARS-CoV-2 may be a US Government bioterrorism plan or was created in a Biosecurity Lab 
        in Wuhan or was a result of 5G network towers. 
        </p>
      </Reveal>


       
    </div>
      
  );
}

function ParagraphFour() {
  return (
    <div className = "textStyle">
      <Zoom>
        <h2> How are we addressing the problem?</h2>
      </Zoom>
        
      <br></br>

      <Reveal ssrFadein>
        <p>
        The site addresses this problem through the simplification of the mass amounts of data that is published daily in 
        relation to the COVID-19 virus. This simplification has been done though the development of story that has been 
        illustrated in the provided detailed and graphical models, graphs and maps of the spread of the coronavirus. 
        </p>
      </Reveal>
                
    </div>
      
  );
}

function SlideText() {
  return (
    <div>
        <div className = "slideStyle">

        <Reveal ssrFadein>
        <h2> Team Members</h2>
          </Reveal>

        <div>
        <Carousel>
          <Slide right>
            <div>
              <h1>Albert</h1>
              <p>Undergrade Data Engineer</p>
            </div>
          </Slide>
          <Slide right>
            <div>
              <h1>Cohen</h1>
              <p>Undergrade Data Engineer</p>
            </div>
          </Slide>
          <Slide right>
            <div>
              <h1>Jayden</h1>
              <p>Undergrade Data Engineer</p>
            </div>
          </Slide>
          <Slide right>
            <div>
              <h1>Joel</h1>
              <p>Undergrade Data Engineer</p>
            </div>
          </Slide>
        </Carousel>
        </div>

        </div>

        </div>
       
   
      
  );
}


function Cardbox() {
  return (
    <div>
        <Card>
          <div className = "Cardstyle">
            <h3>Resources</h3>
            <br></br>
            <p>
               Sed efficitur venenatis libero non fringilla. Fusce euismod volutpat ullamcorper. 
               Curabitur non consectetur nisi. 
            </p>
           </div>
        </Card>
      </div>
      
  );
}


class AboutUs extends Component {
    constructor() {
      super();
      this.state = {
        name: 'React'
      };
    }
  
    render() {
      return (
      <div>
        <Navbar></Navbar>
        <Title></Title>
        <ParagraphOne></ParagraphOne>
        <ParagraphTwo></ParagraphTwo>
        <ParagraphThree></ParagraphThree>
        <ParagraphFour></ParagraphFour>
        <SlideText></SlideText>
        <Cardbox></Cardbox>
      </div>
    );
    }
}


export default AboutUs;