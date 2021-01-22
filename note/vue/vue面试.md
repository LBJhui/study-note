# v-if 和 v-for 哪个优先级更高？如果两个同时出现，应该怎么优化得到更好的性能？

源码中找答案 `compiler/codegen/index.js`

```javascript
export function genElement(el: ASTElement, state: CodegenState): string {
  if (el.parent) {
    el.pre = el.pre || el.parent.pre
  }

  if (el.staticRoot && !el.staticProcessed) {
    return genStatic(el, state)
  } else if (el.once && !el.onceProcessed) {
    return genOnce(el, state)
  } else if (el.for && !el.forProcessed) {
    return genFor(el, state)
  } else if (el.if && !el.ifProcessed) {
    return genIf(el, state)
  } else if (el.tag === 'template' && !el.slotTarget && !state.pre) {
    return genChildren(el, state) || 'void 0'
  } else if (el.tag === 'slot') {
    return genSlot(el, state)
  } else {
    // component or element
    let code
    if (el.component) {
      code = genComponent(el.component, el, state)
    } else {
      let data
      if (!el.plain || (el.pre && state.maybeComponent(el))) {
        data = genData(el, state)
      }

      const children = el.inlineTemplate ? null : genChildren(el, state, true)
      code = `_c('${el.tag}'${
        data ? `,${data}` : '' // data
      }${
        children ? `,${children}` : '' // children
      })`
    }
    // module transforms
    for (let i = 0; i < state.transforms.length; i++) {
      code = state.transforms[i](el, code)
    }
    return code
  }
}
```

```vue
<template>
  <div>
    <h1>v-for 和 v-if 谁的优先级高？应该如何正确使用避免性能问题？</h1>
    <p v-for="child in children" v-if="isFolder">{{ child.title }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      children: [
        {
          title: 'LBJhui',
        },
        {
          title: 'foo',
        },
      ],
      isFolder: true,
    }
  },
}
</script>
```

**结论：**

1.显然 v-for 优先于 v-if 被解析 2.如果同时出现，每次渲染都会先执行循环再判断条件，无论如何循环都不可避免，浪费了性能
3..要避免出现这种情况，则在外层嵌套 template，在这一层进行 v-if 判断，然后在内部进行 v-for 循环

# Vue 组件 data 为什么必须是个函数，而 Vue 的根实例则没有此限制？

源码中找答案 `src/core/instance/state.js - initData() `

函数每次执行都会返回全新 data 对象实例

```javascript
function initData(vm: Component) {
  let data = vm.$options.data

  // 如果data是函数，则执行之并将其结果作为data选项的值
  data = vm._data = typeof data === 'function' ? getData(data, vm) : data || {}
  if (!isPlainObject(data)) {
    data = {}
    process.env.NODE_ENV !== 'production' &&
      warn(
        'data functions should return an object:\n' +
          'https://vuejs.org/v2/guide/components.html#data-Must-Be-a-Function',
        vm
      )
  }
  // proxy data on instance
  const keys = Object.keys(data)
  const props = vm.$options.props
  const methods = vm.$options.methods
  let i = keys.length
  while (i--) {
    const key = keys[i]
    if (process.env.NODE_ENV !== 'production') {
      if (methods && hasOwn(methods, key)) {
        warn(`Method "${key}" has already been defined as a data property.`, vm)
      }
    }
    if (props && hasOwn(props, key)) {
      process.env.NODE_ENV !== 'production' &&
        warn(
          `The data property "${key}" is already declared as a prop. ` +
            `Use prop default value instead.`,
          vm
        )
    } else if (!isReserved(key)) {
      proxy(vm, `_data`, key)
    }
  }
  // observe data
  observe(data, true /* asRootData */)
}
```

```javascript
export function initMixin(Vue: Class<Component>) {
  Vue.prototype._init = function (options?: Object) {
    const vm: Component = this
    // a uid
    vm._uid = uid++

    let startTag, endTag
    /* istanbul ignore if */
    if (process.env.NODE_ENV !== 'production' && config.performance && mark) {
      startTag = `vue-perf-start:${vm._uid}`
      endTag = `vue-perf-end:${vm._uid}`
      mark(startTag)
    }

    // a flag to avoid this being observed
    vm._isVue = true

    // 合并选项
    // merge options
    if (options && options._isComponent) {
      // optimize internal component instantiation
      // since dynamic options merging is pretty slow, and none of the
      // internal component options needs special treatment.
      initInternalComponent(vm, options)
    } else {
      vm.$options = mergeOptions(
        resolveConstructorOptions(vm.constructor),
        options || {},
        vm
      )
    }
    /* istanbul ignore else */
    if (process.env.NODE_ENV !== 'production') {
      initProxy(vm)
    } else {
      vm._renderProxy = vm
    }
    // expose real self
    vm._self = vm
    initLifecycle(vm)
    initEvents(vm)
    initRender(vm)
    callHook(vm, 'beforeCreate')
    initInjections(vm) // resolve injections before data/props
    initState(vm)
    initProvide(vm) // resolve provide after data/props
    callHook(vm, 'created')

    /* istanbul ignore if */
    if (process.env.NODE_ENV !== 'production' && config.performance && mark) {
      vm._name = formatComponentName(vm, false)
      mark(endTag)
      measure(`vue ${vm._name} init`, startTag, endTag)
    }

    if (vm.$options.el) {
      vm.$mount(vm.$options.el)
    }
  }
}
```

**结论**

Vue 组件可能存在多个实例，如果使用对象形式定义 data，则会导致它们共用一个 data 对象，那么状态变更将会影响所有组件实例，这是不合理的；采用函数形式定义，在 initData 时会将其作为工厂函数返回全新 data 对象，有效规避多实例之间状态污染问题。而在 Vue 根实例创建过程中则不存在该限制，也是因为根实例只能有一个，不需要担心这种情况。

