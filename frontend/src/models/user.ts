export interface UserInfo {
  email: string;
  id: number;
  username: string;
  role: string;
}

export interface UserFile {
  date: string;
  id?: string;
  name: string;
  result?: string;
  size: number;
}
