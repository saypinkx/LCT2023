import React from 'react';
import { Grid } from '@mui/material';
import { gridProperties } from '@src/utils';
import './main.less';

export const Main = (): React.ReactElement => {
  return (
    <Grid container item { ...gridProperties }>
      <p>
        Главная
      </p>
    </Grid>
  );
};