# 你知道 vue 中 key 的作用和工作原理吗？说说你对它的理解

源码中找答案 `src/core/vdom/patch.js - updateChildren()

```javascript
function updateChildren(
  parentElm,
  oldCh,
  newCh,
  insertedVnodeQueue,
  removeOnly
) {
  let oldStartIdx = 0
  let newStartIdx = 0
  let oldEndIdx = oldCh.length - 1
  let oldStartVnode = oldCh[0]
  let oldEndVnode = oldCh[oldEndIdx]
  let newEndIdx = newCh.length - 1
  let newStartVnode = newCh[0]
  let newEndVnode = newCh[newEndIdx]
  let oldKeyToIdx, idxInOld, vnodeToMove, refElm

  // removeOnly is a special flag used only by <transition-group>
  // to ensure removed elements stay in correct relative positions
  // during leaving transitions
  const canMove = !removeOnly

  if (process.env.NODE_ENV !== 'production') {
    checkDuplicateKeys(newCh)
  }

  // 循环条件：开始索引不能大于结束索引
  while (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) {
    // 头尾指针调整
    if (isUndef(oldStartVnode)) {
      oldStartVnode = oldCh[++oldStartIdx] // Vnode has been moved left
    } else if (isUndef(oldEndVnode)) {
      oldEndVnode = oldCh[--oldEndIdx]
      // 接下来是头尾比较4种情况
    } else if (sameVnode(oldStartVnode, newStartVnode)) {
      // 两个开头相同
      patchVnode(
        oldStartVnode,
        newStartVnode,
        insertedVnodeQueue,
        newCh,
        newStartIdx
      )
      // 索引向后移动一位
      oldStartVnode = oldCh[++oldStartIdx]
      newStartVnode = newCh[++newStartIdx]
    } else if (sameVnode(oldEndVnode, newEndVnode)) {
      patchVnode(oldEndVnode, newEndVnode, insertedVnodeQueue, newCh, newEndIdx)
      oldEndVnode = oldCh[--oldEndIdx]
      newEndVnode = newCh[--newEndIdx]
    } else if (sameVnode(oldStartVnode, newEndVnode)) {
      // Vnode moved right
      patchVnode(
        oldStartVnode,
        newEndVnode,
        insertedVnodeQueue,
        newCh,
        newEndIdx
      )
      canMove &&
        nodeOps.insertBefore(
          parentElm,
          oldStartVnode.elm,
          nodeOps.nextSibling(oldEndVnode.elm)
        )
      oldStartVnode = oldCh[++oldStartIdx]
      newEndVnode = newCh[--newEndIdx]
    } else if (sameVnode(oldEndVnode, newStartVnode)) {
      // Vnode moved left
      patchVnode(
        oldEndVnode,
        newStartVnode,
        insertedVnodeQueue,
        newCh,
        newStartIdx
      )
      canMove &&
        nodeOps.insertBefore(parentElm, oldEndVnode.elm, oldStartVnode.elm)
      oldEndVnode = oldCh[--oldEndIdx]
      newStartVnode = newCh[++newStartIdx]
    } else {
      if (isUndef(oldKeyToIdx))
        oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx)
      idxInOld = isDef(newStartVnode.key)
        ? oldKeyToIdx[newStartVnode.key]
        : findIdxInOld(newStartVnode, oldCh, oldStartIdx, oldEndIdx)
      if (isUndef(idxInOld)) {
        // New element
        createElm(
          newStartVnode,
          insertedVnodeQueue,
          parentElm,
          oldStartVnode.elm,
          false,
          newCh,
          newStartIdx
        )
      } else {
        vnodeToMove = oldCh[idxInOld]
        if (sameVnode(vnodeToMove, newStartVnode)) {
          patchVnode(
            vnodeToMove,
            newStartVnode,
            insertedVnodeQueue,
            newCh,
            newStartIdx
          )
          oldCh[idxInOld] = undefined
          canMove &&
            nodeOps.insertBefore(parentElm, vnodeToMove.elm, oldStartVnode.elm)
        } else {
          // same key but different element. treat as new element
          createElm(
            newStartVnode,
            insertedVnodeQueue,
            parentElm,
            oldStartVnode.elm,
            false,
            newCh,
            newStartIdx
          )
        }
      }
      newStartVnode = newCh[++newStartIdx]
    }
  }

  // 整理工作：必定有数组还剩下的元素未处理
  if (oldStartIdx > oldEndIdx) {
    // 老的结束了，这种情况说明新的数组里还有剩下的节点
    refElm = isUndef(newCh[newEndIdx + 1]) ? null : newCh[newEndIdx + 1].elm
    addVnodes(
      parentElm,
      refElm,
      newCh,
      newStartIdx,
      newEndIdx,
      insertedVnodeQueue
    )
  } else if (newStartIdx > newEndIdx) {
    // 新的结束了，此时删除老数组中剩下的即可
    removeVnodes(oldCh, oldStartIdx, oldEndIdx)
  }
}
```

**结论**

1. key 的作用主要是为了高效的更新虚拟 DOM，其原理是 vue 在 patch 过程中通过 key 可以精准判断两个节点是否是同一个，从而避免频繁更新不同元素，使得整个 patch 过程更加高效，减少 DOM 操作量， 提高性能。
2. 另外，若不设置 key 还可能在列表更新时引发一些隐藏的 bug
3. vue 中使用相同标签名元素的过渡切换时，也会使用到 key 属性，其目的也是为了让 vue 可以区分它们，否则 vue 只会替换其内部属性而不会出发过渡效果。

# 你怎么理解 vue 中的 diff 算法

源码分析1:必要性，`lifecycle.js-mmoountComponent()`

​	组件中，可能存在很多个 data 中的 key 使用

源码分析2:执行方式，`patch.js-patchVnode()`

​	patchVnode 是diff 发生的地方，整体策略：深度优先，同层比较

源码分析3:高效性，`patch.js-updateChildren()`

```javascript
let updateComponent
/* istanbul ignore if */
if (process.env.NODE_ENV !== 'production' && config.performance && mark) {
  // 用户 $mount() 时，定义updateComponent
  updateComponent = () => {
    const name = vm._name
    const id = vm._uid
    const startTag = `vue-perf-start:${id}`
    const endTag = `vue-perf-end:${id}`

    mark(startTag)
    const vnode = vm._render()
    mark(endTag)
    measure(`vue ${name} render`, startTag, endTag)

    mark(startTag)
    vm._update(vnode, hydrating)
    mark(endTag)
    measure(`vue ${name} patch`, startTag, endTag)
  }
} else {
  updateComponent = () => {
    vm._update(vm._render(), hydrating)
  }
}
```

```javascript
function patchVnode (
oldVnode,
 vnode,
 insertedVnodeQueue,
 ownerArray,
 index,
 removeOnly
) {
  if (oldVnode === vnode) {
    return
  }

  if (isDef(vnode.elm) && isDef(ownerArray)) {
    // clone reused vnode
    vnode = ownerArray[index] = cloneVNode(vnode)
  }

  const elm = vnode.elm = oldVnode.elm

  if (isTrue(oldVnode.isAsyncPlaceholder)) {
    if (isDef(vnode.asyncFactory.resolved)) {
      hydrate(oldVnode.elm, vnode, insertedVnodeQueue)
    } else {
      vnode.isAsyncPlaceholder = true
    }
    return
  }

  // reuse element for static trees.
  // note we only do this if the vnode is cloned -
  // if the new node is not cloned it means the render functions have been
  // reset by the hot-reload-api and we need to do a proper re-render.
  if (isTrue(vnode.isStatic) &&
      isTrue(oldVnode.isStatic) &&
      vnode.key === oldVnode.key &&
      (isTrue(vnode.isCloned) || isTrue(vnode.isOnce))
     ) {
    vnode.componentInstance = oldVnode.componentInstance
    return
  }
	// 执行一些组件钩子
  let i
  const data = vnode.data
  if (isDef(data) && isDef(i = data.hook) && isDef(i = i.prepatch)) {
    i(oldVnode, vnode)
  }

  // 查找新旧节点是否存在孩子
  const oldCh = oldVnode.children
  const ch = vnode.children
  
  // 属性更新 
  if (isDef(data) && isPatchable(vnode)) {
    for (i = 0; i < cbs.update.length; ++i) cbs.update[i](oldVnode, vnode)
    if (isDef(i = data.hook) && isDef(i = i.update)) i(oldVnode, vnode)
  }
  // 判断是否元素
  if (isUndef(vnode.text)) {
    // 双方都有孩子
    if (isDef(oldCh) && isDef(ch)) {
      // 比孩子，reorder
      // 递归
      if (oldCh !== ch) updateChildren(elm, oldCh, ch, insertedVnodeQueue, removeOnly)
    } else if (isDef(ch)) {
      // 新节点有孩子
      if (process.env.NODE_ENV !== 'production') {
        checkDuplicateKeys(ch)
      }
      // 清空老节点文本
      if (isDef(oldVnode.text)) nodeOps.setTextContent(elm, '')
      // 创建孩子并追加
      addVnodes(elm, null, ch, 0, ch.length - 1, insertedVnodeQueue)
    } else if (isDef(oldCh)) {
      // 老节点有孩子，删除即可
      removeVnodes(oldCh, 0, oldCh.length - 1)
    } else if (isDef(oldVnode.text)) {
      // 老节点存在文本，清空
      nodeOps.setTextContent(elm, '')
    }
  } else if (oldVnode.text !== vnode.text) {
    // 双方都是文本节点，更新文本
    nodeOps.setTextContent(elm, vnode.text)
  }
  if (isDef(data)) {
    if (isDef(i = data.hook) && isDef(i = i.postpatch)) i(oldVnode, vnode)
  }
}
```

```javascript
function updateChildren (parentElm, oldCh, newCh, insertedVnodeQueue, removeOnly) {
  let oldStartIdx = 0
  let newStartIdx = 0
  let oldEndIdx = oldCh.length - 1
  let oldStartVnode = oldCh[0]
  let oldEndVnode = oldCh[oldEndIdx]
  let newEndIdx = newCh.length - 1
  let newStartVnode = newCh[0]
  let newEndVnode = newCh[newEndIdx]
  let oldKeyToIdx, idxInOld, vnodeToMove, refElm

  // removeOnly is a special flag used only by <transition-group>
  // to ensure removed elements stay in correct relative positions
  // during leaving transitions
  const canMove = !removeOnly

  if (process.env.NODE_ENV !== 'production') {
    checkDuplicateKeys(newCh)
  }

  // 循环条件：开始索引不能大于结束索引
  while (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) {
    // 头尾指针调整
    if (isUndef(oldStartVnode)) {
      oldStartVnode = oldCh[++oldStartIdx] // Vnode has been moved left
    } else if (isUndef(oldEndVnode)) {
      oldEndVnode = oldCh[--oldEndIdx]
      // 接下来是头尾比较4种情况
    } else if (sameVnode(oldStartVnode, newStartVnode)) {
      // 两个开头相同
      patchVnode(oldStartVnode, newStartVnode, insertedVnodeQueue, newCh, newStartIdx)
      //索引向后移动一位
      oldStartVnode = oldCh[++oldStartIdx]
      newStartVnode = newCh[++newStartIdx]
    } else if (sameVnode(oldEndVnode, newEndVnode)) {
      patchVnode(oldEndVnode, newEndVnode, insertedVnodeQueue, newCh, newEndIdx)
      oldEndVnode = oldCh[--oldEndIdx]
      newEndVnode = newCh[--newEndIdx]
    } else if (sameVnode(oldStartVnode, newEndVnode)) { // Vnode moved right
      // 老的开始和新的结束相同，除了打补丁之外还要移动到队尾
      patchVnode(oldStartVnode, newEndVnode, insertedVnodeQueue, newCh, newEndIdx)
      canMove && nodeOps.insertBefore(parentElm, oldStartVnode.elm, nodeOps.nextSibling(oldEndVnode.elm))
      oldStartVnode = oldCh[++oldStartIdx]
      newEndVnode = newCh[--newEndIdx]
    } else if (sameVnode(oldEndVnode, newStartVnode)) { // Vnode moved left
      patchVnode(oldEndVnode, newStartVnode, insertedVnodeQueue, newCh, newStartIdx)
      canMove && nodeOps.insertBefore(parentElm, oldEndVnode.elm, oldStartVnode.elm)
      oldEndVnode = oldCh[--oldEndIdx]
      newStartVnode = newCh[++newStartIdx]
    } else {
      
      // 4种猜想之后没有找到相同的，不得不开始循环查找
      if (isUndef(oldKeyToIdx)) oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx)
      // 查找在老的孩子数组中的索引
      idxInOld = isDef(newStartVnode.key)
        ? oldKeyToIdx[newStartVnode.key]
      : findIdxInOld(newStartVnode, oldCh, oldStartIdx, oldEndIdx)
      if (isUndef(idxInOld)) { // New element
        // 没找到则创建新元素
        createElm(newStartVnode, insertedVnodeQueue, parentElm, oldStartVnode.elm, false, newCh, newStartIdx)
      } else {
        // 找到除了打补丁，还要移动到队尾
        vnodeToMove = oldCh[idxInOld]
        if (sameVnode(vnodeToMove, newStartVnode)) {
          patchVnode(vnodeToMove, newStartVnode, insertedVnodeQueue, newCh, newStartIdx)
          oldCh[idxInOld] = undefined
          canMove && nodeOps.insertBefore(parentElm, vnodeToMove.elm, oldStartVnode.elm)
        } else {
          // same key but different element. treat as new element
          createElm(newStartVnode, insertedVnodeQueue, parentElm, oldStartVnode.elm, false, newCh, newStartIdx)
        }
      }
      newStartVnode = newCh[++newStartIdx]
    }
  }
  
  // 整理工作：必定有数组还剩下的元素未处理
  if (oldStartIdx > oldEndIdx) {
    // 老的结束了，这种情况说明新的数组里还剩下的节点
    refElm = isUndef(newCh[newEndIdx + 1]) ? null : newCh[newEndIdx + 1].elm
    addVnodes(parentElm, refElm, newCh, newStartIdx, newEndIdx, insertedVnodeQueue)
  } else if (newStartIdx > newEndIdx) {
    // 新的结束了，此时删除老数组中剩下的即可
    removeVnodes(oldCh, oldStartIdx, oldEndIdx)
  }
}
```

**总结**

1. diff 算法是虚拟 DOM 技术的必要产物：通过新旧虚拟 DOM 做对比（即 diff ），将变化的地方更新在真实 DOM 上；另外，也需要 diff 高效的执行对比过程，从而降低时间复杂度为 O(n)。
2. vue 2.x 中为了降低 watcher 粒度，每个组件只有一个 watcher 与之对应，只有引入 diff 才能精确找到发生变化的地方。
3. vue 中 diff 执行的时刻是组件实例执行其更新函数时，它会比对上一次渲染结果 oldVnode 和新的渲染结果 newVnode，此过程称为 patch。
4. diff 过程整体遵循深度优先、同层比较的策略；两个节点之间比较会根据它们是否拥有子节点或者文本节点做不同的操作；比较两组子节点是算法的重点，首先假设头尾节点可能相同做4次比对尝试，如果没有找到相同节点才按照通用方式遍历查找，查找结束再按情况处理剩下的节点；借助key通常可以非常精确找到相同节点，因此整个 patch 过程非常高效。

# 谈一谈对 vue 组件化的理解

回答总体思路：

​	组件化定义、优点、使用场景和注意事项等方面展开陈述，同时要强调 vue 中组件化的一些特点。

- 源码分析1: 组件定义

```vue
// 组件定义
Vue.comoinent('comp', {
template: '<div>this is a component</div>'
})
```

> 组件定义，src/core/global-api/assets.js

```vue
<template>
	<div>
    this is a component
  </div>
