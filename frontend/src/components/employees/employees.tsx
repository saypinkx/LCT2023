import React from 'react';
import { Grid, Typography } from '@mui/material';
import { gridProperties } from '@src/utils';

export const Employees = (): React.ReactElement => {
  return (
    <Grid container item { ...gridProperties }>
      <Typography component="h1" variant="h5">
        Сотрудники
      </Typography>
    </Grid>
  );
};
