import React from 'react';
import { Grid, Typography } from '@mui/material';
import { gridProperties } from '@src/utils';
import './messages.less';

export const Messages = (): React.ReactElement => {
  return (
    <Grid container item { ...gridProperties }>
      <Typography component="h1" variant="h5">
        Сообщения
      </Typography>
    </Grid>
  );
};
