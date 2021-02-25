# javascript event（事件对象）详解

## 1. 事件对象

> Event 对象代表事件的状态，比如事件在其中发生的元素、键盘按键的状态、鼠标的位置、鼠标按钮的状态。

- 什么时候会产生 Event 对象呢?
  - 例如: 当用户单击某个元素的时候,我们给这个元素注册的事件就会触发,该事件的本质就是一个函数,而该函数的形参接收一个 event 对象.
- 事件通常与函数结合使用，函数不会在事件发生前被执行！

## 2. 事件流

### 2.1 事件流发展史

- 事件发展史,这位大神已经写好了,想去偷瞄两眼的请点击[这里](http://www.cnblogs.com/rubylouvre/archive/2010/04/27/1721988.html)

### 2.2 冒泡

- 什么是事件冒泡,
  - 官方的定义就是从最特定的事件目标到最不特定的事件目标

> 意思就是说,假如用户单击了一个元素,该元素拥有一个 click 事件,那么同样的事件也将会被它的祖先触发,这个事件从该元素开始一直冒泡到 DOM 树的最上层,这一过程称为事件冒泡

### 2.3 捕获

- 什么是事件捕获

> 事件捕获和事件是相反的,也就是说,当用户触发了一个事件的时候,这个事件是从 DOM 树的最上层开始触发一直到捕获到事件源.

### 2.4 事件流

- 它的由来

> 由于微软和网景乱搞,后来必须要为事件传播机制,制定一个标准,因为事件捕获是网景公司开发出来的,而事件冒泡是由微软公司开发出来的,它们都想要自己的技术成为标准,所以导致这两个公司老是干架,制定标准的人为了不让它们干架,所以研发了事件流.

### 2.5 事件流的写法以及实现方式

- 标准实现方式使用关键词

  ```
  addEventListener
  ```

  ,假如你想要给某一个元素添加事件,现在就可以这样写

  ```
  element.addEventListener(eventType, fn, false)
  ```

  - `dom对象.addEventListener(事件类型, 回调函数, 事件机制)`这里的事件类型表示你要使用哪种事件类型比如`click`, 回调函数里面写着触发此事件你要做什么事情, 事件机制分为冒泡和捕获,如果为`false`表示事件冒泡,为`true`表示事件捕获

- 既然有标准的实现方式,那么肯定也存在着不和谐的写法,没办法谁让人家牛逼呢,俗话说的好啊

  ```
  两虎之争必有一伤
  ```

  ,可伤了我们程序员了.这种不和谐的写法是

  - `dom对象.attachEvent(eventType, fn)`第一个参数表示事件类型,第二个是回调.这种写法兼容 IE, IE 没有实现事件捕获,因为在当时他比较厉害,以为没必要…………只是,,,,省略一千字, 现在微软的浏览器已经做得很好了… 只是调侃一下无其他意图..

- 以上的两种写法一种是兼容 W3C 标准的一种是老版 IE 的写法,怎么写兼容性写法呢?下面是注册事件和删除事件的`Code`

```javascript
1.// 注册时间
2.if(dom.addEventListener) {
3.    dom.addEventListener(eventType, fn);
4.} else {
5.    if(dom.attachEvent) {
6.        dom.attachEvent('on' + eventType, fn);
7.    }
8.}
9.
10.// 下面是删除事件
11.if(dom.removeEventListener) {
12.    dom.removeEventListener(eventType, fn, false);
13.} else {
14.    if(dom.detachEvent) {
15.        dom.detachEvent("on" + eventType, fn)
16.    }
17.}
```

- 冒泡和捕获的一个小 demo

```javascript
1.<!DOCTYPE html>
2.<html>
3.<head>
4.    <meta charset="utf-8">
5.    <title>bubble event</title>
6.    <style type="text/css">
7.        body{margin:0;}
8.        #one{
9.            width:500px;
10.            height:500px;
11.            background:rgb(255,0,0);
12.            border: 1px solid transparent;
13.        }
14.        #two{
15.            width:400px;
16.            height:400px;
17.            margin: 0 auto;
18.            margin-top: 50px;
19.            background:rgb(255,50,50);
20.            border: 1px solid transparent;
21.        }
22.        #three{
23.            width:300px;
24.            height:300px;
25.            margin: 0 auto;
26.            margin-top: 50px;
27.            background:rgb(255,100,100);
28.            border: 1px solid transparent;
29.        }
30.        #four{
31.            width:200px;
32.            height:200px;
33.            margin: 0 auto;
34.            margin-top: 50px;
35.            background:rgb(255,150,150);
36.        }
37.    </style>
38.</head>
39.<body>
40.    <div id='one'>
41.      <div id='two'>
42.        <div id='three'>
43.          <div id='four'>
44.          </div>
45.        </div>
46.      </div>
47.    </div>
48.
49.    <script>
50.        var one = document.getElementById('one');
51.        var two = document.getElementById('two');
52.        var three = document.getElementById('three');
53.        var four = document.getElementById('four');
54.
55.        var useCapture = false; //false为冒泡获取【目标元素先触发】    true为捕获获取【父级元素先触发】
56.        one.addEventListener('click', function(event) {
57.            event || (event = window.event);
58.            console.log(event);
59.            console.log('one');
60.        }, useCapture);
61.        two.addEventListener('click', function() {
62.            console.log('two');
63.        }, useCapture);
64.        three.addEventListener('click', function() {
65.            console.log('three');
66.        }, useCapture);
67.        four.addEventListener('click', function() {
68.            console.log('four');
69.        }, useCapture);
70.
71.        /*
72.        false
73.        冒泡
74.        点击four div
75.        输出结果：four three two one
76.
77.        true
78.        捕获
79.        点击four div
80.        输出结果： one two three four
81.        */
82.    </script>
83.</body>
84.</html>
```

**注意: 不管是微软的写法还是标准的写法,都支持给一个事件绑定多个函数.并且支持动态的添加和删除事件**

## 3. 关于 event 对象

- 在触发的事件的函数里面我们会接收到一个 event 对象,通过该对象我们需要的一些参数,比如说我们需要知道此事件作用到谁身上了,就可以通过 event 的属性`target`来获取到(IE 暂且不谈),或者想阻止浏览器的默认行为可以通过方法`preventDefault()`来进行阻止.以下是 event 对象的一些属性和方法

| 属性          | 描述                                         |
| ------------- | -------------------------------------------- |
| altKey        | 返回当事件被触发时，”ALT” 是否被按下。       |
| button        | 返回当事件被触发时，哪个鼠标按钮被点击。     |
| clientX       | 返回当事件被触发时，鼠标指针的水平坐标。     |
| clientY       | 返回当事件被触发时，鼠标指针的垂直坐标。     |
| ctrlKey       | 返回当事件被触发时，”CTRL” 键是否被按下。    |
| metaKey       | 返回当事件被触发时，”meta” 键是否被按下。    |
| relatedTarget | 返回与事件的目标节点相关的节点。             |
| screenX       | 返回当某个事件被触发时，鼠标指针的水平坐标。 |
| screenY       | 返回当某个事件被触发时，鼠标指针的垂直坐标。 |
| shiftKey      | 返回当事件被触发时，”SHIFT” 键是否被按下。   |

- `IE` 属性(除了上面的鼠标/事件属性，IE 浏览器还支持下面的属性)

| 属性            | 描述                                                                                   |
| --------------- | -------------------------------------------------------------------------------------- |
| `cancelBubble`  | 如果事件句柄想阻止事件传播到包容对象，必须把该属性设为 true。                          |
| fromElement     | 对于 mouseover 和 mouseout 事件，fromElement 引用移出鼠标的元素。                      |
| keyCode         | 对于 keypress 事件，该属性声明了被敲击的键生成的 Unicode 字符码。对于 keydown 和 keyup |
| offsetX,offsetY | 发生事件的地点在事件源元素的坐标系统中的 x 坐标和 y 坐标。                             |
| `returnValue`   | 如果设置了该属性，它的值比事件句柄的返回值优先级高。把这个属性设置为                   |
| `srcElement`    | 对于生成事件的 Window 对象、Document 对象或 Element 对象的引用。                       |
| toElement       | 对于 mouseover 和 mouseout 事件，该属性引用移入鼠标的元素。                            |
| x,y             | 事件发生的位置的 x 坐标和 y 坐标，它们相对于用 CSS 动态定位的最内层包容元素。          |

- 标准 Event 属性 下面列出了 2 级 DOM 事件标准定义的属性。

| 属性和方法          | 描述                                           |
| ------------------- | ---------------------------------------------- |
| bubbles             | 返回布尔值，指示事件是否是起泡事件类型。       |
| `cancelable`        | 返回布尔值，指示事件是否可拥可取消的默认动作。 |
| `currentTarget`     | 返回其事件监听器触发该事件的元素。             |
| eventPhase          | 返回事件传播的当前阶段。                       |
| `target`            | 返回触发此事件的元素（事件的目标节点）。       |
| timeStamp           | 返回事件生成的日期和时间。                     |
| `type`              | 返回当前 Event 对象表示的事件的名称。          |
| initEvent()         | 初始化新创建的 Event 对象的属性。              |
| `preventDefault()`  | 通知浏览器不要执行与事件关联的默认动作。       |
| `stopPropagation()` | 不再派发事件。                                 |

## 4. Event 对象的一些兼容性写法

- 获得 event 对象兼容性写法
  `event || (event = window.event);`
- 获得 target 兼容型写法
  `event.target||event.srcElement`
- 阻止浏览器默认行为兼容性写法
  `event.preventDefault ? event.preventDefault() : (event.returnValue = false);`
- 阻止冒泡写法
  `event.stopPropagation ? event.stopPropagation() : (event.cancelBubble = true);`
- 注册和删除事件方法的形式

```javascript
1.// 绑定事件.
2.function on(id, eventType, fn) {
3.    var dom = this.isString(id) ? this.$id(id) : id;
4.    if(dom.addEventListener) {
5.        dom.addEventListener(eventType, fn);
6.    } else {
7.        if(dom.attachEvent) {
8.            dom.attachEvent('on' + eventType, fn);
9.        }
10.    }
11.},
12.// 解除绑定
13.function un(id, eventType, fn) {
14.    var dom = this.$id(id);
15.    if(dom.removeEventListener) {
16.        dom.removeEventListener(eventType, fn, false);
17.    } else {
18.        if(dom.detachEvent) {
19.            dom.detachEvent("on" + eventType, fn)
20.        }
21.    }
22.
23.}
```
