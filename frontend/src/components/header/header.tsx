import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import LogoutIcon from '@mui/icons-material/Logout';
import { Button, Typography } from '@mui/material';
import { useAuth } from '@src/hooks';
import './header.less';

export const Header = (): React.ReactElement => {
  const navigate = useNavigate();
  const { pathname } = useLocation();
  const { onLogout, user } = useAuth();

  const handleClick = (path: string): void => {
    if (path !== pathname) navigate(path);
  };

  return (
    <header className="app-header">
      <Button onClick={() => handleClick('/main')}>Главная</Button>
      {user.role === 'hr' && <Button onClick={() => handleClick('/employees')}>Сотрудники</Button>}
      {user.role !== 'boss' && <Button onClick={() => handleClick('/materials')}>Материалы</Button>}
      <Button onClick={() => handleClick('/messages')}>Сообщения</Button>
      <Typography variant="body1" component="div" sx={{ flexGrow: 1, textAlign: 'right' }}>
        {user.username}
      </Typography>
      <Button color="secondary" startIcon={<LogoutIcon />} onClick={() => onLogout()}>Выход</Button>
    </header>
  )
}
