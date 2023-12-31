import React from 'react';
import { Delete, Edit } from '@mui/icons-material';
import { Button, ButtonGroup, Grid, Link, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from '@mui/material';
import { deleteMaterial, getFolders, getMaterials } from '@src/api';
import { MaterialEdit } from '@src/components';
import { useAuth } from '@src/hooks';
import { Folder, Material } from '@src/models';
import { gridProperties } from '@src/utils';

export const Materials = (): React.ReactElement => {
  const { user } = useAuth();
  const [item, setItem] = React.useState<Material | null | undefined>();
  const [folders, setFolders] = React.useState<Folder[]>([]);
  const [materials, setMaterials] = React.useState<Material[]>([]);
  const isHr = React.useMemo(() => user.role === 'hr', [user]);

  const onDelete = (id: number): void => {
    deleteMaterial(id)
      .then(() => update())
      .catch(console.log);
  };

  const onClose = (isSubmit: boolean): void => {
    setItem(undefined);
    if (isSubmit) update();
  };

  const update = (): void => {
    Promise.all([getFolders(), getMaterials()])
      .then(([folders, items]) => {
        const res = items.map(item => ({
          folder_id: item.folder_id,
          folder_name: folders.find(f => f.id === item.folder_id)?.name || '-',
          id: item.id,
          link: item.link,
          name: item.name,
        }));
        setFolders(folders);
        setMaterials(res);
      })
      .catch(console.log);
  }

  React.useEffect(() => {
    update();
  }, []);

  return (
    <Grid container item { ...gridProperties } md={10}>
      {
        isHr && (
          <Button color="secondary" style={{ marginBottom: '8px' }} onClick={() => setItem(null)}>
            Добавить материал
          </Button>
        )
      }
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Наименование</TableCell>
              <TableCell>Директория</TableCell>
              <TableCell>Ссылка</TableCell>
              {isHr && <TableCell align="center">Действия</TableCell>}
            </TableRow>
          </TableHead>
          <TableBody>
            {materials.map((row) => (
              <TableRow key={row.id} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell component="th" scope="row">
                  {row.name}
                </TableCell>
                <TableCell>{row.folder_name}</TableCell>
                <TableCell>
                  {
                    row.link ? (
                      <Link href={row.link} target="_blank" underline="none">{row.link}</Link>
                    ) : '-'
                  }
                </TableCell>
                {
                  isHr && (
                    <TableCell align="center">
                      <ButtonGroup variant="text" aria-label="text button group">
                        <Button startIcon={<Edit />} onClick={() => setItem(row)} />
                        <Button color="error" startIcon={<Delete />} onClick={() => onDelete(row.id)} />
                      </ButtonGroup>
                    </TableCell>
                  )
                }
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
      {item !== undefined && <MaterialEdit folders={folders} item={item} onClose={onClose} />}
    </Grid>
  );
};
