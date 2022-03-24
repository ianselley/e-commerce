import { useCookies } from 'vue3-cookies';

import authHeader from './auth-header.js';
import axiosRequest from './axios.service.js';

const { cookies } = useCookies();

class ProductService {
  registerProduct(product) {
    const options = {
      endpoint: '/product/create-product',
      method: 'post',
      headers: authHeader(),
      data: product,
    };
    return axiosRequest(options, (response) => {
      if (response.data) {
        const user = cookies.get('user');
        user.seller.products.push(response.data);
        cookies.set('user', user);
      }
    });
  }
  uploadImages(productId, images) {
    const bodyFormData = new FormData();
    bodyFormData.append('product_id', productId);
    for (let image of images) {
      bodyFormData.append('images', image);
    }
    const options = {
      endpoint: '/product/upload-images',
      method: 'post',
      headers: {
        ...authHeader(),
        'Content-Type': 'multipart/form-data',
      },
      data: bodyFormData,
    };
    return axiosRequest(options);
  }
}

export default new ProductService();
