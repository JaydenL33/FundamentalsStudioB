
import React, { Component } from 'react';

import "./Header.css"

import {
	BrowserRouter as Router,
	Switch,
	Route,
	Link
  } 
from "react-router-dom";



// a in style.css has now become <link> so remember to replace that in the CSS. 

class Header extends Component {
    render() {
        return (
            <Router>
                <h1>SANITISE.<span>MEDIA</span></h1>
                <ul class="nav_links">
                    <li>
                        <Link to="/Indicators">Indicators</Link>
                    </li>
                    <li>
                        <Link to="/Story">Story</Link>
                    </li>
                    <li>
                        <Link to="/AboutUs">About Us</Link>
                    </li>
                    <li>
                        <Link to="/ContactUs">Contact Us</Link>
                    </li>
                </ul>
                    <Switch>
                        <Route path="/Indicators">
                            <Indicators />
                        </Route>
                        <Route path="/">
                            <Story />
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

function Indicators() {
    return null;
  }

function Story()
{
    return null;
}
  
function AboutUs() {
    return null;
}

function ContactUs() {
    return null;
}


export default Header;