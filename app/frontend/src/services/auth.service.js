import { useCookies } from 'vue3-cookies';

import authHeader from './auth-header.js';
import axiosRequest from './axios.service.js';

const { cookies } = useCookies();

function setUser(response) {
  const { seller, buyer, ...user } = response.data;
  if (seller) {
    const sellerProducts = seller.products;
    localStorage.setItem('seller', JSON.stringify(seller));
    localStorage.setItem('sellerProducts', JSON.stringify(sellerProducts));
  }
  if (buyer) {
    localStorage.setItem('buyer', JSON.stringify(buyer));
  }
  cookies.set('user', JSON.stringify(user));
}

class AuthService {
  login(user) {
    const options = {
      endpoint: '/user/login',
      method: 'post',
      data: user,
    };
    return axiosRequest(options, (response) => {
      if (response.data.access_token) {
        setUser(response);
      }
    });
  }

  getUser(userId) {
    const options = {
      endpoint: '/user',
      method: 'get',
      headers: authHeader(),
      params: { user_id: userId },
    };
    return axiosRequest(options, (response) => {
      if (response.data.access_token) {
        setUser(response);
      }
    });
  }

  logout() {
    cookies.remove('user');
    localStorage.clear();
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
        localStorage.setItem('buyer', JSON.stringify(response.data));
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
        localStorage.setItem('seller', JSON.stringify(response.data));
      }
    });
  }
}

export default new AuthService();
