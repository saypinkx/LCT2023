export interface Credentials {
  username: string;
  password: string;
}

export interface LoginInfo {
  access_token: string;
  user_role: string;
}

export interface LogoutInfo {
  ok: boolean;
}
