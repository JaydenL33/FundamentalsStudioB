
import React, { Component } from 'react';

import "./App.css";
import AboutUs from './pages/AboutUs';
import Indicators from './pages/Indicators';
import Story from './pages/Story';
import ContactUs from './pages/ContactUs';


import {
	BrowserRouter as Router,
	Switch,
	Route,
  } 
from "react-router-dom";



// a in style.css has now become <link> so remember to replace that in the CSS. 

class App extends Component {
    
    render() {
        return (
            <Router>
                <Switch>
                    <Route exact path="/">
                        <Story />
                     </Route>
                    <Route path="/Indicators">
                        <Indicators />
                    </Route>
                    <Route path="/AboutUs">
                        <AboutUs />
                    </Route>
                    <Route path="/ContactUs">
                        <ContactUs />
                    </Route>
                </Switch>
            </Router>
        )
    }
};



export default App;