</template>
```

> Vue-loader 会编译 template 为 render 函数，最终导出的依然是组件配置对象

**src/core/global-api/assets.js**

```javascript
/* @flow */

import { ASSET_TYPES } from 'shared/constants'
import { isPlainObject, validateComponentName } from '../util/index'

export function initAssetRegisters (Vue: GlobalAPI) {
  /**
   * Create asset registration methods.
   */
  ASSET_TYPES.forEach(type => {
    Vue[type] = function (
      id: string,
      definition: Function | Object
    ): Function | Object | void {
      if (!definition) {
        return this.options[type + 's'][id]
      } else {
        /* istanbul ignore if */
        if (process.env.NODE_ENV !== 'production' && type === 'component') {
          validateComponentName(id)
        }
    
    		// def 是对象
        if (type === 'component' && isPlainObject(definition)) {
          // 定义 name
          definition.name = definition.name || id
          // extend 创建组件构造函数，def变成了构造函数
          definition = this.options._base.extend(definition)
        }
        if (type === 'directive' && typeof definition === 'function') {
          definition = { bind: definition, update: definition }
        }
    
    		// 注册 this.options[components][comp] = Ctor
        this.options[type + 's'][id] = definition
        return definition
      }
    }
  })
}

```

**src/core/global-api/extend.js**

```javascript
/* @flow */

