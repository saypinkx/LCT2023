import React from 'react';
import { Grid } from '@mui/material';
import { gridProperties } from '@src/utils';
import './messages.less';

export const Messages = (): React.ReactElement => {
  return (
    <Grid container item { ...gridProperties }>
      <p>
        Сообщения
      </p>
    </Grid>
  );
};
