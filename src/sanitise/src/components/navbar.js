import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import './navbar.css';
/*import {Logo} from '../images/logo.png'*/
import Logo from '../images/logo.png'




const imagestyle = {
   
    height: '320px',
    width: 'auto',
    overflow: 'hidden',
    margin: '-200px 0px -200px -100px'
}

class Navbar extends Component {
    render () {
        return (
   
        <header id ="nav">
        <img src={Logo} style ={imagestyle} alt="logo"/>
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