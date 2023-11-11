import React from 'react';
import { Delete, Edit } from '@mui/icons-material';
import { Button, ButtonGroup, Grid, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from '@mui/material';
import { getProfiles } from '@src/api';
import { gridProperties } from '@src/utils';

export const Employees = (): React.ReactElement => {
  const [profiles, setProfiles] = React.useState([]);

  React.useEffect(() => {
    getProfiles()
      .then(res => setProfiles(res))
      .catch(console.log);
  }, []);

  return (
    <Grid container item { ...gridProperties } md={10}>
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>ФИО</TableCell>
              <TableCell>Отдел</TableCell>
              <TableCell>Ремарка</TableCell>
              <TableCell align="center">Действия</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {profiles.map((row) => (
              <TableRow key={row.id} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell component="th" scope="row">
                  {row.lastname + ' ' + row.firstname + ' ' + row.secondname}
                </TableCell>
                <TableCell>{row.jt.title}</TableCell>
                <TableCell>{row.remark}</TableCell>
                <TableCell align="center">
                  <ButtonGroup variant="text" aria-label="text button group">
                    <Button startIcon={<Edit />} />
                    <Button color="error" startIcon={<Delete />} />
                  </ButtonGroup>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Grid>
  );
};