import { ASSET_TYPES } from 'shared/constants'
import { defineComputed, proxy } from '../instance/state'
import { extend, mergeOptions, validateComponentName } from '../util/index'

export function initExtend (Vue: GlobalAPI) {
  /**
   * Each instance constructor, including Vue, has a unique
   * cid. This enables us to create wrapped "child
   * constructors" for prototypal inheritance and cache them.
   */
  Vue.cid = 0
  let cid = 1

  /**
   * Class inheritance
   */
  Vue.extend = function (extendOptions: Object): Function {
    extendOptions = extendOptions || {}
    const Super = this
    const SuperId = Super.cid
    const cachedCtors = extendOptions._Ctor || (extendOptions._Ctor = {})
    if (cachedCtors[SuperId]) {
      return cachedCtors[SuperId]
    }

    const name = extendOptions.name || Super.options.name
    if (process.env.NODE_ENV !== 'production' && name) {
      validateComponentName(name)
    }
		
    // 创建一个 VueComponent 类
    const Sub = function VueComponent (options) {
      this._init(options)
    }
    // 继承于 Vue
    Sub.prototype = Object.create(Super.prototype)
    Sub.prototype.constructor = Sub
    Sub.cid = cid++
    
    // 选项合并
    Sub.options = mergeOptions(
      Super.options,
      extendOptions
    )
    Sub['super'] = Super

    // For props and computed properties, we define the proxy getters on
    // the Vue instances at extension time, on the extended prototype. This
    // avoids Object.defineProperty calls for each instance created.
    if (Sub.options.props) {
      initProps(Sub)
    }
    if (Sub.options.computed) {
      initComputed(Sub)
    }

    // allow further extension/mixin/plugin usage
    Sub.extend = Super.extend
    Sub.mixin = Super.mixin
    Sub.use = Super.use

    // create asset registers, so extended classes
    // can have their private assets too.
    ASSET_TYPES.forEach(function (type) {
      Sub[type] = Super[type]
    })
    // enable recursive self-lookup
    if (name) {
      Sub.options.components[name] = Sub
    }

    // keep a reference to the super options at extension time.
    // later at instantiation we can check if Super's options have
    // been updated.
    Sub.superOptions = Super.options
    Sub.extendOptions = extendOptions
    Sub.sealedOptions = extend({}, Sub.options)

    // cache constructor
    cachedCtors[SuperId] = Sub
    return Sub
  }
}

