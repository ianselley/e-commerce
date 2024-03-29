import authHeader from './auth-header.js';
import axiosRequest from './axios.service.js';

function findProductIndex(list, productId) {
  return list.findIndex((product) => product.id == productId);
}

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

  editProduct(product, productId) {
    const options = {
      endpoint: '/product',
      method: 'put',
      headers: authHeader(),
      data: { ...product, id: productId },
    };
    return axiosRequest(options, (response) => {
      if (response.data) {
        let sellerProducts = JSON.parse(localStorage.getItem('sellerProducts'));
        const productIndex = findProductIndex(sellerProducts, productId);
        sellerProducts[productIndex] = response.data;
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
      const productIndex = findProductIndex(sellerProducts, productId);
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
      const productIndex = findProductIndex(sellerProducts, productId);
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
      const productIndex = findProductIndex(sellerProducts, productId);
      sellerProducts[productIndex].images = sellerProducts[
        productIndex
      ].images.filter((image) => !imageIds.includes(image.id));
      localStorage.setItem('sellerProducts', JSON.stringify(sellerProducts));
    });
  }

  getSearchedProducts(search, page, productsPerPage) {
    const skip = (page - 1) * productsPerPage;
    const options = {
      endpoint: '/product/all',
      method: 'get',
      params: { substring: search, skip, limit: productsPerPage },
    };
    return axiosRequest(options);
  }

  getSellerProducts() {
    const options = {
      endpoint: '/user/seller',
      method: 'get',
      headers: authHeader(),
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
