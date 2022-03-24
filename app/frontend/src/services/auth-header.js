import { useCookies } from 'vue3-cookies';

const { cookies } = useCookies();

export default function authHeader() {
  let user = cookies.get('user');
  if (!user || !user.access_token) return {};
  return {
    Accept: 'application/json',
    Authorization: 'Bearer ' + user.access_token,
  };
}