function initProps (Comp) {
  const props = Comp.options.props
  for (const key in props) {
    proxy(Comp.prototype, `_props`, key)
  }
}

function initComputed (Comp) {
  const computed = Comp.options.computed
  for (const key in computed) {
    defineComputed(Comp.prototype, key, computed[key])
  }
}
```

- 源码分析2: 组件化优点

Lifecycle.js - mountComponent()

> 组件、Watcher、渲染函数和更新函数之间的关系

```javascript
export function mountComponent (
  vm: Component,
  el: ?Element,
  hydrating?: boolean
): Component {
  vm.$el = el
  if (!vm.$options.render) {
    vm.$options.render = createEmptyVNode
    if (process.env.NODE_ENV !== 'production') {
      /* istanbul ignore if */
      if ((vm.$options.template && vm.$options.template.charAt(0) !== '#') ||
        vm.$options.el || el) {
        warn(
          'You are using the runtime-only build of Vue where the template ' +
          'compiler is not available. Either pre-compile the templates into ' +
          'render functions, or use the compiler-included build.',
          vm
        )
      } else {
        warn(
          'Failed to mount component: template or render function not defined.',
          vm
        )
      }
    }
  }
  callHook(vm, 'beforeMount')

  let updateComponent
  /* istanbul ignore if */
  if (process.env.NODE_ENV !== 'production' && config.performance && mark) {
    updateComponent = () => {
      const name = vm._name
      const id = vm._uid
      const startTag = `vue-perf-start:${id}`
      const endTag = `vue-perf-end:${id}`

      mark(startTag)
      const vnode = vm._render()
      mark(endTag)
      measure(`vue ${name} render`, startTag, endTag)

      mark(startTag)
      vm._update(vnode, hydrating)
      mark(endTag)
      measure(`vue ${name} patch`, startTag, endTag)
    }
  } else {
    
    // 用户 $mount() 时，定义 updateComponent
    updateComponent = () => {
      vm._update(vm._render(), hydrating)
    }
  }

  // we set this to vm._watcher inside the watcher's constructor
  // since the watcher's initial patch may call $forceUpdate (e.g. inside child
  // component's mounted hook), which relies on vm._watcher being already defined
  new Watcher(vm, updateComponent, noop, {
    before () {
      if (vm._isMounted && !vm._isDestroyed) {
        callHook(vm, 'beforeUpdate')
      }
    }
  }, true /* isRenderWatcher */)
  hydrating = false

  // manually mounted instance, call mounted on self
  // mounted is called for render-created child components in its inserted hook
  if (vm.$vnode == null) {
    vm._isMounted = true
    callHook(vm, 'mounted')
  }
  return vm
}
```

- 源码分析3: 组件化实现

构造函数，src/core/global-api/extend.js

实例化及挂载，src/core/vdom/patch.js - createElm()

```javascript
function createElm (
vnode,
 insertedVnodeQueue,
 parentElm,
 refElm,
 nested,
 ownerArray,
 index
) {
  if (isDef(vnode.elm) && isDef(ownerArray)) {
    // This vnode was used in a previous render!
    // now it's used as a new node, overwriting its elm would cause
    // potential patch errors down the road when it's used as an insertion
    // reference node. Instead, we clone the node on-demand before creating
    // associated DOM element for it.
    vnode = ownerArray[index] = cloneVNode(vnode)
  }

  vnode.isRootInsert = !nested // for transition enter check
  // 如果要创建的是组件，走下面的流程
  if (createComponent(vnode, insertedVnodeQueue, parentElm, refElm)) {
    return
  }

  // 原生标签创建
  const data = vnode.data
  const children = vnode.children
  const tag = vnode.tag
  if (isDef(tag)) {
    if (process.env.NODE_ENV !== 'production') {
      if (data && data.pre) {
        creatingElmInVPre++
      }
      if (isUnknownElement(vnode, creatingElmInVPre)) {
        warn(
          'Unknown custom element: <' + tag + '> - did you ' +
          'register the component correctly? For recursive components, ' +
          'make sure to provide the "name" option.',
          vnode.context
        )
      }
    }

    vnode.elm = vnode.ns
      ? nodeOps.createElementNS(vnode.ns, tag)
    : nodeOps.createElement(tag, vnode)
    setScope(vnode)

    /* istanbul ignore if */
    if (__WEEX__) {
      // in Weex, the default insertion order is parent-first.
      // List items can be optimized to use children-first insertion
      // with append="tree".
      const appendAsTree = isDef(data) && isTrue(data.appendAsTree)
      if (!appendAsTree) {
        if (isDef(data)) {
          invokeCreateHooks(vnode, insertedVnodeQueue)
        }
        insert(parentElm, vnode.elm, refElm)
      }
      createChildren(vnode, children, insertedVnodeQueue)
      if (appendAsTree) {
        if (isDef(data)) {
          invokeCreateHooks(vnode, insertedVnodeQueue)
        }
        insert(parentElm, vnode.elm, refElm)
      }
    } else {
      createChildren(vnode, children, insertedVnodeQueue)
      if (isDef(data)) {
        invokeCreateHooks(vnode, insertedVnodeQueue)
      }
      insert(parentElm, vnode.elm, refElm)
    }

    if (process.env.NODE_ENV !== 'production' && data && data.pre) {
      creatingElmInVPre--
    }
  } else if (isTrue(vnode.isComment)) {
    vnode.elm = nodeOps.createComment(vnode.text)
    insert(parentElm, vnode.elm, refElm)
  } else {
    vnode.elm = nodeOps.createTextNode(vnode.text)
    insert(parentElm, vnode.elm, refElm)
  }
}

