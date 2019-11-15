# DAY_8

## 第三章 第六章 复习

### 第三章 图形初阶

#### 3.1 

#####  通过代码保存图形

pdf("mygraph.pdf") 
attach(mtcars) 
plot(wt, mpg) 
abline(lm(mpg~wt)) 
title("Regression of MPG on Weight") 
detach(mtcars) 
dev.off() 
也可以使用函数win.metafile()、png()、jpeg()、bmp()、tiff()、xfig()和postscript()将图形保存为其他格式。

可以使用函数dev.new()、dev.next()、dev.prev()、dev.set()和dev.off()
同时打开多个图形窗口，并选择将哪个输出发送到哪个窗口中

不加参数地执行par()将生成一个含有当前图形参数设置的列表。
添加参数no.readonly=TRUE可以生成一个可以修改的当前图形参数列表。

#### 3.3

 图形尺寸与边界大小
 通过par()设定的参数对两幅图都有效，而在plot()函数中指定的参数仅对那个特定图形有效

 #### 3.4

 可以使用title()函数为图形添加标题和坐标轴标签。
 可以使用函数axis()来创建自定义的坐标轴
 函数abline()可以用来为图形添加参考线

 可以通过函数text()和mtext()将文本添加到图形上。
 text()可向绘图区域内部添加文本，而mtext()则向图形的四个边界之一添加文本。

 函数plotmath()可以为图形主体或边界上的标题、坐标轴名称或文本标注添加数学符号。 

 #### 3.5

 可以在par()函数中使用图形参数mfrow=c(nrows, ncols)来创建按行填充的、行数为
nrows、列数为ncols的图形矩阵。另外，可以使用mfcol=c(nrows, ncols)按列填充矩阵。

对图形布局的精细控制可以使用图形参数fig=完成

### 第六章 基本图形

##### 6.1 条形图

若height是一个向量，则它的值就确定了各条形的高度，并将绘制一幅垂直的条形图。
如果height是一个矩阵而不是一个向量，则绘图结果将是一幅堆砌条形图或分组条形图。

##### 6.2 饼图

饼图可由函数pie(x, labels)创建
扇形图是通过plotrix包中的fan.plot()函数实现的。

##### 6.3 直方图

使用hist(x) 函数创建直方图：

##### 6.4 核密度图

绘制密度图的方法（不叠加到另一幅图上方）为：plot(density(x)) 
使用sm包中的sm.density.compare()函数可向图形叠加两组或更多的核密度图。
使用格式为：sm.density.compare(x, factor) 
其中的x是一个数值型向量，factor是一个分组变量。

##### 6.5 箱线图

箱线图可以展示单个变量或分组变量。使用格式为：boxplot(formula, data=dataframe) 

##### 6.6 点图

使用dotchart()函数创建点图，格式为：dotchart(x, labels=) 