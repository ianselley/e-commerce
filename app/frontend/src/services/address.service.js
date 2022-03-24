import { useCookies } from 'vue3-cookies';

import authHeader from './auth-header.js';
import axiosRequest from './axios.service.js';

const { cookies } = useCookies();

class AddressService {
  registerAddress(address) {
    address.zip_code = address.zipCode;
    delete address.zipCode;
    const options = {
      endpoint: '/address/register',
      method: 'post',
      headers: authHeader(),
      data: address,
    };
    return axiosRequest(options, (response) => {
      if (response.data) {
        console.log(cookies);
        const user = cookies.get('user');
        user.buyer.addresses.push(response.data);
        if (!user.buyer.main_address_id) {
          user.buyer.main_address_id = response.data.buyer.main_address_id;
        }
        cookies.set('user', user);
      }
    });
  }
}

export default new AddressService();
