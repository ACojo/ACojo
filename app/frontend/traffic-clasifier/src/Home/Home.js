import React, { Component } from "react";
import { useState } from "react";
import { Button } from "react-bootstrap";
import axios from "axios";
import history from "./../history";
import BasicPie from "../components/BasicPie";
import "./Home.css";

// export default class Home extends Component {
export default function Home(props) {
  const [attackMessage, setAttackMessage] = useState(
    "Currently there is no anomaly detected"
  );
  const [tcpResult, SetTcpResult] = useState([0,0,0,0])
  const [udpResult, SetUdpResult] = useState([0,0,0,0])

  // the get request
  const handleSubmit = async (event) => {
    let url = "http://localhost:5000/api/getClassifiedData";
    try {
      const response = await axios.get(url);
      console.log(response.data)
      SetTcpResult(response.data)
      
      console.log(response.data);
    } catch (error) {
      console.error("Eroare:", error);
    }
  };

  // render() {
  return (
    <div className="Home">
      <div className="lander">
        <h1>Home page</h1>
        <p>{attackMessage}</p>
        <BasicPie tcpResult={tcpResult} />
        <form>
          <Button
            variant="btn btn-success"
            onClick={handleSubmit}
          >
            Evaluate current traffic
          </Button>
        </form>
      </div>
    </div>
  );
  // }
}
