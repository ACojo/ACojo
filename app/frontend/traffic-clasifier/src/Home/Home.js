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
  const [tcpResult, SetTcpResult] = useState([1,0,0,0])
  const [udpResult, SetUdpResult] = useState([1,0,0,0])

  // the get request
  const handleSubmit = async (event) => {
    let url = "http://localhost:5000/api/getClassifiedData";
    let tcp_values=[0,0,0,0]
    let udp_values=[0,0,0,0]
    try {
      const response = await axios.get(url);
      console.log(response.data)
      

      for (var i=0; i < 4; i++){
          tcp_values[i] = response.data[i]
          udp_values[i] = response.data[i+4]
      }
      SetTcpResult(tcp_values)
      SetUdpResult(udp_values)
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
        
          <div>
            <BasicPie tcpResult={tcpResult} type={['Normal traffic', 'DOS / DDOS', 'Smurf', 'Buffer overun']} />
          </div>
          
          <div>
            <BasicPie tcpResult={udpResult} type={['Normal traffic', 'DOS / DDOS', 'Insider', 'Amplification']} />

          </div>
            
            
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