// 这里 createComponent 是把前面的那个执行的结果 vnode 转换为真实 dom
function createComponent (vnode, insertedVnodeQueue, parentElm, refElm) {
  // 获取管理钩子函数
  let i = vnode.data
  if (isDef(i)) {
    const isReactivated = isDef(vnode.componentInstance) && i.keepAlive
    // 存在 init 钩子，则执行之创建实例并挂载
    if (isDef(i = i.hook) && isDef(i = i.init)) {
      i(vnode, false /* hydrating */)
    }
    // after calling the init hook, if the vnode is a child component
    // it should've created a child instance and mounted it. the child
    // component also has set the placeholder vnode's elm.
    // in that case we can just return the element and be done.
    // 如果组件实例存在
    if (isDef(vnode.componentInstance)) {
      // 属性初始化
      initComponent(vnode, insertedVnodeQueue)
      // dom 插入操作
      insert(parentElm, vnode.elm, refElm)
      if (isTrue(isReactivated)) {
        reactivateComponent(vnode, insertedVnodeQueue, parentElm, refElm)
      }
      return true
    }
  }
}
```

**总结**

1、组件是独立和可复用的代码组织单元。组件系统是 Vue 核心特性之一，它使开发者使用小型、独立和通常可复用的组件构建大型应用；

2、组件化开发能大幅提高应用开发效率、测试性、复用性等；

3、组件使用按分类有：页面组件、业务组件、通用组件；

4、vue的组件是基于配置的，我们通常编写的组件是组件配置而非组件，框架后续会生成其构造函数，它们基于VueComponent，扩展于Vue；

5、vue中常见组件化技术有：属性prop，自定义事件，插槽等，它们主要用于组件通信、扩展等；

6、合理的划分组件，有助于提升应用性能；

7、组件应该是高内聚、低耦合的；

8、遵循单向数据流的原则。

# 谈一谈对 vue 设计原则的理解

在vue的官网上，就写着大大的定义和特点：

渐进式JavaScript框架

易用、灵活和高效

所以阐述此题的整体思路按照这个展开即可。

**总结**

- 首先就是渐进式JavaScript框架：

与其它大型框架不同的是，Vue 被设计为可以自底向上逐层应用。Vue 的核心库只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。另一方面，当与现代化的工具链以及各种支持类库结合使用时，Vue 也完全能够为复杂的单页应用提供驱动。

![渐进式](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vue%E9%9D%A2%E8%AF%95/1.webp)



- **易用性**

vue提供数据响应式、声明式模板语法和基于配置的组件系统等核心特性。

这些使我们只需要关注应用的核心业务即可，只要会写js、html和css就能轻松编写vue应用。

- **灵活性**

渐进式框架的最大优点就是灵活性，如果应用足够小，我们可能仅需要vue核心特性即可完成功能；

随着应用规模不断扩大，我们才可能逐渐引入路由、状态管理、vue-cli等库和工具；

不管是应用体积还是学习难度都是一个逐渐增加的平和曲线。

- **高效性**

超快的虚拟 DOM 和 diff 算法使我们的应用拥有最佳的性能表现。

追求高效的过程还在继续，vue3中引入Proxy对数据响应式改进以及编译器中对于静态内容编译的改进都会让vue更加高效。

# vue 为什么要求组件模版只能有一个根元素

从三方面考虑

1. new Vue({el:'#app'})
2. 单文件组件中，template 下的元素 div 。其实就是“树”状数据结构中的“根”。
3. diff 算法要求的，源码中，patch.js 里 patchVnode() 。

> 一

实例化 Vue 时：

```vue
<body>
  <div id='app'></div>
</body>

<script>
 var vm = new Vue({
   el: '#app'
 })
</script>
```

如果我在 body 下这样：

```vue
<body>
  <div id='app1'></div>
  <div id='app2'></div>
