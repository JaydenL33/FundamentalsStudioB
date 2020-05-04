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

// import { Home } from './Home';
// import { About } from './About';
// import { NoMatch } from './NoMatch';
// import Sidebar from './components/Sidebar';

function App() {
  return (
    <React.Fragment>
      <Router>
        <NavigationBar />

        <Sidebar />

        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/about" component={About} />
          <Route component={NoMatch} />
        </Switch>
      </Router>
    </React.Fragment>
  );
}

export default App;
