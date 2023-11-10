import React, { useEffect, useState } from 'react';
import { Grid, Link, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from '@mui/material';
import { getFolders, getMaterials } from '@src/api';
import { Material } from '@src/models';
import { gridProperties } from '@src/utils';
import './materials.less';

export const Materials = (): React.ReactElement => {
  const [materials, setMaterials] = useState<Material[]>([]);

  const update = (): void => {
    Promise.all([getFolders(), getMaterials()])
      .then(([folders, items]) => {
        const res = items.map(item => ({
          folder_name: folders.find(f => f.id === item.folder_id)?.name || '-',
          id: item.id,
          link: item.link,
          name: item.name,
        }));
        setMaterials(res);
      })
      .catch(() => setMaterials([]));
  }

  useEffect(() => {
    update();
  }, []);

  return (
    <Grid container item { ...gridProperties }>
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Наименование</TableCell>
              <TableCell>Директория</TableCell>
              <TableCell>Ссылка</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {materials.map((row) => (
              <TableRow key={row.id} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell component="th" scope="row">
                  {row.name}
                </TableCell>
                <TableCell>{row.folder_name}</TableCell>
                <TableCell>{row.link ? (<Link href={row.link}>{row.link}</Link>) : '-'}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Grid>
  );
};
