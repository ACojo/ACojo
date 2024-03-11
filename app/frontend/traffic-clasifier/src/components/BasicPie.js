import * as React from 'react';
import { PieChart } from '@mui/x-charts/PieChart';

export default function BasicPie(props) {
  return (
    console.log(props),
    // console.log(tcpResult.content[0]),
    // console.log(typeof(props.tcpResult)),
    // console.log(props.tcpResult),
    // console.log(props.tcpResult[0]),
    <div
      style={{
      display: "flex",
      alignItems: "center",
      height: "100%"
    }} 
    >
      <PieChart
        series={[
          {
            data: [
              { id: 0, value: props.tcpResult[0], label: props.type[0] },
              { id: 1, value: props.tcpResult[1], label: props.type[1]},
              { id: 2, value: props.tcpResult[2], label: props.type[2] },
              { id: 3, value: props.tcpResult[3], label: props.type[3] },
            ],
          },
        ]}
        width={400}
        height={200}
        
    />


    </div>
  
  );
}
