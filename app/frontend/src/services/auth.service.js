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

  getUser() {
    const options = {
      endpoint: '/user',
      method: 'get',
      headers: authHeader(),
    };
    return axiosRequest(options, (response) => {
      if (response.data.access_token) {
        setUser(response);
      }
    });
  }

  editUser(user) {
    const options = {
      endpoint: '/user',
      method: 'put',
      headers: authHeader(),
      data: user,
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
      endpoint: '/user',
      method: 'post',
      data: user,
    };
    return axiosRequest(options);
  }

  registerBuyer(name) {
    const options = {
      endpoint: '/user/buyer',
      method: 'post',
      headers: authHeader(),
      data: { name },
    };
    return axiosRequest(options, (response) => {
      if (response.data) {
        localStorage.setItem('buyer', JSON.stringify(response.data));
      }
    });
  }

  editName(name) {
    const options = {
      endpoint: '/user/buyer',
      method: 'put',
      headers: authHeader(),
      data: { name },
    };
    return axiosRequest(options, (response) => {
      if (response.data) {
        localStorage.setItem('buyer', JSON.stringify(response.data));
      }
    });
  }

  registerSeller(brand) {
    const options = {
      endpoint: '/user/seller',
      method: 'post',
      headers: authHeader(),
      data: { brand },
    };
    return axiosRequest(options, (response) => {
      if (response.data) {
        localStorage.setItem('seller', JSON.stringify(response.data));
      }
    });
  }

  editBrand(brand) {
    const options = {
      endpoint: '/user/seller',
      method: 'put',
      headers: authHeader(),
      data: { brand },
    };
    return axiosRequest(options, (response) => {
      if (response.data) {
        localStorage.setItem('seller', JSON.stringify(response.data));
      }
    });
  }
}

export default new AuthService();
