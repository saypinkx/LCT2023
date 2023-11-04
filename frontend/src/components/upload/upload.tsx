import React from 'react';
import { Grid } from '@mui/material';
import { gridProperties } from '@src/utils';
import './upload.less';

export const Upload = (): JSX.Element => {
  return (
    <Grid container item { ...gridProperties }>
      <p className="uploader-description">
        Загрузите Excel
      </p>
    </Grid>
  );
};
