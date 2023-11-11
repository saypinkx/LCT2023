import React from 'react';
import { Navigate, Route, Routes } from 'react-router-dom';
import { Container, Employees, Login, Main, Materials, Messages, UserMain } from '@src/components';
import { useAuth } from '@src/hooks';

export const App = (): React.ReactElement => {
  const { user } = useAuth();
  return user?.id && (
    <Routes>
      <Route element={user.id > -1 ? <Container /> : <Navigate to='/login' replace /> }>
        <Route path='/main' element={user.role === 'hr' ? <Main /> : <UserMain />} />
        <Route path='/employees' element={user.role === 'hr' ? <Employees /> : <Navigate to='/main' replace />} />
        <Route path='/materials' element={user.role === 'boss' ? <Navigate to='/main' replace /> : <Materials />} />
        <Route path='/messages' element={<Messages />} />
      </Route>
      <Route path='/login' element={user.id > -1 ? <Navigate to='/main' replace /> : <Login />} />
      <Route path='*' element={<Navigate to={user.id > -1 ? '/main' : '/login'} replace />} />
    </Routes>
  );
};
