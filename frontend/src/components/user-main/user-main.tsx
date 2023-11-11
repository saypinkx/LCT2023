import React from 'react';
import { Button, Checkbox, FormControlLabel, FormGroup, Grid, Typography } from '@mui/material';
import { getPosition} from '@src/api';
import { gridProperties } from '@src/utils';

export const UserMain = (): React.ReactElement => {
  const [quality, setQuality] = React.useState([]);

  React.useEffect(() => {
    Promise.all([getPosition(3)])
      .then(([pos]) => {
        setQuality(pos);
      })
      .catch(console.log);
  }, []);

  return (
    <Grid container item { ...gridProperties }>
      <Typography component="h6" variant="h6">
        Выберите качества из списка
      </Typography>
      <FormGroup>
        {
          quality.length ? quality.map(pos => (
            <FormControlLabel
              control={<Checkbox />}
              key={pos[0]}
              label={pos[0]}
            />
          )) : null
        }
      </FormGroup>
      <Button type="submit" variant="contained" sx={{ mt: 2 }}>Отправить</Button>
    </Grid>
  );
};