</body>
```

Vue 其实并不知道哪一个才是我们的入口。如果同时设置了多个入口，那么 vue 就不知道哪一个才是这“类”。

> 二

在 webpack 搭建的 vue 开发环境下，使用单文件组件时：

```vue
<template>
	<div>
    
  </div>
</template>
```

Template 这个标签，它有三个特性：

1. 隐藏性：该标签不会显示在页面的任何地方，即便里面有多少内容，它永远都是隐藏的状态，设置了display：none；
2. 任意性：该标签可以写在任何地方，甚至是 head、 body、 script 标签内
3. 无效性：该标签里的任何 HTML 内容都是无效的，不会起任何作用；只能 innerHTML 来获取到里面的内容。

一个 vue 单文件组件就是一个 vue 实例，如果 template 下有多个 div 那么如何指定 vue 实例的根入口呢，为了让组件可以正常生成一个 vue 实例，这个 div 会自然的处理成程序的入口，通过这个根节点，来递归遍历整个 vue 树下的所有节点，并处理为 vdom，最后再渲染真正的 HTML，插入在正确的位置。

> 三

diff 中 patchVnode 方法，用来比较新旧节点

```JavaScript
/*
	比较新旧 vnode 节点，根据不同的状态对 dom 做合理的更新草哦做（添加、移动、删除）
	整个过程还会依次调用 prepatch, update, postpatch 等钩子函数，在编译阶段生成的一些静态子树
	在这个过程中由于不会改变而直接跳过比对
	动态子树在比较过程中比较核心的部分就是当新旧 vnode 同时存在 children，通过 updataChildren 方法对字节点做更新，
	
	@param oldVnode 旧node
	@param vnode    新node
	@param insertedVnodeQueuue	空数组，用于生命周期 inserted 阶段，记录下所有新插入的节点以备调用
	@param removeOnly 是一个只用于 <transition-group> 的特殊标签，确保移除元素过程中保持一个正确的相对位置
*/
function patchVnode (
oldVnode,
 vnode,
 insertedVnodeQueue,
 ownerArray,
 index,
 removeOnly
) {
  if (oldVnode === vnode) {
    return
  }

  if (isDef(vnode.elm) && isDef(ownerArray)) {
    // clone reused vnode
    vnode = ownerArray[index] = cloneVNode(vnode)
  }

  const elm = vnode.elm = oldVnode.elm

  if (isTrue(oldVnode.isAsyncPlaceholder)) {
    if (isDef(vnode.asyncFactory.resolved)) {
      hydrate(oldVnode.elm, vnode, insertedVnodeQueue)
    } else {
      vnode.isAsyncPlaceholder = true
    }
    return
  }

  // reuse element for static trees.
  // note we only do this if the vnode is cloned -
  // if the new node is not cloned it means the render functions have been
  // reset by the hot-reload-api and we need to do a proper re-render.
  if (isTrue(vnode.isStatic) &&
      isTrue(oldVnode.isStatic) &&
      vnode.key === oldVnode.key &&
      (isTrue(vnode.isCloned) || isTrue(vnode.isOnce))
     ) {
    vnode.componentInstance = oldVnode.componentInstance
    return
  }

  let i
  const data = vnode.data
  if (isDef(data) && isDef(i = data.hook) && isDef(i = i.prepatch)) {
    i(oldVnode, vnode)
  }

  const oldCh = oldVnode.children
  const ch = vnode.children
  if (isDef(data) && isPatchable(vnode)) {
    for (i = 0; i < cbs.update.length; ++i) cbs.update[i](oldVnode, vnode)
    if (isDef(i = data.hook) && isDef(i = i.update)) i(oldVnode, vnode)
  }
  if (isUndef(vnode.text)) {
    if (isDef(oldCh) && isDef(ch)) {
      if (oldCh !== ch) updateChildren(elm, oldCh, ch, insertedVnodeQueue, removeOnly)
    } else if (isDef(ch)) {
      if (process.env.NODE_ENV !== 'production') {
        checkDuplicateKeys(ch)
      }
      if (isDef(oldVnode.text)) nodeOps.setTextContent(elm, '')
      addVnodes(elm, null, ch, 0, ch.length - 1, insertedVnodeQueue)
    } else if (isDef(oldCh)) {
      removeVnodes(oldCh, 0, oldCh.length - 1)
    } else if (isDef(oldVnode.text)) {
      nodeOps.setTextContent(elm, '')
    }
  } else if (oldVnode.text !== vnode.text) {
    nodeOps.setTextContent(elm, vnode.text)
  }
  if (isDef(data)) {
    if (isDef(i = data.hook) && isDef(i = i.postpatch)) i(oldVnode, vnode)
  }
}

function sameVnode (a, b) {
  return (
    a.key === b.key && (  // key值
      (
        a.tag === b.tag && // 标签名
        a.isComment === b.isComment && // 是否为注释节点
        isDef(a.data) === isDef(b.data) && // 是否定义了data，data包含一些具体信息
        sameInputType(a, b) // 当标签是 <input> 的时候，type 必须相同
      ) || (
        isTrue(a.isAsyncPlaceholder) &&
        a.asyncFactory === b.asyncFactory &&
        isUndef(b.asyncFactory.error)
      )
    )
  )
}
```

# 谈谈你对 MVC、MVP 和 MVVM 的理解

答题思路：此题涉及知识点很多，很难说清、说透，因为 MVC、MVP 这些我们前端程序员自己甚至都没用过。但是恰恰反映了前端这些年从无到有，从有到优的变迁过程，因此沿此思路回答将十分清楚。



**web 1.0 时代**

在 web 1.0 时代，并没有前端的概念。开发一个 web 应用多数采用 ASP.NET / JAVA / PHP编写，项目通常由多个aspx / jsp / php 文件构成，每个文件中同时包含了 HTML、CSS、JavaScript、C# / JAVA / PHP 代码，系统整体架构可能是这个样子的：

![ web 1.0 时代](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vue%E9%9D%A2%E8%AF%95/2.webp)

这种架构的好处是简单快捷，但是，缺点也非常明显：JSP代码难以维护为了让开发更加便捷，代码更易维护，前后端职责更清晰。便衍生出MVC开发模式和框架，前端展示以模板的形式出现。典型的框架就是：**Spring、Structs、Hibernate。**

整体框架如图所示☟：

![整体框架](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vue%E9%9D%A2%E8%AF%95/3.webp)

使用这种分层架构，职责清晰，代码易维护。但这里的MVC仅限于后端，前后端形成了一定的分离，前端只完成了后端开发中的view层。

但是，同样的这种模式存在着一些问题：

1、前端页面开发效率不高

2、前后端职责不清

# Vue 中 props 的实现原理

`<componment></componment> => ast语法树 => vnode`

```javascript
// create-componment.js
// install component management hooks onto the placeholder node
installComponentHooks(data)

