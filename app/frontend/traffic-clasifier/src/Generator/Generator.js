import React, { Component, useState } from "react";
import "./Generator.css";
import Switch from "@mui/material/Switch";
import BasicPie from "../components/BasicPie";
import FormGroup from "@mui/material/FormGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import Stack from "@mui/material/Stack";
import Typography from "@mui/material/Typography";
import TcpGen from "../components/TcpGen";
import BasicFormControl from "../components/BasicControl";
import SignUp from "../components/SignUp";
import BasicControl from "../components/BasicControl";

function Generator() {
  const [trafficType, setTrafficType] = useState(false);
  const [name, setName] = useState("tcp");
  const [methodPort, setMethodPort] = useState("Method");
  const [listMethodPort, setListMethodPort] = useState(["GET", "POST", "PUT", "DELETE"]);
  // var name= React.createContext();

  function handleSwitch() {
    if (trafficType) {
      setName("tcp");
      setMethodPort("Method");
      setListMethodPort(["GET", "POST", "PUT", "DELETE"]);
    } else {
      setName("udp");
      setMethodPort("Destination Port");
      setListMethodPort(["DNS", "NTP", "SNMP", "TFTP"]);
    }
    setTrafficType(!trafficType);
  }

  return (
    <div className="Generator">
      <div style={{ display: "flex", justifyContent: "center", padding: 30 }}>
        <h2>Generator for TCP/UDP traffic</h2>
      </div>
      <div className="switch">
        <FormGroup>
          <Stack direction="row" spacing={1} alignItems="center">
            <Typography>TCP</Typography>
            <Switch onChange={handleSwitch} />
            <Typography>UDP</Typography>
          </Stack>
        </FormGroup>
      </div>
      <div>
        {/* {console.log(name)} */}
        <SignUp name={name} methodPort={methodPort} listMethodPort={listMethodPort}/>
        {/* {!trafficType ? (
                        // the tcp form 
                        //  <TcpGen />
                         <SignUp name/>
                        //console.log("este fals")
                     ) : (
                        // the udp form
                        <SignUp name/>
                        //console.log("nu este fals")
      )} */}
      </div>
    </div>
  );
}

export default Generator;
