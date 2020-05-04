// Author: Albert
// Created: 04-05-2020
// Updated: 04-05-2020
// note: adds new components and "templating" REACT style to app
// note: TEMP FILE AS PROJECT APP.JS WASNT GIT TRACKED


import React from 'react';
import logo from './logo.svg';
import './App.css';

import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { NavigationBar } from './components/NavigationBar';

import { Indicators } from './Indicators';
import { Story } from './Story';
import { About } from './AboutUs';
import { ContactUs } from './ContactUs';
import { NoMatch } from './NoMatch';

// import Sidebar from './components/Sidebar';

function App() {
  return (
    <React.Fragment>
      <Router>
        <NavigationBar />
        
        {/* Router uses the switch to convey the user to different pages */}
        <Switch>
          <Route exact path="/" component={Story} />
          <Route path="/Indicators" component={Indicators} />
          <Route path="/" component={Story} />
          <Route path="/ConactUs" component={ContactUs} />
          <Route path="/AboutUs" component={About} />
          <Route component={NoMatch} />
        </Switch>
      </Router>
    </React.Fragment>
  );
}

export default App;
