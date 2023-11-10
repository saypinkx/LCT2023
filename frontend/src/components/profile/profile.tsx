import React from 'react';
import { Grid, Typography } from '@mui/material';
import { gridProperties } from '@src/utils';
import './profile.less';

export const Profile = (): React.ReactElement => {
  return (
    <Grid container item { ...gridProperties }>
      <Typography component="h1" variant="h5">
        Профиль
      </Typography>
    </Grid>
  );
};
