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



**web 2.0时代**

自从Gmail的出现，ajax技术开始风靡全球。有了ajax之后，前后端的职责就更加清晰了。

因为前端可以通过Ajax与后端进行数据交互，因此，整体的架构图也变化成了下面这幅图☟：

![整体框架](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vue%E9%9D%A2%E8%AF%95/4.webp)

通过ajax与后台服务器进行数据交换，前端开发人员，只需要开发页面这部分内容，数据可由后台进行提供。

而且ajax可以使得页面实现部分刷新，减少了服务端负载和流量消耗，用户体验也更佳。

这时，才开始有专职的前端工程师。同时前端的类库也慢慢的开始发展，最著名的就是jQuery了。

当然，此架构也存在问题：缺乏可行的开发模式承载更复杂的业务需求，页面内容都杂糅在一起，一旦应用规模增大，就会导致难以维护了。

因此，前端的MVC也随之而来。



**前后端分离后的架构演变——MVC、MVP和MVVM**



**MVC**

前端的MVC与后端类似，具备着View、Controller和Model。

- Model：负责保存应用数据，与后端数据进行同步

- Controller：负责业务逻辑，根据用户行为对Model数据进行修改

- View：负责视图展示，将model中的数据可视化出来。

三者形成了一个如图所示的模型：

![MVC](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vue%E9%9D%A2%E8%AF%95/5.webp)

这样的模型，在理论上是可行的。但往往在实际开发中，并不会这样操作。因为开发过程并不灵活。

例如，一个小小的事件操作，都必须经过这样的一个流程，那么开发就不再便捷了。

在实际场景中，我们往往会看到另一种模式，

如图所示☟：

![MVC](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vue%E9%9D%A2%E8%AF%95/6.webp)

这种模式在开发中更加的灵活，backbone.js框架就是这种的模式。

但是，这种灵活可能导致严重的问题：

1、数据流混乱：如下图☟

![MVC](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vue%E9%9D%A2%E8%AF%95/7.webp)

2、View比较庞大，而Controller比较单薄：

由于很多的开发者都会在view中写一些逻辑代码，逐渐的就导致view中的内容越来越庞大，而controller变得越来越单薄。

既然有缺陷，就会有变革。

前端的变化中，似乎少了MVP的这种模式，是因为AngularJS早早地将MVVM框架模式带入了前端。

MVP模式虽然前端开发并不常见，但是在安卓等原生开发中，开发者还是会考虑到它。



**MVP**

MVP与MVC很接近，P指的是Presenter，presenter可以理解为一个中间人。

它负责着View和Model之间的数据流动，防止View和Model之间直接交流。

我们可以看一下图示☟

![MVP](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vue%E9%9D%A2%E8%AF%95/8.webp)

我们可以通过看到，presenter负责和Model进行双向交互，还和View进行双向交互。

这种交互方式，相对于MVC来说少了一些灵活，VIew变成了被动视图，并且本身变得很小。虽然它分离了View和Model。

但是应用逐渐变大之后，导致presenter的体积增大，难以维护。

要解决这个问题，或许可以从MVVM的思想中找到答案。



**MVVM**

首先，何为MVVM呢？MVVM可以分解成(Model-View-VIewModel)。

ViewModel可以理解为在presenter基础上的进阶版。如图所示☟☟：

![MVVM](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vue%E9%9D%A2%E8%AF%95/9.png)

ViewModel通过实现一套数据响应式机制自动响应Model中数据变化；

同时Viewmodel会实现一套更新策略自动将数据变化转换为视图更新；

通过事件监听响应View中用户交互修改Model中数据。

这样在ViewModel中就减少了大量DOM操作代码。

MVVM在保持View和Model松耦合的同时，还减少了维护它们关系的代码，使用户专注于业务逻辑，兼顾开发效率和可维护性。



**总结：**

这三者都是框架模式，它们设计的目标都是为了解决Model和View的耦合问题。

MVC模式出现较早主要应用在后端，如Spring MVC、ASP.NET MVC等，在前端领域的早期也有应用，如Backbone.js。

它的优点是分层清晰，缺点是数据流混乱，灵活性带来的维护性问题。

MVP模式在是MVC的进化形式，Presenter作为中间层负责MV通信，解决了两者耦合问题，但P层过于臃肿会导致维护问题。

