import React from 'react';
import { Outlet } from 'react-router-dom';
import { Header } from '@src/components';
import './container.less';

export const Container = (): JSX.Element => {
  return (
    <>
      <Header />
      <div className="app-container"><Outlet /></div>
    </>
  );
};