// return a placeholder vnode
const name = Ctor.options.name || tag
const vnode = new VNode(
  `vue-component-${Ctor.cid}${name ? `-${name}` : ''}`,
  data,
  undefined,
  undefined,
  undefined,
  context,
  { Ctor, propsData, listeners, tag, children },
  asyncFactory
)

// init.js
export function initInternalComponent(
  vm: Component,
  options: InternalComponentOptions
) {
  const opts = (vm.$options = Object.create(vm.constructor.options))
  // doing this because it's faster than dynamic enumeration.
  const parentVnode = options._parentVnode
  opts.parent = options.parent
  opts._parentVnode = parentVnode

  const vnodeComponentOptions = parentVnode.componentOptions
  opts.propsData = vnodeComponentOptions.propsData
  opts._parentListeners = vnodeComponentOptions.listeners
  opts._renderChildren = vnodeComponentOptions.children
  opts._componentTag = vnodeComponentOptions.tag

  if (options.render) {
    opts.render = options.render
    opts.staticRenderFns = options.staticRenderFns
  }
}

// state.js
//propsOptions 用户自定义的属性
function initProps(vm: Component, propsOptions: Object) {
  const propsData = vm.$options.propsData || {}
  const props = (vm._props = {})
  // cache prop keys so that future props updates can iterate using Array
  // instead of dynamic object key enumeration.
  const keys = (vm.$options._propKeys = [])
  const isRoot = !vm.$parent
  // root instance props should be converted
  if (!isRoot) {
    // 如果是根元素 属性需要定义成响应式的
    toggleObserving(false)
  }
  for (const key in propsOptions) {
    keys.push(key) // 校验用户定义的属性和传入的属性
    const value = validateProp(key, propsOptions, propsData, vm)
    /* istanbul ignore else */
    if (process.env.NODE_ENV !== 'production') {
      const hyphenatedKey = hyphenate(key)
      if (
        isReservedAttribute(hyphenatedKey) ||
        config.isReservedAttr(hyphenatedKey)
      ) {
        warn(
          `"${hyphenatedKey}" is a reserved attribute and cannot be used as component prop.`,
          vm
        )
      }
      defineReactive(props, key, value, () => {
        if (!isRoot && !isUpdatingChildComponent) {
          warn(
            `Avoid mutating a prop directly since the value will be ` +
              `overwritten whenever the parent component re-renders. ` +
              `Instead, use a data or computed property based on the prop's ` +
              `value. Prop being mutated: "${key}"`,
            vm
          )
        }
      })
    } else {
      defineReactive(props, key, value)
    }
    // static props are already proxied on the component's prototype
    // during Vue.extend(). We only need to proxy props defined at
    // instantiation here.
    if (!(key in vm)) {
      proxy(vm, `_props`, key)
    }
  }
  toggleObserving(true)
}
```

# Vue.set

```javascript
export function set(target: Array<any> | Object, key: any, val: any): any {
  // 1.是开发环境 target 没定义或者是基础类型则报错
  if (process.env.NODE_ENV !== 'production' && (isUndef(target) || target)) {
    warn(
      `Cannot set reactive property on undefined, null, or primitive value: ${(target: any)}`
    )
  }
  // 2.如果是数组 Vue.set(array, 1, 100); 调用我们重写的splice方法(这样可以更新视图)
  if (Array.isArray(target) && isValidArrayIndex(key)) {
    target.length = Math.max(target.length, key)
    target.splice(key, 1, val)
    return val
  }
  // 3.如果是对象本身的属性，则直接添加即可
  if (key in target && !(key in Object.prototype)) {
    target[key] = val
    return val
  }
  // 4.如果是Vue实例 或 根数据data时 报错
  const ob = (target: any).__ob__
  if (target._isVue || (ob && ob.vmCount)) {
    process.env.NODE_ENV !== 'production' &&
      warn(
        'Avoid adding reactive properties to a Vue instance or its root $data ' +
          'at runtime - declare it upfront in the data option.'
      )
    return val
  }
  // 5.如果不是响应式的也不需要将其定义成响应式属性
  if (!ob) {
    target[key] = val
    return val
  }
  // 6.将属性定义成响应式的
  defineReactive(ob.value, key, val)
  // 7.通知视图更新
  ob.dep.notify()
  return val
}
```

# 谈一谈你对 Vue 的个人理解

- 先表达出对单向数据流的多概念，及整个 vuex 的运行流程
- 状态集中管理，实现多组件状态共享
- Vuex 的原理是通过 new Vue 产生实例，达到响应式数据变化的目的

# Vue 中观察者模式和发布订阅的区别和场景

- Vue 中响应式数据变化就是典型的观察者模式
- Vue 中的事件绑定就是发布订阅模式

观察者模式中观察者和被观察者是存在关联的。发布订阅模式中订阅者和发布者没有关联，所以观察者模式中包含了发布订阅模式(watcher 和 dep)