MVVM模式在前端领域有广泛应用，它不仅解决MV耦合问题，还同时解决了维护两者映射关系的大量繁杂代码和DOM操作代码，在提高开发效率、可读性同时还保持了优越的性能表现。

# Vue 中组件之间的通信

1. props
2. $emit / $on
3. vuex
4. $parent / $children
5. $attrs / $ listeners
6. Provide / inject

常用使用场景可以分为三类：

- 父子组件通信
- 兄弟组件通信
- 跨层组件通信

# 你了解哪些Vue性能优化方法

首先，我们要找到VUE性能的现存问题，大部分都是代码层面的，然后具体的提出代码层优化意见就可以了。



目前我们所知的VUE代码层优化大致为一下11点，村长已经都帮大家整理好了，请大家随意消化一下：

- 路由懒加载
- keep-alive缓存页面
- 使用v-show复用DOM
- v-for 遍历避免同时使用 v-if
- 长列表性能优化
- 事件的销毁
- 图片懒加载
- 第三方插件按需引入
- 无状态的组件标记为函数式组件
- 子组件分割
- 变量本地化
- SSR



- 路由懒加载☟

```javascript
const router = new VueRouter({
  routes: [
    { path: '/foo', component: () => import('./Foo.vue') }
  ]
})
```

- keep-alive缓存页面☟

```vue
<template>
  <div id="app">
    <keep-alive>
      <router-view/>
    </keep-alive>
  </div>
</template>
```

- 使用v-show复用DOM☟

```vue
<template>
 <div class="cell">
   <!-- 这种情况用 v-show 复用 DOM，比 v-if 效果好-->
   <div v-show="value" class="on">
     <Heavy :n="10000"/>
   </div>
   <div v-show="!value" class="off">
     <Heavy :n="10000"/>
   </div>
  </div>
</template>
```

- v-for 遍历避免同时使用 v-if☟
- 长列表性能优化：

  如果列表是纯粹的数据展示，不会有任何改变，就不需要做响应化☟

```javascript
export default {
  data: () => ({
    users: []
  }),
  async create() {
    const users = await.get('/api/users')
    this.users = Object.freze(users)
  }
}
```

​	如果是大数据长列表，可采用虚拟滚动，只渲染少部分区域的内容☟

```vue
<recycle-scroller class="items" :items="items" :item-size="24">
	<template>
  	<FetchItemView :item="item" @vote="voteItem(item)" />
  </template>
</recycle-scroller>
```

