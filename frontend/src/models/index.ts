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

export interface Message {
  id: number;
  date: string;
  topic: string;
  is_completed: number;
  from_id: number;
  to_id: number;
  after_id: number;
  body: string;
  is_read: number;
}

export interface UserInfo {
  email: string;
  id: number;
  username: string;
  role: string;
}
