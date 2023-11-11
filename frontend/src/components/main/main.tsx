import React from 'react';
import { Grid, Typography } from '@mui/material';
import { getIsIdeal, getPlan, getPosition, getProfile } from '@src/api';
import { useAuth } from '@src/hooks';
import { gridProperties } from '@src/utils';
import './main.less';

export const Main = (): React.ReactElement => {
  const [ideal, setIdeal] = React.useState([]);
  const [plan, setPlan] = React.useState([]);
  const [quality, setQuality] = React.useState([]);
  const { user } = useAuth();

  React.useEffect(() => {
    getProfile(user.id)
      .then(res => {
        Promise.all([getIsIdeal(res.id, 3), getPlan(res.id, 3), getPosition(3)])
          .then(([isIdeal, pl, pos]) => {
            setIdeal(isIdeal.map((it: any) => pos.find((_, i) => i === it[0])?.[0] ?? '-'));
            setPlan(pl);
            setQuality(pos.filter((it: any) => it[1] > 1 && it[2].startsWith('Личностные')).map(arr => arr[0]));
          })
          .catch(console.log);
      })
      .catch(console.log);
  }, []);

  return (
    <Grid container item { ...gridProperties }>
      <Typography component="h2" variant="h5">
        {ideal.length ? 'Компетенции: ' + ideal.join(', ') : null}
      </Typography>
      <Typography component="h2" variant="h5" sx={{ mt: 2 }}>
        {plan.length ? 'Самая лучшая метрика: ' + plan[0][1] : null}
      </Typography>
      <Typography component="h2" variant="h5" sx={{ mt: 2 }}>
        {quality.length ? 'Личностные качества: ' + quality.join(', ') : null}
      </Typography>
    </Grid>
  );
};
