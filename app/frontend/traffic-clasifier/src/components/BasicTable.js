import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

function createData(
  timestamp: String,
  knn: String,
  dt: String,
  dnn: String,
  
) {
  return { timestamp, knn, dt, dnn };
}



export default function BasicTable(props) {
  console.log("rewfrfre")
  console.log(props.data)
  console.log(props.data[0]['no1'][0]['date'])
  const rows = [
    createData(props.data[0]['no1'][0]['date'], props.data[0]['no1'][0]['knn'], props.data[0]['no1'][0]['dtt'], props.data[0]['no1'][0]['dnn']),
    createData(props.data[0]['no2'][0]['date'], props.data[0]['no2'][0]['knn'], props.data[0]['no2'][0]['dtt'], props.data[0]['no2'][0]['dnn']),
    createData(props.data[0]['no3'][0]['date'], props.data[0]['no3'][0]['knn'], props.data[0]['no3'][0]['dtt'], props.data[0]['no3'][0]['dnn']),
    createData(props.data[0]['no4'][0]['date'], props.data[0]['no4'][0]['knn'], props.data[0]['no4'][0]['dtt'], props.data[0]['no4'][0]['dnn']),
    createData(props.data[0]['no5'][0]['date'], props.data[0]['no5'][0]['knn'], props.data[0]['no5'][0]['dtt'], props.data[0]['no5'][0]['dnn']),
  ];
  console.log("look here")
  console.log(props.data[0]['no1'][0]['date'])
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead >
        {props.type} data each row (normal DDoS {props.attack2} {props.attack3})
          <TableRow>
            <TableCell>Timestamp of evaluation</TableCell>
            <TableCell align="center">KNN</TableCell>
            <TableCell align="center">DT</TableCell>
            <TableCell align="center">DNN</TableCell>
            {/* <TableCell align="right">Protein&nbsp;(g)</TableCell> */}
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.timestamp}
              </TableCell>
              <TableCell align="right">{row.knn}</TableCell>
              <TableCell align="right">{row.dt}</TableCell>
              <TableCell align="right">{row.dnn}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>



  );
}