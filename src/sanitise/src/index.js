
import React from 'react';
import ReactDOM from 'react-dom';
import * as apis from './APILoader.js';
import Header from './Header'
import Display from "./display"




ReactDOM.render(<Header />, document.getElementById('nav'));



ReactDOM.render(<Display 
    title={"SANITISE.MEDIA @ UTS"}
    title2={"(Showing and Naming Integral Tools in Slowing Epidemics"}
 />, document.getElementsByClassName('intro')[0]);

