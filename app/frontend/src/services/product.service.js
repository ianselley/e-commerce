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
        let sellerProducts =
          JSON.parse(localStorage.getItem('sellerProducts')) || [];
        sellerProducts.push(response.data);
        localStorage.setItem('sellerProducts', JSON.stringify(sellerProducts));
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
    return axiosRequest(options, (response) => {
      let sellerProducts = JSON.parse(localStorage.getItem('sellerProducts'));
      const productListId = sellerProducts.findIndex(
        (product) => product.id == productId
      );
      sellerProducts[productListId].images = response.data;
      localStorage.setItem('sellerProducts', JSON.stringify(sellerProducts));
    });
  }

  getAllProducts() {
    const options = {
      endpoint: '/product/all',
      method: 'get',
    };
    return axiosRequest(options);
  }

  getSellerProducts(sellerId) {
    const options = {
      endpoint: '/user/seller',
      method: 'get',
      params: { seller_id: sellerId },
    };
    return axiosRequest(options, (response) => {
      const { products } = response.data;
      response.data = products;
    });
  }

  getProduct(productId) {
    const options = {
      endpoint: `/product/${productId}`,
      method: 'get',
    };
    return axiosRequest(options);
  }
}

export default new ProductService();
