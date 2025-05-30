// import router from '@/router'

const selectWidthSmall = 168
const selectWidth = 240
const selectWidthLarge = 360

const isLogin = () => {
  return localStorage.getItem('token') || ''
}

// const goLogin = () => {
//   router.push('/login')
// }

export { selectWidthSmall, selectWidthLarge, selectWidth, isLogin }
