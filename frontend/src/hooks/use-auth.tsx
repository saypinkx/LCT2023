import React, { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { currentUser, login, logout } from '@src/api';
import { Credentials, UserInfo } from '@src/models';

interface Context {
  error: string;
  onLogin: (credentials: Credentials) => Promise<void>;
  onLogout: () => Promise<void>;
  user: UserInfo;
}

const AuthContext = createContext({} as Context);

export const AuthProvider = ({ children }: React.PropsWithChildren): React.ReactElement => {
  const navigate = useNavigate();
  const [error, setError] = useState<string>('');
  const [user, setUser] = useState<UserInfo>({} as UserInfo);

  const getUser = useCallback(async () => {
    try {
      setUser(await currentUser());
    } catch (err) {
      setUser({ email: '', id: -1, role: '', username: '' });
      navigate('/login', { replace: true });
    }
  }, []);

  const onLogin = async (credentials: Credentials): Promise<void> => {
    try {
      await login(credentials);
      setUser(await currentUser());
      setError('');
      navigate('/upload', { replace: true });
    } catch(e) {
      setError(e?.message || 'Произошла неизвестная ошибка');
    }
  };

  const onLogout = async (): Promise<void> => {
    await logout();
    setUser({ email: '', id: -1, role: '', username: '' });
    navigate('/login', { replace: true });
  };

  const value = useMemo(() => ({ error, onLogin, onLogout, user }), [error, user]);

  useEffect(() => {
    getUser();
  }, [getUser]);

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  return useContext(AuthContext);
};
