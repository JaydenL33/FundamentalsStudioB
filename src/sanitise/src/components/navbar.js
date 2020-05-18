import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import './navbar.css';

const imagestyle = {
    height: "50px",
    width: "25px"
}

class Navbar extends Component {
    render () {
        return (
        <header id ="nav">
            <h1>SANITISE.<span>MEDIA</span></h1>
            <img src="/SANITISE_LOGO.png" style={imagestyle} alt=""/>
            <ul className="nav_links">
                <li>
                    <Link to="/">Story</Link>
                </li>
                <li>
                    <Link to="/Indicators">Indicators</Link>
                </li>
                <li>
                    <Link to="/AboutUs">About Us</Link>
                </li>
                <li>
                    <Link to="/ContactUs">Contact Us</Link>
                </li>
            </ul>
        </header>
        );
    }
}

export default Navbar;