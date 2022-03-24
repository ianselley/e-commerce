import { useCookies } from 'vue3-cookies';

import authHeader from './auth-header.js';
import axiosRequest from './axios.service.js';

const { cookies } = useCookies();

class AuthService {
  login(user) {
    const options = {
      endpoint: '/user/login',
      method: 'post',
      data: user,
    };
    return axiosRequest(options, (response) => {
      if (response.data.access_token) {
        cookies.set('user', JSON.stringify(response.data));
      }
    });
  }

  logout() {
    cookies.remove('user');
  }

  register(user) {
    const options = {
      endpoint: '/user/signup',
      method: 'post',
      data: user,
    };
    return axiosRequest(options);
  }

  registerBuyer(buyer) {
    const options = {
      endpoint: '/user/signup-buyer',
      method: 'post',
      headers: authHeader(),
      data: buyer,
    };
    return axiosRequest(options, (response) => {
      if (response.data) {
        const user = cookies.get('user');
        user.buyer = response.data;
        cookies.set('user', user);
      }
    });
  }

  registerSeller(info) {
    const options = {
      endpoint: '/user/signup-seller',
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
