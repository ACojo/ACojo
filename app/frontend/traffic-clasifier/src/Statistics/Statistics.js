import React, { Component, useEffect, useState } from "react";
import { Card, ListGroup } from "react-bootstrap";
import BasicTable from "../components/BasicTable";
import Button from "@mui/material/Button";
import axios from "axios";

// class Statistics extends Component {

export default function Statistics(props) {
  const [dataTCP, setDataTCP] = useState([
    {
      no1: [
        {
          date: "xx-xx-xxxx",
          knn: "xx-xx-xxxx",
          dtt: "xx-xx-xxxx",
          dnn: "xx-xx-xxxx",
        },
      ],
      no2: [
        {
          date: "xx-xx-xxxx",
          knn: "xx-xx-xxxx",
          dtt: "xx-xx-xxxx",
          dnn: "xx-xx-xxxx",
        },
      ],
      no3: [
        {
          date: "xx-xx-xxxx",
          knn: "xx-xx-xxxx",
          dtt: "xx-xx-xxxx",
          dnn: "xx-xx-xxxx",
        },
      ],
      no4: [
        {
          date: "xx-xx-xxxx",
          knn: "xx-xx-xxxx",
          dtt: "xx-xx-xxxx",
          dnn: "xx-xx-xxxx",
        },
      ],
      no5: [
        {
          date: "xx-xx-xxxx",
          knn: "xx-xx-xxxx",
          dtt: "xx-xx-xxxx",
          dnn: "xx-xx-xxxx",
        },
      ],
    },
  ]);
  const [dataUDP, setDataUDP] = useState([
    {
      no1: [
        {
          date: "xx-xx-xxxx",
          knn: "xx-xx-xxxx",
          dtt: "xx-xx-xxxx",
          dnn: "xx-xx-xxxx",
        },
      ],
      no2: [
        {
          date: "xx-xx-xxxx",
          knn: "xx-xx-xxxx",
          dtt: "xx-xx-xxxx",
          dnn: "xx-xx-xxxx",
        },
      ],
      no3: [
        {
          date: "xx-xx-xxxx",
          knn: "xx-xx-xxxx",
          dtt: "xx-xx-xxxx",
          dnn: "xx-xx-xxxx",
        },
      ],
      no4: [
        {
          date: "xx-xx-xxxx",
          knn: "xx-xx-xxxx",
          dtt: "xx-xx-xxxx",
          dnn: "xx-xx-xxxx",
        },
      ],
      no5: [
        {
          date: "xx-xx-xxxx",
          knn: "xx-xx-xxxx",
          dtt: "xx-xx-xxxx",
          dnn: "xx-xx-xxxx",
        },
      ],
    },
  ]);

  const getClassifiedStatistics = async (event) => {
    let url = "http://localhost:5000/api/getStatisticsdData";

    try {
      const response = await axios.get(url);
      console.log("in click method");
      console.log(response.data);
      console.log(response.data["tcp"]);
      setDataTCP(response.data["tcp"]);
      setDataUDP(response.data["udp"]);
      console.log(response.data);
      console.log(typeof response.data["tcp"]);
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
          <BasicTable
            type="TCP"
            attack2="Smurf"
            attack3="Buffer"
            data={dataTCP}
          />
        </h2>
      </div>
      <div style={{ display: "flex", justifyContent: "center", padding: 30 }}>
        <h2>
          <BasicTable
            type="UDP"
            attack2="Insider"
            attack3="Amplification"
            data={dataUDP}
          />
        </h2>
      </div>

      <Button
        onClick={getClassifiedStatistics}
        variant="contained"
        sx={{ mt: 3, mb: 2 }}
      >
        Get statistics data
      </Button>
    </div>
  );
  //   }
}

// export default Statistics;
