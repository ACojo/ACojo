import React, { Component, useState } from 'react';
import "./Generator.css";
import Switch from '@mui/material/Switch';
import BasicPie from '../components/BasicPie';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import TcpGen from '../components/TcpGen';
import BasicFormControl from '../components/BasicControl';
import SignUp from '../components/SignUp';
import BasicControl from '../components/BasicControl';




function Generator(){
    const [trafficType, setTrafficType] = useState(false)


    function handleSwitch() {

        setTrafficType(!trafficType)
        
    }

        return (
            <div className='Generator'>
                <div style={{ display: 'flex', justifyContent: 'center', padding: 30 }}>
                    <h2>Generator for TCP/UDP traffic</h2>

                </div>
                <div className='switch'>



                <FormGroup>
                <Stack direction="row" spacing={1} alignItems="center">
                <Typography>TCP</Typography>
                <Switch onChange={handleSwitch} />
                <Typography>UDP</Typography>
                </Stack>
                </FormGroup>
                
                </div>
                <div>

                    {!trafficType ? (
                        // the tcp form 
                        //  <TcpGen />
                         <SignUp name="TCP"/>
                        //console.log("este fals")
                     ) : (
                        // the udp form
                        <SignUp name="UDP"/>
                        //console.log("nu este fals")
      )}
                </div>
            </div>


        );
    
}

export default Generator;