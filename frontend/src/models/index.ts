export interface Credentials {
  username: string;
  password: string;
}

export interface Folder {
  id: number;
  name: string;
  descr: string;
  parent_id: number;
}

export interface Material {
  folder_id: number;
  folder_name: string;
  id: number;
  link: string;
  name: string;
}

export interface UserInfo {
  email: string;
  id: number;
  username: string;
  role: string;
}
