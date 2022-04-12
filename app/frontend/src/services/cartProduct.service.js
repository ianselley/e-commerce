import axiosRequest from '@/services/axios.service.js';
import authHeader from '@/services/auth-header.js';

class CartProductService {
  addToCart(productId, quantity) {
    const options = {
      endpoint: '/cart-product',
      method: 'post',
      headers: authHeader(),
      params: { product_id: productId, quantity },
    };
    return axiosRequest(options, (response) => {
      const buyer = JSON.parse(localStorage.getItem('buyer'));
      buyer.shopping_cart.push(response.data);
      localStorage.setItem('buyer', JSON.stringify(buyer));
    });
  }
  removeFromCart(cartProductId) {
    const options = {
      endpoint: '/cart-product',
      method: 'delete',
      headers: authHeader(),
      params: { cart_product_id: cartProductId },
    };
    return axiosRequest(options, () => {
      let buyer = JSON.parse(localStorage.getItem('buyer'));
      buyer.shopping_cart = buyer.shopping_cart.filter(
        (cartProduct) => cartProduct.id != cartProductId
      );
      localStorage.setItem('buyer', JSON.stringify(buyer));
    });
  }
}

export default new CartProductService();
