interface userInfoInterface {
  id: string
  userName: string
  phone: string
  Ncoin: number
  password: string
  avatar: string
  loginTime: Date
  autoLogin: boolean
  rememberPassword: boolean
}

interface userInfoRes {
  code?: number
  refresh: string
  token: string
  user_info: userInfoInterface
}

interface CouponList {
  id: string
  couponName: string
  expiration: string
  price: number
  status: number
  isUsing: number
}

interface CouponEnu {
  id: string
  couponName: string
  expiration: string
  price: number
}

export { userInfoInterface, userInfoRes, CouponList, CouponEnu }
