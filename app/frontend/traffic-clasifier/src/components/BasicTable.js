import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

function createData(
  timestamp: number,
  knn: number,
  dt: number,
  dnn: number,
  
) {
  return { timestamp, knn, dt, dnn };
}

const rows = [
  createData('Frozen yoghurt', 159, 6.0, 24),
  createData('Ice cream sandwich', 237, 9.0, 37),
  createData('Eclair', 262, 16.0, 24),
  createData('Cupcake', 305, 3.7, 67),
  createData('Gingerbread', 356, 16.0, 49),
];

export default function BasicTable() {
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Timestamp of evaluation</TableCell>
            <TableCell align="right">KNN&nbsp;(%)</TableCell>
            <TableCell align="right">DT&nbsp;(%)</TableCell>
            <TableCell align="right">DNN</TableCell>
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