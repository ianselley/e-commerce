import axios from 'axios';

import { API_URL } from '@/config.json';

export default function axiosRequest(options, callback) {
  if (options.endpoint) {
    options.url = API_URL + options.endpoint;
  }
  return axios(options)
    .then((response) => {
      typeof callback === 'function' && callback(response);
      return Promise.resolve(response.data);
    })
    .catch((error) => {
      if (!error.response) return Promise.reject(error);
      return Promise.reject(error.response.data.detail);
    });
}
