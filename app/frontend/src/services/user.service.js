import axios from 'axios';

import authHeader from './auth-header';
import { BASE_URL } from './config.json';

class UserService {
  getPublicContent() {
    return axios.get(BASE_URL + '/all');
  }
  getBuyer() {
    return axios.get(BASE_URL + '/buyer', { headers: authHeader() });
  }
  getSeller() {
    return axios.get(BASE_URL + '/seller', { headers: authHeader() });
  }
  getUser() {
    return axios.get(BASE_URL + '/user', { headers: authHeader() });
  }
}

export default new UserService();