import axios, { AxiosError } from 'axios';
import Cookies from 'js-cookie';
import { Credentials, LoginInfo, LogoutInfo, UserInfo } from '@src/models';

type ApiError = { error: boolean; message: string; };

const api = axios.create({
  baseURL: 'http://185.221.152.242:5460/api',
  headers: { 'Content-Type': 'application/json' },
});

const token = Cookies.get('Authorization');
if (token && api.defaults.headers.common) api.defaults.headers.common['Authorization'] = `Bearer ${token}`;

export async function currentUser(): Promise<UserInfo> {
  try {
    const { data } = await api.get<UserInfo>('/users/current');
    return data;
  } catch (e) {
    throw new Error((e as AxiosError<ApiError>)?.response?.data?.message);
  }
}

export async function login(credentials: Credentials): Promise<LoginInfo> {
  try {
    const { data } = await api.post<LoginInfo>('/users/login', credentials);
    Cookies.set('Authorization', data.access_token, { expires: 1 });
    if (data.access_token && api.defaults.headers.common) api.defaults.headers.common['Authorization'] = `Bearer ${data.access_token}`;
    return data;
  } catch (e) {
    throw new Error((e as AxiosError<ApiError>)?.response?.data?.message);
  }
}

export async function logout(): Promise<LogoutInfo> {
  try {
    const { data } = await api.get<LogoutInfo>('/users/logout');
    Cookies.remove('Authorization');
    delete api.defaults.headers.common['Authorization'];
    return data;
  } catch (e) {
    throw new Error((e as AxiosError<ApiError>)?.response?.data?.message);
  }
}
