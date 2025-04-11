type PageInfo = {
  total: number
  currentPage: number
  pageSize: number
  selectedNum: number
}

// 定义选项的类型
interface Option {
  [key: string]: any // 动态键值对，可根据实际需求调整为更具体的类型
}

export type { PageInfo, Option }
