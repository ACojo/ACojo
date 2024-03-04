import * as React from 'react';
import { PieChart } from '@mui/x-charts/PieChart';

export default function BasicPie() {
  return (
    <div style={{
      display: "flex",
      alignItems: "center",
      height: "100%"
    }} >
      <PieChart
        series={[
          {
            data: [
              { id: 0, value: 10, label: 'Normal  traffic' },
              { id: 1, value: 10, label: 'DOS / DDOS' },
              { id: 2, value: 15, label: 'Smurf' },
              { id: 3, value: 20, label: 'Buffer overflow' },
            ],
          },
        ]}
        width={400}
        height={200}
      
    />


    </div>
  
  );
}
