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
          <h2> Covid-19 Visualisation</h2>
        </Zoom>

        <Reveal ssrFadein>
          <p>
           Lorem ipsum dolor sit amet, consunc neque, dapibus id consequat vitae, imperdiet sit amet nisl. Mauris ac ultrices lectus, et sagittis mauris. Nunc et vestibulum augue. Fusce eget facilisis libero. Maecenas ullamcorper condimentum lorem nec ultricies.
          </p>
        </Reveal>

    </div>
      
  );
}

function ParagraphTwo() {
  return (
    <div className = "textStyle">
          <Zoom>
            <h2> What is this? </h2>
          </Zoom>
        
          <br></br>
          <Reveal ssrFadein>
            <p>
              Sed efficitur venenatis libero non fringilla. Fusce euismod volutpat ullamcorper. Curabitur non consectetur nisi. Curabitur varius tempor finibus. In eget eleifend diam, at auctor sapien. Proin at dui et nisi venenatis ultrices. Fusce sit amet libero sollicitudin, efficitur nulla in, consequat orci. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a dignissim urna. Quisque a congue ligula. Nunc scelerisque, metus non pulvinar sagittis, sem mauris ultricies lacus, eget interdum odio lorem in libero. Praesent eget tortor nisi.
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
        <h2> Why is this a problem?</h2>
      </Zoom>
      <br></br>

      <Reveal ssrFadein>
        <p>
          Sed efficitur venenatis libero non fringilla. Fusce euismod volutpat ullamcorper. 
          Curabitur non consectetur nisi. Curabitur varius tempor finibus. In eget eleifend diam,
          at auctor sapien. Proin at dui et nisi venenatis ultrices. Fusce sit amet libero sollicitudin, 
          efficitur nulla in, consequat orci. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec
           a dignissim urna. Quisque a congue ligula. Nunc scelerisque, metus non pulvinar sagittis, sem mauris
          ultricies lacus, eget interdum odio lorem in libero. Praesent eget tortor nisi.
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
          Sed efficitur venenatis libero non fringilla. Fusce euismod volutpat ullamcorper. Curabitur non consectetur nisi. Curabitur varius tempor finibus. In eget eleifend diam, at auctor sapien. Proin at dui et nisi venenatis ultrices. Fusce sit amet libero sollicitudin, efficitur nulla in, consequat orci. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a dignissim urna. Quisque a congue ligula. Nunc scelerisque, metus non pulvinar sagittis, sem mauris ultricies lacus, eget interdum odio lorem in libero. Praesent eget tortor nisi.
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