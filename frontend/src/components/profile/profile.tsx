import React from 'react';
import { Grid } from '@mui/material';
import { gridProperties } from '@src/utils';
import './profile.less';

export const Profile = (): React.ReactElement => {
  return (
    <Grid container item { ...gridProperties }>
      <p>
        Профиль
      </p>
    </Grid>
  );
};
