import React from 'react';
import { Navigate, Route, Routes } from 'react-router-dom';
import { Container, Login, Upload } from '@src/components';
import { useAuth } from '@src/hooks';

export const App = (): JSX.Element => {
  const { user } = useAuth();
  return user?.id && (
    <Routes>
      <Route element={user.id > -1 ? <Container /> : <Navigate to='/login' replace /> }>
        <Route path='/upload' element={<Upload />} />
      </Route>
      <Route path='/login' element={user.id > -1 ? <Navigate to='/upload' replace /> : <Login />} />
      <Route path='*' element={<Navigate to={user.id > -1 ? '/upload' : '/login'} replace />} />
    </Routes>
  );
};
