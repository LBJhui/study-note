#### echarts x 轴标签文字过多导致显示不全

https://blog.csdn.net/superlover_/article/details/79714823

如图：
![img](https://img-blog.csdn.net/20170330153938697?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2ViaTAwNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

#### 解决办法 1：xAxis.axisLabel 属性

axisLabel 的类型是 object ,主要作用是： 坐标轴刻度标签的相关设置。（当然 yAxis 也是一样有这个属性的）

**[html]** [view plain](https://blog.csdn.net/kebi007/article/details/68488694#) [copy](https://blog.csdn.net/kebi007/article/details/68488694#)

1. axisLabel: {
2. interval:0,
3. rotate:40
4. }

以上就可解决 x 轴文字显示不全并将文字倾斜。如图：

![img](https://img-blog.csdn.net/20170330155103733?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2ViaTAwNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
稍微解释一下

interval

坐标轴刻度标签的显示间隔(在类目轴中有效哦)，默认会采用标签不重叠的方式显示标签（也就是默认会将部分文字显示不全）
可以设置为 0 强制显示所有标签，如果设置为 1，表示隔一个标签显示一个标签，如果为 3，表示隔 3 个标签显示一个标签，以此类推

rotate

标签倾斜的角度，在类目轴的类目标签显示不全时可以通过旋转防止标签重叠（官方这样说的）旋转的角度是-90 到 90 度
问题又来了，这个名称 x 轴的文字如果太长会受到遮挡，还是显示不全，这个时候可以用 grid 属性解决

**[html]** [view plain](https://blog.csdn.net/kebi007/article/details/68488694#) [copy](https://blog.csdn.net/kebi007/article/details/68488694#)

1. grid: {
2. left: '10%',
3. bottom:'35%'
4. },

如图：

![img](https://img-blog.csdn.net/20170330182415737?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2ViaTAwNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

#### 解决办法 2：调用 formatter 文字竖直显示

一般很多人都习惯办法 1 的方式虽然不是很完美，但是在一定程度上还是解决了一些问题。在文字不是非常多的情况下还是可以的，感觉还没第一种方法好

axisLabel 中使用 formatter 回调，formatter 有两个参数，使用方法是这样的 formatter:function(value,index){} ，value 是类目（测试医院 A，人民医院）,index 是类目索引。

**[html]** [view plain](https://blog.csdn.net/kebi007/article/details/68488694#) [copy](https://blog.csdn.net/kebi007/article/details/68488694#)

1. axisLabel: {
2. ​ interval: 0,
3. ​ formatter:function(value)
4. ​ {
5. ​ return value.split("").join("\n");
6. ​ }
7. ​ }

如图：

![img](https://img-blog.csdn.net/20170330183437313?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2ViaTAwNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

文字竖直这个 formatter 实在有点太简单化了，所以我们来做一个两个字的加\n 的换行。formatter 如下：

**[html]** [view plain](https://blog.csdn.net/kebi007/article/details/68488694#) [copy](https://blog.csdn.net/kebi007/article/details/68488694#)

1. axisLabel: {
2. ​ interval: 0,
3. ​ formatter:function(value)
4. ​ {
5. ​ debugger
6. ​ var ret = "";//拼接加\n 返回的类目项
7. ​ var maxLength = 2;//每项显示文字个数
8. ​ var valLength = value.length;//X 轴类目项的文字个数
9. ​ var rowN = Math.ceil(valLength / maxLength); //类目项需要换行的行数
10. ​ if (rowN **>** 1)//如果类目项的文字大于 3,
11. ​ {
12. ​ for (var i = 0; i **<** **rowN**; i++) {
13. ​ var temp = "";//每次截取的字符串
14. ​ var start = i \* maxLength;//开始截取的位置
15. ​ var end = start + maxLength;//结束截取的位置
16. ​ //这里也可以加一个是否是最后一行的判断，但是不加也没有影响，那就不加吧
17. ​ temp = value.substring(start, end) + "\n";
18. ​ ret += temp; //凭借最终的字符串
19. ​ }
20. ​ return ret;
21. ​ }
22. ​ else {
23. ​ return value;
24. ​ }
25. ​ }
26. ​ }

效果如图
![img](https://img-blog.csdn.net/20170330190543779?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2ViaTAwNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

####

####

#### 解决办法 3：X 轴类目项隔一个换行(使用 formatter 中 index 参数)

都是上面的第二种方法是利用 formatter 中的 value 参数实现了文字拼接\n 换行的，但是 index 参数并没有使用，现在我们就一起来使用这两个参数实现隔一个类目项换行。

效果如图：

![img](https://img-blog.csdn.net/20170330193929655?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQva2ViaTAwNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

代码比较简单：

**[html]** [view plain](https://blog.csdn.net/kebi007/article/details/68488694#) [copy](https://blog.csdn.net/kebi007/article/details/68488694#)

1. axisLabel: {
2. ​ interval: 0,
3. ​ formatter:function(value,index)
4. ​ {
5. ​ debugger
6. ​ if (index % 2 != 0) {
7. ​ return '\n\n' + value;
8. ​ }
9. ​ else {
10. ​ return value;
11. ​ }
12. ​ }
13. ​ }
