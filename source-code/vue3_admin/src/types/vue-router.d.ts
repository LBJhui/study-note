import { _RouteRecordBase } from 'vue-router'

declare module 'vue-router' {
  interface RouteMeta {
    title: string
    fullPath: string
    icon?: string
    isNav: boolean
    keepalive: boolean
  }
}
