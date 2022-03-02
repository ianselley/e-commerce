import { useCookies } from 'vue3-cookies';

const { cookies } = useCookies();

export default function authHeader() {
  let user = cookies.get('user');
  if (!user || !user.accessToken) return {};
  return { Authorization: 'Bearer ' + user.accessToken };
}
