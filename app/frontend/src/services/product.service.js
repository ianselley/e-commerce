import authHeader from './auth-header.js';
import axiosRequest from './axios.service.js';

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
        let products = JSON.parse(localStorage.getItem('products'));
        if (!products) products = [];
        products.push(response.data);
        localStorage.setItem('products', JSON.stringify(products));
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
  getProducts() {
    const options = {
      endpoint: '/product/all',
      method: 'get',
    };
    return axiosRequest(options);
  }
}

export default new ProductService();
