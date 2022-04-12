import authHeader from './auth-header.js';
import axiosRequest from './axios.service.js';

class ProductService {
  registerProduct(product) {
    const options = {
      endpoint: '/product',
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
      endpoint: '/product/images',
      method: 'post',
      headers: {
        ...authHeader(),
        'Content-Type': 'multipart/form-data',
      },
      data: bodyFormData,
    };
    return axiosRequest(options, (response) => {
      let sellerProducts = JSON.parse(localStorage.getItem('sellerProducts'));
      const productIndex = sellerProducts.findIndex(
        (product) => product.id == productId
      );
      sellerProducts[productIndex].images = response.data;
      localStorage.setItem('sellerProducts', JSON.stringify(sellerProducts));
    });
  }

  changeProductAvailability(productId) {
    const options = {
      endpoint: '/product/availability',
      method: 'put',
      headers: authHeader(),
      params: { product_id: productId },
    };
    return axiosRequest(options, () => {
      let sellerProducts = JSON.parse(localStorage.getItem('sellerProducts'));
      const productIndex = sellerProducts.findIndex(
        (product) => product.id == productId
      );
      sellerProducts[productIndex].available =
        !sellerProducts[productIndex].available;
      localStorage.setItem('sellerProducts', JSON.stringify(sellerProducts));
    });
  }

  deleteImages(productId, imageIds) {
    const options = {
      endpoint: '/product/images',
      method: 'delete',
      headers: authHeader(),
      params: { product_id: productId, image_ids: imageIds },
    };
    return axiosRequest(options, () => {
      let sellerProducts = JSON.parse(localStorage.getItem('sellerProducts'));
      const productIndex = sellerProducts.findIndex(
        (product) => product.id == productId
      );
      sellerProducts[productIndex].images = sellerProducts[
        productIndex
      ].images.filter((image) => !imageIds.includes(image.id));
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
      endpoint: '/product',
      method: 'get',
      params: { product_id: productId },
    };
    return axiosRequest(options);
  }
}

export default new ProductService();
