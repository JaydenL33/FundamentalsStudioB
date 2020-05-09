
import React from 'react';
import ReactDOM from 'react-dom';
import * as apis from './APILoader.js';
import Header from './Header'
import Display from "./display"


ReactDOM.render(<Header />, document.getElementById('nav'));



ReactDOM.render(<Display 
    title={"SANITISE.MEDIA @ UTS"}
    title2={"(Showing and Naming Integral Tools in Slowing Epidemics)"}
    paragraph1={"Our Mission is to educate the generation population about the risks and real issues around SARS-CoV-2"}
 />, document.getElementById('intro'));

 ReactDOM.render(<Display 
    title={"SANITISE.MEDIA @ UTS"}
    title2={"(Showing and Naming Integral Tools in Slowing Epidemics)"}
    paragraph1={"Our Mission is to educate the generation population about the risks and real issues around SARS-CoV-2"}
 />, document.getElementById('main-body'));

