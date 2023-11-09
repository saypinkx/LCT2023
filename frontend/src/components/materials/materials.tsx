import React from 'react';
import { Grid } from '@mui/material';
import { gridProperties } from '@src/utils';
import './materials.less';

export const Materials = (): React.ReactElement => {
  return (
    <Grid container item { ...gridProperties }>
      <p>
        Материалы
      </p>
    </Grid>
  );
};
