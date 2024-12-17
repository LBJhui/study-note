// import router from '@/router'

const isLogin = () => {
  return localStorage.getItem('token') || ''
}

// const goLogin = () => {
//   router.push('/login')
// }

export { isLogin, goLogin }
