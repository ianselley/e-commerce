import axiosRequest from '@/services/axios.service.js';
import authHeader from '@/services/auth-header.js';

class OrderService {
  orderProducts({ addressId, cartProductIds }) {
    const options = {
      endpoint: '/order',
      method: 'post',
      headers: authHeader(),
      params: { address_id: addressId, cart_product_ids: cartProductIds },
    };
    return axiosRequest(options, (response) => {
      let buyer = JSON.parse(localStorage.getItem('buyer'));
      const cartProductIdsList = cartProductIds.split(',');
      buyer.shopping_cart = buyer.shopping_cart.filter(
        (cartProduct) => !cartProductIdsList.includes(cartProduct.id.toString())
      );
      buyer.orders = buyer.orders.concat(response.data);
      localStorage.setItem('buyer', JSON.stringify(buyer));
    });
  }
  productArrives(orderId) {
    const options = {
      endpoint: '/order',
      method: 'put',
      headers: authHeader(),
      params: { order_id: orderId },
    };
    return axiosRequest(options, () => {
      let buyer = JSON.parse(localStorage.getItem('buyer'));
      const orderIndex = buyer.orders.findIndex((order) => order.id == orderId);
      buyer.orders[orderIndex].delivered = true;
      localStorage.setItem('buyer', JSON.stringify(buyer));
    });
  }
}

export default new OrderService();
