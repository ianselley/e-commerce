import axios from 'axios';

export default async function axiosRequest(options, callback) {
  return await axios(options)
    .then((response) => {
      typeof callback === 'function' && callback(response);
      return Promise.resolve(response.data);
    })
    .catch((error) => {
      if (!error.response) return Promise.reject(error);
      return Promise.reject(error.response.data.detail);
    });
}
