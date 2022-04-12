import authHeader from './auth-header.js';
import axiosRequest from './axios.service.js';

class AddressService {
  registerAddress(address) {
    address.zip_code = address.zipCode;
    delete address.zipCode;
    const options = {
      endpoint: '/address',
      method: 'post',
      headers: authHeader(),
      data: address,
    };
    return axiosRequest(options, (response) => {
      if (response.data) {
        const address = Object.assign({}, response.data);
        const buyer = JSON.parse(localStorage.getItem('buyer'));
        buyer.main_address_id = address.buyer.main_address_id;
        delete address.buyer;
        buyer.addresses.push(address);
        localStorage.setItem('buyer', JSON.stringify(buyer));
      }
    });
  }

  editAddress(address, addressId) {
    address.zip_code = address.zipCode;
    delete address.zipCode;
    const options = {
      endpoint: '/address',
      method: 'put',
      headers: authHeader(),
      data: { ...address, id: addressId },
    };
    return axiosRequest(options, (response) => {
      if (response.data) {
        const address = Object.assign({}, response.data);
        const buyer = JSON.parse(localStorage.getItem('buyer'));
        buyer.main_address_id = address.buyer.main_address_id;
        delete address.buyer;
        const addressIndex = buyer.addresses.findIndex(
          (address) => address.id == addressId
        );
        buyer.addresses[addressIndex] = address;
        localStorage.setItem('buyer', JSON.stringify(buyer));
      }
    });
  }

  makeItMainAddress(addressId) {
    const options = {
      endpoint: '/address/main_address_id',
      method: 'put',
      headers: authHeader(),
      params: { address_id: addressId },
    };
    return axiosRequest(options, () => {
      const buyer = JSON.parse(localStorage.getItem('buyer'));
      buyer.main_address_id = addressId;
      localStorage.setItem('buyer', JSON.stringify(buyer));
    });
  }

  deleteAddress(addressId) {
    const options = {
      endpoint: '/address',
      method: 'delete',
      headers: authHeader(),
      params: { address_id: addressId },
    };
    return axiosRequest(options, () => {
      const buyer = JSON.parse(localStorage.getItem('buyer'));
      if (buyer.main_address_id == addressId) {
        buyer.main_address_id = null;
      }
      buyer.addresses = buyer.addresses.filter(
        (address) => address.id != addressId
      );
      localStorage.setItem('buyer', JSON.stringify(buyer));
    });
  }
}

export default new AddressService();
