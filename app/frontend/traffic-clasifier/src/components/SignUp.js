import * as React from 'react';
import { useState } from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Select from '@mui/material/Select'
import MenuItem from '@mui/material/MenuItem'
import FormHelperText from '@mui/material/FormHelperText'
import InputLabel from '@mui/material/InputLabel'
import FormControl from '@mui/material/FormControl'

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'Copyright © '}
      <Link color="inherit" href="https://mui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

// TODO remove, this demo shouldn't need to reset the theme.

const defaultTheme = createTheme();

export default function SignUp(props) {

  const [noPkt,setNoPkt] = useState('')



  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log({
        pkts : data.get('pkts'),
        email: data.get('email'),
        password: data.get('password'),
        flags: data.get('flags')
    });
    setNoPkt('')
  };

  return (
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 2,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >

          <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
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
                    onChange={event =>{setNoPkt(event.target.value)}}
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
            </Grid>
              <p> </p>
              <h>The destination IP</h>
              <p> </p>
            <Grid container spacing={2}>
                <Grid item xs={12} sm={3}>
                  <TextField
                    required
                    fullWidth
                    id="IPDestA"
                    label="IP A"
                    name="IPDestA"
                    autoComplete="IP A"
                  />
                </Grid>
                <Grid item xs={12} sm={3}>
                  <TextField
                    required
                    fullWidth
                    id="IPDestB"
                    label="IP B"
                    name="IPDestB"
                    autoComplete="IP B"
                  />
                </Grid>
                <Grid item xs={12} sm={3}>
                  <TextField
                    required
                    fullWidth
                    id="IPDestC"
                    label="IP C"
                    name="IPDestC"
                    autoComplete="IP C"
                  />
                </Grid>
                <Grid item xs={12} sm={3}>
                  <TextField
                    required
                    fullWidth
                    id="IPDestD"
                    label="IP D"
                    name="IPDestd"
                    autoComplete="IP D"
                  />
                </Grid>
              </Grid>
              <p> </p>
              <h>The source IP</h>
              <p> </p>
              <Grid>
              <Grid container spacing={2}>
                <FormControl sx={{ m: 1, minWidth: 120 }}>
                  <InputLabel id="demo-simple-select-helper-label">Age</InputLabel>
                  <Select
                    labelId="flags"
                    name='flags'
                    id="flags"
                    value={10}
                    label="Age"
                    // onChange={handleChange}
                  >
                    <MenuItem value="">
                      <em>None</em>
                    </MenuItem>
                    <MenuItem value={10}>10</MenuItem>
                    <MenuItem value={20}>Twenty</MenuItem>
                    <MenuItem value={30}>Thirty</MenuItem>
                  </Select>
                  <FormHelperText>With label + helper text</FormHelperText>
                  </FormControl>
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
            </Grid>
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign Up
            </Button>
            <Grid container justifyContent="flex-end">

            </Grid>
          </Box>
        </Box>
        <Copyright sx={{ mt: 5 }} />
      </Container>
    </ThemeProvider>
  );
}