type DialogFormDate = {
  party: string
  userName: string
  mobilePhone: string
  email: string
  telephone: string
  IDType: string
  IDNumber: string
  userStatus: string
  isAddToContact: string
  contactType: string[]
  comment: string
  role: string[]
  product: string[]
}

type TableDataItem = {
  userAccount: string
  userName: string
  party: string
  role: string[]
  userStatus: string
  email: string
  telephone: string
  IDType: string
  IDNumber: string
  comment: string
} & DialogFormDate

export type { TableDataItem, DialogFormDate }
