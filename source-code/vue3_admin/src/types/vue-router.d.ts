import { _RouteRecordBase } from 'vue-router'

declare module 'vue-router' {
  interface _RouteRecordBase {
    title: string
    fullPath: string
    icon?: string
    isNav?: boolean
    keepalive: boolean
  }
}
