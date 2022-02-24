import axios from 'axios';

import { BASE_URL } from '@/config.json';

class AuthService {
  async login(user) {
    const response = await axios.post(BASE_URL + '/user/login', {
      username: user.username,
      password: user.password,
    });
    if (response.data.accessToken) {
      localStorage.setItem('user', JSON.stringify(response.data));
    }
    return response.data;
  }

  logout() {
    localStorage.removeItem('user');
  }

  register(user) {
    return axios.post(BASE_URL + '/user/signup/test', {
      email: user.email,
      password: user.password,
      username: user.username,
    });
  }
}

export default new AuthService();
