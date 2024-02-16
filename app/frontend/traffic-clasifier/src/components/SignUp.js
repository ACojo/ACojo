import * as React from "react";
import { useState } from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";
import FormHelperText from "@mui/material/FormHelperText";
import InputLabel from "@mui/material/InputLabel";
import FormControl from "@mui/material/FormControl";
import axios from "axios";

function Copyright(props) {
  return (
    <Typography
      variant="body2"
      color="text.secondary"
      align="center"
      {...props}
    >
      {"Copyright © "}
      <Link color="inherit" href="https://mui.com/">
        Your Website
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}

// TODO remove, this demo shouldn't need to reset the theme.

const defaultTheme = createTheme();

export default function SignUp(props) {
  const [noPkt, setNoPkt] = useState("");
  const [flags, setFlags] = useState("");
  const [method, setMethod] = useState("");
  const [pktsSize, setPktSize] = useState("");
  const [ipDestA, setIpDestA] = useState("");
  const [ipDestB, setIpDestB] = useState("");
  const [ipDestC, setIpDestC] = useState("");
  const [ipDestD, setIpDestD] = useState("");
  const [ipSrcA, setIpSrcA] = useState("");
  const [ipSrcB, setIpSrcB] = useState("");
  const [ipSrcC, setIpSrcC] = useState("");
  const [ipSrcD, setIpSrcD] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    let ipdest =
      data.get("IPDestA") +
      "." +
      data.get("IPDestB") +
      "." +
      data.get("IPDestC") +
      "." +
      data.get("IPDestD");
    let ipsrc =
      data.get("IPSrcA") +
      "." +
      data.get("IPSrcB") +
      "." +
      data.get("IPSrcC") +
      "." +
      data.get("IPSrcD");
    const matchesIpDest = ipdest.match(/[a-zA-Z]/g); // Caută toate literele din șir
    const matchesIpSrc = ipsrc.match(/[a-zA-Z]/g); // Caută toate literele din șir
    // const containsLetters = matches !== null && matches.length > 0;
    if (
      !(
        matchesIpDest !== null &&
        matchesIpDest.length > 0 &&
        matchesIpSrc !== null &&
        matchesIpSrc.length > 0
      )
    ) {
      console.log(props.name);
      console.log(props.methodPort);

      
      const dataPUT = { 
        // console.log({
        traffic: props.name,
        pkts: data.get("pkts"),
        TimeBetweenPackets: data.get("TimeBetweenPackets"),
        pktsSize: data.get("pktsSize"),
        ipDest: ipdest,
        ipSrc: ipsrc,
        method: data.get("method"),
        flags: data.get("flags")};
      // });
      setNoPkt("");
      setFlags("");
      setMethod("");
      setPktSize("");
      setIpDestA("");
      setIpDestB("");
      setIpDestC("");
      setIpDestD("");
      setIpSrcA("");
      setIpSrcB("");
      setIpSrcC("");
      setIpSrcD("");

      let url="127.0.0.1:8000/sendtraffic/"
      axios.put(url, dataPUT)
      .then(response => {
        console.log("Răspuns de la server:", response.data);
        
      })
      .catch(error => {
        console.error("Eroare:", error);
      });

    }
  };

  return (
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 2,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <Box
            component="form"
            noValidate
            onSubmit={handleSubmit}
            sx={{ mt: 3 }}
          >
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <TextField
                  autoComplete="no of pkts"
                  name="pkts"
                  fullWidth
                  id="pkts"
                  label="No. of packets"
                  autoFocus
                  value={noPkt}
                  onChange={(event) => {
                    setNoPkt(event.target.value);
                  }}
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  required
                  fullWidth
                  id="TimeBetweenPackets"
                  label="Time between packets"
                  name="TimeBetweenPackets"
                  autoComplete="Time between packets"
                />
              </Grid>

              <Grid item xs={6} sm={12}>
                <TextField
                  autoComplete="package size"
                  name="pktsSize"
                  fullWidth
                  id="pktsSize"
                  label="Package size (1 500B - 9 000B)"
                  autoFocus
                  value={pktsSize}
                  onChange={(event) => {
                    setPktSize(event.target.value);
                  }}
                />
              </Grid>
            </Grid>

            {/* <Grid container spacing={2}>

            </Grid> */}
            <p> </p>
            <h>The destination IP</h>
            <p> </p>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={3}>
                <TextField
                  fullWidth
                  id="IPDestA"
                  label="IP A"
                  name="IPDestA"
                  autoComplete="IP A"
                  value={ipDestA}
                  onChange={(event) => {
                    setIpDestA(event.target.value);
                  }}
                />
              </Grid>
              <Grid item xs={12} sm={3}>
                <TextField
                  fullWidth
                  id="IPDestB"
                  label="IP B"
                  name="IPDestB"
                  autoComplete="IP B"
                  value={ipDestB}
                  onChange={(event) => {
                    setIpDestB(event.target.value);
                  }}
                />
              </Grid>
              <Grid item xs={12} sm={3}>
                <TextField
                  fullWidth
                  id="IPDestC"
                  label="IP C"
                  name="IPDestC"
                  autoComplete="IP C"
                  value={ipDestC}
                  onChange={(event) => {
                    setIpDestC(event.target.value);
                  }}
                />
              </Grid>
              <Grid item xs={12} sm={3}>
                <TextField
                  fullWidth
                  id="IPDestD"
                  label="IP D"
                  name="IPDestD"
                  autoComplete="IP D"
                  value={ipDestD}
                  onChange={(event) => {
                    setIpDestD(event.target.value);
                  }}
                />
              </Grid>
            </Grid>
            <p> </p>
            <h>The source IP</h>
            <p> </p>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={3}>
                <TextField
                  fullWidth
                  id="IPSrcA"
                  label="IP A"
                  name="IPSrcA"
                  autoComplete="IP A"
                  value={ipSrcA}
                  onChange={(event) => {
                    setIpSrcA(event.target.value);
                  }}
                />
              </Grid>
              <Grid item xs={12} sm={3}>
                <TextField
                  fullWidth
                  id="IPSrcB"
                  label="IP B"
                  name="IPSrcB"
                  autoComplete="IP B"
                  value={ipSrcB}
                  onChange={(event) => {
                    setIpSrcB(event.target.value);
                  }}
                />
              </Grid>
              <Grid item xs={12} sm={3}>
                <TextField
                  fullWidth
                  id="IPSrcC"
                  label="IP C"
                  name="IPSrcC"
                  autoComplete="IP C"
                  value={ipSrcC}
                  onChange={(event) => {
                    setIpSrcC(event.target.value);
                  }}
                />
              </Grid>
              <Grid item xs={12} sm={3}>
                <TextField
                  fullWidth
                  id="IPSrcD"
                  label="IP D"
                  name="IPSrcD"
                  autoComplete="IP D"
                  value={ipSrcD}
                  onChange={(event) => {
                    setIpSrcD(event.target.value);
                  }}
                />
              </Grid>
            </Grid>
            <p></p>
            <h> </h>
            <p></p>
            <Grid container spacing={2}>
              <FormControl sx={{ m: 2, width: 170 }}>
                <InputLabel id="demo-simple-select-helper-label">
                  {props.methodPort}
                </InputLabel>
                <Select
                  labelId="method"
                  name="method"
                  id="method"
                  value={method}
                  label="method"
                  onChange={(event) => {
                    setMethod(event.target.value);
                  }}
                >
                  {/* <MenuItem value="">
                      <em>None</em>
                    </MenuItem> */}
                  <MenuItem value={0}>{props.listMethodPort[0]}</MenuItem>
                  <MenuItem value={250}>{props.listMethodPort[1]}</MenuItem>
                  <MenuItem value={500}>{props.listMethodPort[2]}</MenuItem>
                  <MenuItem value={750}>{props.listMethodPort[3]}</MenuItem>
                </Select>
              </FormControl>

              {(props.name === "tcp" )? (
                <FormControl sx={{ m: 2, width: 175 }}>
                  <InputLabel id="demo-simple-select-helper-label">
                    Flags
                  </InputLabel>
                  <Select
                    labelId="flags"
                    name="flags"
                    id="flags"
                    value={flags}
                    label="flags"
                    onChange={(event) => {
                      setFlags(event.target.value);
                    }}
                  >
                    {/* <MenuItem value="">
                    <em>None</em>
                  </MenuItem> */}
                    <MenuItem value={0}>RESET</MenuItem>
                    <MenuItem value={250}>ACK</MenuItem>
                    <MenuItem value={500}>SYN</MenuItem>
                    <MenuItem value={750}>ECHO REQUEST</MenuItem>
                  </Select>
                </FormControl>
              ) : (
                <FormControl sx={{ m: 2, width: 175 }}>
                  <InputLabel id="demo-simple-select-helper-label">
                    Flags
                  </InputLabel>
                  <Select
                    labelId="flags"
                    name="flags"
                    id="flags"
                    value={flags}
                    label="flags"
                    onChange={(event) => {
                      setFlags(event.target.value);
                    }}
                  >
                    {/* <MenuItem value="">
                            <em>None</em>
                          </MenuItem> */}
                    <MenuItem value={0}>IN</MenuItem>

                    <MenuItem value={750}>OUT</MenuItem>
                  </Select>
                </FormControl>
              )}
            </Grid>

            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Send traffic
            </Button>
            <Grid container justifyContent="flex-end"></Grid>
          </Box>
        </Box>
        <Copyright sx={{ mt: 5 }} />
      </Container>
    </ThemeProvider>
  );
}
