import React, { Component } from "react";
import { Router, Route } from "react-router-dom";

import Generator from "./Generator/Generator";
import Contact from "./Contact/Contact";
import Statistics from "./Statistics/Statistics";
import Home from "./Home/Home";
import history from './history';


export default class Routes extends Component {
    render() {
        return (
            <Router history={history}>
                
                    <Route path="/" exact component={Home} />
                    <Route path="/Generator" component={Generator} />
                    <Route path="/Statistics" component={Statistics} />
                    <Route path="/Contact" component={Contact} />
                
            </Router>
        )
    }
}