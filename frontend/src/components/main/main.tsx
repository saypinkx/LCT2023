import React from 'react';
import { Grid, Typography } from '@mui/material';
import { gridProperties } from '@src/utils';
import './main.less';

export const Main = (): React.ReactElement => {
  return (
    <Grid container item { ...gridProperties }>
      <Typography component="h1" variant="h5">
        Главная
      </Typography>
    </Grid>
  );
};