> 参考：[vue-virtual-scroller](https://github.com/Akryum/vue-virtual-scroller)、[vue-virtual-scroll-list](https://github.com/tangbc/vue-virtual-scroll-list)

- 事件的销毁：

Vue 组件销毁时，会自动解绑它的全部指令及事件监听器，但是仅限于组件本身的事件。

```javascript
created() {
  this.timer = setInterval(this.refresh, 2000)
},

beforeDestroy() {
  clearInterval(this.timer)
}
```

- 图片懒加载：

对于图片过多的页面，为了加速页面加载速度。

所以很多时候我们需要将页面内未出现在可视区域内的图片先不做加载， 等到滚动到可视区域后再去加载。

```vue
<img v-lazy="/static/img/1.png">
```

> 参考项目：[vue-lazyload](https://github.com/hilongjw/vue-lazyload)

- 第三方插件按需引入：

像element-ui这样的第三方组件库可以按需引入，避免体积太大。

```vue
import Vue from 'vue';
import { Button, Select } from 'element-ui';

Vue.use(Button)
Vue.use(Select)
```

- 无状态的组件标记为函数式组件☟

```vue
<template functional>
	<div class="cell">
    <div v-if="props.value" class="on"></div>
    <section v-else class="off"></section>
  </div>
</template>

<script>
	export default {
    props: ['value']
  }
</script>
```

- 子组件分割

```vue
<template>
	<div>
    <ChildrComp/>
  </div>
</template>

<script>
export default {
  components: {
    ChildrComp: {
      methods: {
        heavy () { /* 耗时任务 */}
      }，
      render (h) {
    		return h('div', this.heavy())
  		}
    }
  }
}
</script>
```

- 变量本地化

```vue
<template>
	<div :style="{ opacity:start / 300 }">
    {{ result }}
  </div>
</template>

<script>
import { heavy } from '@/utils'
  
export default {
  props: ['start'],
  computed: {
    base () { return 42 },
    result () {
      const base = this.base()
      let result = thiis.start
      for(let i = 0; i < 1000; i++){
        result += heay(base)
      }
      return result
    }
  }
}
</script>
```

- 服务端渲染 - SSR

# 你对Vue3.0的新特性有没有了解

Vue3.0改进方向，主要在以下几点：

- 更快
  - 虚拟DOM重写
  - 优化slots的生成
  - 静态树提升
  - 静态属性提升
  - 基于Proxy的响应式系统
- 更小：
  - 通过摇树优化核心库体积
- 更容易维护：
  - TypeScript + 模块化
- 更加友好
  - 跨平台：编译器核心和运行时核心与平台无关，使得Vue更容易与任何平台（Web、Android、iOS）一起使用
- 更容易使用
  - 改进的TypeScript支持，编辑器能提供强有力的类型检查和错误及警告
- 更好的调试支持
- 独立的响应化模块
- Composition API



**虚拟 DOM 重写**

期待更多的编译时提示来减少运行时开销，使用更有效的代码来创建虚拟节点。

组件快速路径+单个调用+子节点类型检测

▷跳过不必要的条件分支

▷JS引擎更容易优化

详情见下图☟

![虚拟 DOM 重写](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vue%E9%9D%A2%E8%AF%95/10.jpeg)



**优化slots生成**

vue3中可以单独重新渲染父级和子级：

▷确保实例正确的跟踪依赖关系

▷避免不必要的父子组件重新渲染

详情见下图☟

![优化slots生成](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vue%E9%9D%A2%E8%AF%95/11.jpeg)



**静态树提升(Static Tree Hoisting)**

使用静态树提升，这意味着 Vue 3 的编译器将能够检测到什么是静态的，然后将其提升，从而降低了渲染成本。

▷跳过修补整棵树，从而降低渲染成本

▷即使多次出现也能正常工作

详情见下图☟

![静态树提升(Static Tree Hoisting)](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vue%E9%9D%A2%E8%AF%95/12.jpeg)



**静态属性提升**

使用静态属性提升，Vue 3打补丁时将跳过这些属性不会改变的节点。☟

![静态属性提升](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vue%E9%9D%A2%E8%AF%95/13.webp)



**基于 Proxy 的数据响应式**

Vue 2的响应式系统使用：

- Object.defineProperty 的getter 和 setter。

Vue 3 将使用 ES2015 Proxy 作为其观察机制，这将会带来如下变化：

- 组件实例初始化的速度提高100％
- 使用Proxy节省以前一半的内存开销，加快速度，但是存在低浏览器版本的不兼容
- 为了继续支持 IE11，Vue 3 将发布一个支持旧观察者机制和新 Proxy 版本的构建

![基于 Proxy 的数据响应式](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vue%E9%9D%A2%E8%AF%95/14.webp)



**高可维护性**

Vue 3 将带来更可维护的源代码。它不仅会使用 TypeScript，而且许多包被解耦，更加模块化。

![高可维护性](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vue%E9%9D%A2%E8%AF%95/15.png)

# vue扩展现有组件

1. 使用 Vue.mixin 全局混入

混入(mixin)是一种分发 vue 组件中可复用功能的非常灵活的方式。混入对象可以包含任意组件选项。当组件使用混入对象时，所有混入对象的选项将被混入该组件本身的选项。mixin选项接受一个混合对象的数组。

**mixin**的调用顺序：

从执行先后顺序来说，混入对象的钩子将在组件自身钩子之前调用，如果遇到全局混入(Vue.mixin)，全局混入的执行顺序要前于混入和组件里的方法。

2. 加 slot 扩展

- 默认插槽和匿名插槽

  slot 用来获取组件中的原内容

- 具名插槽

# watch 和 computed 的区别以及怎么选用

**区别**

1. 定义/语义区别

> watch

```vue
<input type="text" v-model="foo" />
```

```javascript
var = vm = new Vue({
  el: '#demo',
  data: {
    foo: 1
  },
  watch: {
    foo: function (newVal, oldVal) {
      console.log(newVal + '' + oldVal)
    }
  }
})
vm.foo = 2 // 2 1 
```

> computed

```javascript
var vm = new Vue({
  el: '#demo',
  data: {
    firstName: 'LBJ',
    lastName: 'hui'
  },
  computed: {
    fullName: function () {
      return this.firstName + '' + this.lastName
    }
  }
})
vm.fullName //LBJ hui  computed 内部的函数调用的时候不需要加 ()
```

2. 功能区别

watch 更通用，computed 派生功能都能实现，计算属性底层来自于 watch，但做了更多，例如缓存

3. 用法区别

conputed 更简单/更高效，优先使用

有些必须 watch，比如值变化要和后端交互

**使用场景**

> watch

watch 需要在数据变化时执行异步或开销较大的操作时使用，简单讲，当一条数据影响多条数据的时候，例如，搜索数据

> computed

对于任何复杂逻辑或一个数据属性在它所依赖的属性发生变化时，也要发生变化，简单讲，当一个属性受多个属性影响的时候，例如购物车商品结算时。

# Vue 生命周期的理解

![Vue 生命周期](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vue生命周期.jpg)

下面从源码方面详细解释一下这张图

**实例化**

> 显而易见，这个就是实例化。实例化之后，会执行一下操作。根据 vue 的源码，我们可以看到 vue 的本质就是一个 function， new Vue 的过程就是初始化 **参数、生命周期、事件**等一系列过程

src/instance/index.js

```javascript
// vue 构造函数
function Vue (options) {
  if (process.env.NODE_ENV !== 'production' &&
    !(this instanceof Vue)
  ) {
    warn('Vue is a constructor and should be called with the `new` keyword')
  }
  // 只有在 new Vue 时才会执行， _init 方法就是 initMixin 中的 _init 方法
  this._init(options)
}

// 初始化 option 相关工作（<= 此处调用beforeCreate、create 钩子）
initMixin(Vue)
// 数据绑定核心方法
stateMixin(Vue)
// 事件绑定的核心方法
eventsMixin(Vue)
// 生命周期的核心方法
lifecycleMixin(Vue)
// 渲染核心方法， render / Vnode
renderMixin(Vue)

export default Vue
```

**初始化事件 生命周期函数**

> 首先就是初始化事件和生命周期函数。这时候，这个对象身上只有默认一些生命周期函数和默认的事件，其他的东西都未创建

**beforeCreate 创建前**

> 接着就是`beforeCreate(创建前)`执行。但是这个时候拿不到 `data`里边的数据。data 和 ，methods 中的数据都还没初始化

**注射相应**

> `injections`(注射器) `reactivity`(响应) 给数据添加观察者

**created 创建后**

> `created 创建后`执行。因为上边给数据添加了观察者，所以现在就可以访问到`data`里的数据了。这个钩子也是常用的，可以请求数据了。如果要调用 methods 中的方法或者操作 data 中数据，要在 created 里操作。也因为请求数据是一步的，所以发送请求宜早不宜迟，通常在这个时候发送请求。

src/instance/init.js

```javascript
export function initMixin (Vue: Class<Component>) {
  // 此处的 _init 方法，与 Vue 构造函数中的 _init 是同一个方法
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
    callHook(vm, 'beforeCreate') // 执行 beforeCreate 生命周期函数
    initInjections(vm) // resolve injections before data/props
    initState(vm)
    initProvide(vm) // resolve provide after data/props
    callHook(vm, 'created') // 执行 create 生命周期函数

    /* istanbul ignore if */
    if (process.env.NODE_ENV !== 'production' && config.performance && mark) {
      vm._name = formatComponentName(vm, false)
      mark(endTag)
      measure(`vue ${vm._name} init`, startTag, endTag)
    }

    // 判断 el 元素
    if (vm.$options.el) {
      // 挂载该 el DOM 元素
      vm.$mount(vm.$options.el)
    }
  }
}
```

**是否存在 el**

> `el` 指明挂载目标。这个步骤就是判断一下是否有写 `el` ,如果没有就判断有没有调用实例上的 `$mount('')` 方法调用。

src/instance/init.js

**判断是否有 template**

> 判断是否有template

- 如果有 `template` 则渲染 `template` 里的内容
- 如果没有，则渲染 `el` 指明的挂载对象里的内容

src/platforms/web/entry-runtime-with-compiler.js

```javascript
// 保存 mount
const mount = Vue.prototype.$mount
Vue.prototype.$mount = function (
  el?: string | Element,
  hydrating?: boolean
): Component {
  el = el && query(el)

  /* istanbul ignore if */
  if (el === document.body || el === document.documentElement) {
    process.env.NODE_ENV !== 'production' && warn(
      `Do not mount Vue to <html> or <body> - mount to normal elements instead.`
    )
    return this
  }

  const options = this.$options
  // resolve template/el and convert to render function
  if (!options.render) {
    let template = options.template
    // 判断是否存在 template
    if (template) {
      if (typeof template === 'string') {
        if (template.charAt(0) === '#') {
          // 通过 #id 获取 DOM
          template = idToTemplate(template)
          /* istanbul ignore if */
          if (process.env.NODE_ENV !== 'production' && !template) {
            warn(
              `Template element not found or is empty: ${options.template}`,
              this
            )
          }
        }
      } else if (template.nodeType) {
        template = template.innerHTML
      } else {
        if (process.env.NODE_ENV !== 'production') {
          warn('invalid template option:' + template, this)
        }
        return this
      }
    } else if (el) {
      template = getOuterHTML(el)
    }
    if (template) {
      /* istanbul ignore if */
      if (process.env.NODE_ENV !== 'production' && config.performance && mark) {
        mark('compile')
      }

      const { render, staticRenderFns } = compileToFunctions(template, {
        outputSourceRange: process.env.NODE_ENV !== 'production',
        shouldDecodeNewlines,
        shouldDecodeNewlinesForHref,
        delimiters: options.delimiters,
        comments: options.comments
      }, this)
      options.render = render
      options.staticRenderFns = staticRenderFns

      /* istanbul ignore if */
      if (process.env.NODE_ENV !== 'production' && config.performance && mark) {
        mark('compile end')
        measure(`vue ${this._name} compile`, 'compile', 'compile end')
      }
    }
  }
  return mount.call(this, el, hydrating)
}
```

**beforeMount 挂载前**

> beforeMount 挂载前执行

**替换 el**

> 这个时候会在实例上创建一个 `el` ,替换原来的 `el` 。也是真正的挂载

**mounted 挂载后**

> `mounted` 挂载后执行。这个时候 DOM 已经加载完成了，可以操作 DOM 了。只要执行完成了 mounted，就表示整个 vue 实例已经初始化完毕了。这个也是常用的钩子。一般操作 DOM 都在这里。

src/platforms/web/runtime/index.js

```javascript
// public mount method
Vue.prototype.$mount = function (
  el?: string | Element,
  hydrating?: boolean
): Component {
  // 判断是否存在 el 以及在浏览器环境
  el = el && inBrowser ? query(el) : undefined
  // 调用 mountComponent
  return mountComponent(this, el, hydrating) // 看这里
}
```

src/core/instance/lifecycle.js

```javascript
export function mountComponent (
  vm: Component,
  el: ?Element,
  hydrating?: boolean
): Component { // 挂载组件 vm： Vue实例 el：真实的 DOM 节点对象
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
  callHook(vm, 'beforeMount') // 挂载前 执行生命周期里的 beforeMount 事件

  let updateComponent
  /* istanbul ignore if */
  if (process.env.NODE_ENV !== 'production' && config.performance && mark) { // 开启了性能追踪时的分支
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
      // 更新视图，第一个参数返回 Vnode
      // vm._render 会根据我们的 html 模板和 vm 上的数据生成一个新的 VNode
      // vm._update 会将新的 VNode 与旧的 Vnode 进行对比，执行 __patch__ 方法打补丁，并更新真实 DOM
      // 初始化时，肯定没有旧的 VNode 咯，这个时候就会全量更新 DOM
      vm._update(vm._render(), hydrating)
    }
  }

  // we set this to vm._watcher inside the watcher's constructor
  // since the watcher's initial patch may call $forceUpdate (e.g. inside child
  // component's mounted hook), which relies on vm._watcher being already 
  // 当 new Watcher 时，会执行 updateComponent
  // 执行 updateComponent 函数会访问 data 中的数据，相当于触发 data 中数据的 get 属性
  // 触发 data 中数据的 get 属性，就相当于触发了 依赖收集
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
    vm._isMounted = true // 修改当前 vm 的状态
    callHook(vm, 'mounted') // mounted 钩子被调用
  }
  return vm
}
```

**dataChange**

> 当数据有变动时，会触发下面两个钩子

- 在 `beforeUpdate` 更新前和 `updated` 更新后之间会进行 DOM 的重新渲染和补全。
- 接着是 `updated` 更新后

src/core/observer/scheduler.js

```javascript
function callUpdatedHooks (queue) {
  let i = queue.length
  while (i--) {
    const watcher = queue[i]
    const vm = watcher.vm
    if (vm._watcher === watcher && vm._isMounted && !vm._isDestroyed) {
      callHook(vm, 'updated') // 执行 updated
    }
  }
}
```

**callDestroys**

- `beforeDestroy`销毁前和`destroy`销毁后这两个钩子是需要我们手动调用实例上的 `$destroy` 方法才会触发
- 当 `$destroy` 方法调用后
- `beforeDestroy`销毁前触发
- 移除数据劫持、事件监听、子组件属性所有的东西还保留只是不能修改
- `desstroy`销毁后触发

src/core/instance/lifecycle.js

```javascript
  Vue.prototype.$destroy = function () {
    const vm: Component = this
    if (vm._isBeingDestroyed) {
      return
    }
    callHook(vm, 'beforeDestroy') // 调用 beforeDestroy
    vm._isBeingDestroyed = true
    // remove self from parent
    const parent = vm.$parent
    if (parent && !parent._isBeingDestroyed && !vm.$options.abstract) {
      remove(parent.$children, vm)
    }
    // teardown watchers
    // 清楚 watcher
    if (vm._watcher) {
      vm._watcher.teardown()
    }
    let i = vm._watchers.length
    while (i--) {
      vm._watchers[i].teardown()
    }
    // remove reference from data ob
    // frozen object may not have observer.
    if (vm._data.__ob__) {
      vm._data.__ob__.vmCount--
    }
    // call the last hook...
    // 修改 vm 状态
    vm._isDestroyed = true
    // invoke destroy hooks on current rendered tree
    vm.__patch__(vm._vnode, null)
    // fire destroyed hook
    callHook(vm, 'destroyed') // 调用 destroyed
    // turn off all instance listeners.
    // 关闭 vm 实例的 listeners
    vm.$off()
    // remove __vue__ reference
    if (vm.$el) {
      vm.$el.__vue__ = null
    }
    // release circular reference (#6759)
    if (vm.$vnode) {
      vm.$vnode.parent = null
    }
  }
```

**新增钩子**

- activated: keep-alive 组件激活时调用

  类似 created 没有真正创建，只是激活

- deactivated: keep-alive 组件停用时调用

  类似 destroyed 没有真正移除，只是禁用

- 在 2.2.0 及其更高版本中，activated 和 deactivated 将会在 `<keep-alive></keep-alive>` 树内的所有嵌套组件中触发。

# vuex 使用及其理解

1. vuex是什么
2. 核心概念是什么
   1. state
   2. mutation
   3. action
   4. getter
   5. model
3. 怎么做数据存储
4. 什么情况下应该使用vuex
5. vuex理解  => 源码

vuex 数据流程

![vuex](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/Vue/vuex.jpg)

# nextTick 的原理

nextTick 官方文档的解释，它可以在 DOM 更新完毕之后执行一个回调

```javascript
// 修改数据
vm.msg = 'Hello'
// DOM 还没有更新
Vue.nextTick(function () {
	// DOM 更新了
})
```

尽管 MVVM 框架并不推荐访问 DOM，但有时候确实会有这样的需求，尤其是和第三方插件进行配合的时候，免不了要进行 DOM 操作。而 nextTick 就提供了一个桥梁，确保我们操作的是更新后的 DOM。

**Vue 如何检测到 DOM 更新完毕呢？**

能监听到 DOM 改动的API：MutationObserver

**理解 MutationObserver**

MutationObserver 是 HTML5 新增的属性，用于监听 DOM 修改事件，能够监听到节点的属性、文本内容、字节点等的改动过，是一个功能强大的利器。

```javascript
// MutationObserver 基本用法
var observer = new MutationObserver(() => {
  console.log('DOM被修改了')
})
var article = document.querySelector('article')
observer.observer(article)
```

vue是不是用 MutationObserver 来监听 DOM 更新完毕的呢？

vue 的源码中实现 nextTick 的地方：

```javascript
// src/core/util/next-tick.js
if (!isIE && typeof MutationObserver !== 'undefined' && (
  isNative(MutationObserver) ||
  // PhantomJS and iOS 7.x
  MutationObserver.toString() === '[object MutationObserverConstructor]'
)) {
  // Use MutationObserver where native Promise is not available,
  // e.g. PhantomJS, iOS7, Android 4.4
  // (#6466 MutationObserver is unreliable in IE11)
  let counter = 1
  const observer = new MutationObserver(flushCallbacks)
  const textNode = document.createTextNode(String(counter))
  observer.observe(textNode, {
    characterData: true
  })
  timerFunc = () => {
    counter = (counter + 1) % 2
    textNode.data = String(counter)
  }
  isUsingMicroTask = true
}
```

**事件循环**

在 js 的运行环境中，通常伴随着很多事件的发生，比如用户点击、页面渲染、脚本执行、网络请求，等等。为了协调这些事件等处理，浏览器使用事件循环机制。

简要来说，事件循环会维护一个或多个任务队列(task queues)，以上提到的事件作为任务源往队列中加入任务。有一个持续执行的线程来处理这些任务，每执行完一个就从队列中移除它，这就是一次事件循环。

```javascript
for(let i = 0; i < 100; i++){
  dom.style.left = i + 'px'
}
```

事实上，这100次 for 循环同属于一个 task，浏览器只在该 task 执行完成后进行一次 DOM 更新。

只要让 nextTick 里的代码放在 UI render 步骤后面执行，岂不就访问到更新后的 DOM 了？

vue 就是这样的思路，并不是用 MutationObserver 进行 DOM 变动监听，而是用队列控制的方式达到目的。那么 vue 又是如何做到队列控制的呢？我们可以很自然的想到 setTimeout，把 nextTick 要执行的代码当作下一个 task 放入队列末尾。

vue 的数据响应过程包含：数据更改 ➡️ 通知Watcher ➡️ 更新DOM。而数据对的更改不由我们控制，可能在任何时候发生。如果恰巧发生在重绘之前，就会发生多次渲染。这就意味着性能浪费，是 vue 不愿意看到的。

所以，vue 的队列控制是经过了深思熟虑的。在这之前，我们还需了解 event loop 的另一个重要概念，microtask。

**microtask**

从名字看，我们可以把它称为微任务。

每一次事件循环都包含一个 microtask 队列，在循环结束后依次执行队列中的 microtask 并移除，然后再开始下一次事件循环。

在执行 microtask 的过程中后加入 mircotask 队列的微任务，也会在下一次事件循环之前被执行。也就是说，microtask 总要等到 mircotask 都执行完后才能执行，microtask 有着更高的优先级。

microtask 的这一特性，是做队列控制的最佳选择。vue 进行 DOM 更新内部也是调用 nextTick 来做异步队列控制。而当我们自己调用 nextTick 的时候，它就在更新 DOM 的那个 microtask 后追加了我们自己的回调函数，从而确保我们的代码在 DOM 更新后执行，同时也避免了 setTimeout 可能存在多次执行问题。

常见的 microtask 有：Promise、MutationObserver、Object.observe(废弃)，以及 nodejs 中的 process.nextTick。

看到了 MutationObserver，vue 用 MutationObserver 是想利用它的 mircotask 特性，而不是想做 DOM 监听。核心是 mircotask，用不用 MutationObserver 都行的。事实上，vue 在 2.5 版本中已经删去了 MutationObserver 相关的代码，因为它是 HTML5 新增的特性，在 IOS 上尚有 bug。

那么最有的 mircotask 策略就是 Promise 了，而令人尴尬的是，Promise 是 ES6 新增的东西，也存在兼容问题呀。所以 vue 就面临一个降级策略。

**vue 的降级策略**

上面我们讲到了，队列控制的最佳选择是 microtask，而 mircotask 的最佳选择是 Promise。但如果当前环境不支持 Promise， vue 就不得不降级为 macrotask 来做队列控制了。

macrotask 有哪些可选的方案呢？前面提到了setTimeout 是一种，但它不是理想的方案。因为 setTimeout 执行的最小时间间隔是约4ms的样子，略微有点延迟。

在 vue2.5 的源码中，microtask 的降级的方案依次是： setImmediate、MessageChannel、setTimeout。

setImmediate 是最理想的方案了，可惜的是只有 IE 和 nodejs 支持

MessageChannel 的 onmessage 回调也是 microtask，但也是个新的 API，面临兼容性的尴尬。

所以最后的兜底方案就是 setTimeout 了，尽管它有执行延迟，可能造成多次渲染，算是没有办法的办法了。

**总结**

1. vue 是异步队列的方式来控制 DOM 更新和 nextTick 回调先后执行
2. microtask 因为其高优先级特性，能确保队列中的微任务在一次事件循环前被执行完毕
3. 因为兼容性问题，vue 不得不做了 microtask 向 macrotask 的降级方案

# vue 双向数据绑定原理



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
