import React, { Component } from "react";
import { Button } from 'react-bootstrap';
import history from './../history';
import BasicPie from "../components/BasicPie";
import "./Home.css";

export default class Home extends Component {
  render() {
    return (
      <div className="Home">
        <div className="lander">
          <h1>Home page</h1>
          <p>Here is the network status and the history's pie chart</p>
          <BasicPie />
          <form>
            <Button variant="btn btn-success" onClick={() => history.push('/Products')}>Click button to view products</Button>
          </form>
          
        </div>
      </div>
    );
  }
}