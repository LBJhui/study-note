// import router from '@/router'
import type { PageInfo } from '@/types/index'

const selectWidthSmall = 168
const selectWidth = 240
const selectWidthLarge = 360

const isLogin = () => {
  return localStorage.getItem('token') || ''
}

// const goLogin = () => {
//   router.push('/login')
// }

const getYearMonthDay = (date: Date) => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  return {
    year,
    month,
    day,
  }
}

export { selectWidthSmall, selectWidthLarge, selectWidth, isLogin, getYearMonthDay }
