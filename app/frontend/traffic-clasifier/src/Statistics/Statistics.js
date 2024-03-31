import React, { Component } from "react";
import { Card, ListGroup } from "react-bootstrap";
import BasicTable from "../components/BasicTable";
import Button from "@mui/material/Button";
import axios from "axios";


// class Statistics extends Component {
    
export default function Statistics(props){
    const getClassifiedStatistics = async (event) => {
        let url = "http://localhost:5000/api/getStatisticsdData";
        // let tcp_values=[0,0,0,0]
        // let udp_values=[0,0,0,0]
        try {
          const response = await axios.get(url);
          console.log(response.data)
          
    
        //   for (var i=0; i < 4; i++){
        //       tcp_values[i] = response.data[i]
        //       udp_values[i] = response.data[i+4]
        //   }
        //   SetTcpResult(tcp_values)
        //   SetUdpResult(udp_values)
          console.log(response.data);
        } catch (error) {
          console.error("Eroare:", error);
        }
      };




//   render() {
    return (
      <div>
        <div style={{ justifyContent: "center", padding: 30 }}>
          <h2>Statistics Page for the last classification</h2>
        </div>
        <div style={{ display: "flex", justifyContent: "center", padding: 30 }}>
          <h2>
            <BasicTable type="TCP" attack2="Smurf" attack3="Buffer" />
          </h2>
        </div>
        <div style={{ display: "flex", justifyContent: "center", padding: 30 }}>
          <h2>
            <BasicTable type="UDP" attack2="Insider" attack3="Amplification" />
          </h2>
        </div>

        <Button
          onClick={getClassifiedStatistics}
          variant="contained"
          sx={{ mt: 3, mb: 2 }}
        >
          Send normal traffic
        </Button>
      </div>
    );
//   }
}

// export default Statistics;
