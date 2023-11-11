import React, { useEffect, useState } from 'react';
import { Card, CardContent, Grid, Tab, Tabs, Typography } from '@mui/material';
import { getMessages } from '@src/api';
import { useAuth } from '@src/hooks';
import { Message } from '@src/models';
import { gridProperties } from '@src/utils';
import './messages.less';

export const Messages = (): React.ReactElement => {
  const { user } = useAuth();
  const [incoming, setIncoming] = useState<Message[] | null>(null);
  const [sent, setSent] = useState<Message[] | null>(null);
  const [value, setValue] = useState(0);

  useEffect(() => {
    Promise.all([getMessages('incoming', user.id), getMessages('sent', user.id)])
      .then(([inc, st]) => {
        setIncoming(inc);
        setSent(st);
      })
      .catch(console.log);
  }, []);

  return (
    <Grid container item { ...gridProperties }>
      <Tabs value={value} onChange={(_, val) => setValue(val)} aria-label="basic tabs">
        <Tab label="Входящие" aria-controls="simple-tabpanel-0" id="simple-tab-0" />
        <Tab label="Исходящие" aria-controls="simple-tabpanel-1" id="simple-tab-1" />
      </Tabs>
      <div aria-labelledby="simple-tab-0" id="simple-tabpanel-0" hidden={value !== 0} role="tabpanel" style={{ width: '100%' }}>
        {value === 0 && incoming && !incoming.length && (
          <Typography sx={{ marginTop: 1 }}>Нет входящих сообщений</Typography>
        )}
        {value === 0 && incoming?.length ? (
          incoming.map(item => (
            <Card key={item.id} sx={{ mt: 2, textAlign: 'left' }}>
              <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                  {new Date(item.date).toLocaleString() + ', от пользователя с id ' + item.from_id}
                </Typography>
                <Typography variant="h5" component="div">
                  {item.body}
                </Typography>
              </CardContent>
            </Card>
          ))
        ) : null}
      </div>
      <div aria-labelledby="simple-tab-1" id="simple-tabpanel-1" hidden={value !== 1} role="tabpanel" style={{ width: '100%' }}>
        {value === 1 && sent && !sent.length && (
          <Typography sx={{ marginTop: 1 }}>Нет исходящих сообщений</Typography>
        )}
        {value === 1 && sent?.length ? (
          sent.map(item => (
            <Card key={item.id} sx={{ mt: 2, textAlign: 'left' }}>
              <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                  {new Date(item.date).toLocaleString() + ', пользователю с id ' + item.to_id}
                </Typography>
                <Typography variant="h5" component="div">
                  {item.body}
                </Typography>
              </CardContent>
            </Card>
          ))
        ) : null}
      </div>
    </Grid>
  );
};
