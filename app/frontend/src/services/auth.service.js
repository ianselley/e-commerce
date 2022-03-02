import { useCookies } from 'vue3-cookies';

import { BASE_URL } from '@/config.json';
import authHeader from './auth-header';
import axiosRequest from './axios.service';

const { cookies } = useCookies();

class AuthService {
  login(user) {
    const options = {
      url: BASE_URL + '/user/login',
      method: 'post',
      data: user,
    };
    return axiosRequest(options, (response) => {
      if (response.data.accessToken) {
        cookies.set('user', JSON.stringify(response.data));
      }
    });
  }

  logout() {
    cookies.remove('user');
  }

  register(user) {
    const options = {
      url: BASE_URL + '/user/signup',
      method: 'post',
      data: user,
    };
    return axiosRequest(options);
  }

  registerSeller(info) {
    const options = {
      url: BASE_URL + '/user/signup-seller',
      method: 'post',
      headers: authHeader(),
      data: info,
    };
    return axiosRequest(options, (response) => {
      if (response.data) {
        const user = cookies.get('user');
        user.seller = response.data;
        cookies.set('user', user);
      }
    });
  }
}

export default new AuthService();
