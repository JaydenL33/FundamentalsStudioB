
import React, { Component } from 'react';

import "./App.css"
import AboutUs from './pages/AboutUs'
import Indicators from './pages/Indicators'
import Story from './pages/Story'


import {
	BrowserRouter as Router,
	Switch,
	Route,
	Link
  } 
from "react-router-dom";

const imagestyle = {
    height: "50px",
    width: "25px"
}


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