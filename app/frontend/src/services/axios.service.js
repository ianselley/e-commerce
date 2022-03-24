import axios from 'axios';

import { BASE_URL } from '@/config.json';

export default async function axiosRequest(options, callback) {
  if (options.endpoint) {
    options.url = BASE_URL + options.endpoint;
  }
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
