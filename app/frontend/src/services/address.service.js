import authHeader from './auth-header.js';
import axiosRequest from './axios.service.js';

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
        const address = Object.assign({}, response.data);
        let buyer = JSON.parse(localStorage.getItem('buyer'));
        buyer.main_address_id = address.buyer.main_address_id;
        delete address.buyer;
        buyer.addresses.push(address);
        localStorage.setItem('buyer', JSON.stringify(buyer));
      }
    });
  }
}

export default new AddressService();
