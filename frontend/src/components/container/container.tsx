import React from 'react';
import { Outlet } from 'react-router-dom';
import { Header } from '@src/components';
import './container.less';

export const Container = (): React.ReactElement => {
  return (
    <>
      <Header />
      <div className="app-container"><Outlet /></div>
    </>
  );
};
