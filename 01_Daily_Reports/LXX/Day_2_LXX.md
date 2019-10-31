## 第三章 图形初阶

### 3.1使用图形

1. 简单绘图：

   attach(mtcars)  #绑定数据框mtcars

   plot(wt, mpg)  #散点图

   abline(lm(mpg~wt))#mpg纵坐标，wt横坐标

   title("Regression of MPG on Weight")  #添加最优拟合曲线

   detach(mtcars) #为数据框解除绑定

2. 保存图形：

   pdf("mygraph.pdf")**  #还可以使用函数win.metafile()、png()、jpeg()、bmp()、tiff()、xfig() 和postscript()将图形保存为其他格式

   attach(mtcars)  

   plot(wt, mpg)  

   abline(lm(mpg~wt))  

   title("Regression of MPG on Weight")  

   detach(mtcars)  

   dev.off()

   对于Windows，在图形窗口中选择“文件”→ “另存为”，然后在弹出的对话框中选择想要的格式和保存位置即可

3. 如何创建多个窗口并查看每一个

   第==一==种方法：你可以在创建一幅新图形之前打开一个新的图形窗口： 

   dev.new()  

   statements to create graph 1

   dev.new() 

   statements to create a graph 2

   etc.  

   每一幅新图形将出现在最近一次打开的窗口中

   第==二==种方法：你可以通过图形用户界面来查看多个图形，在Windows上，这个过程分为两步。在打开第一个图形窗口以后，勾选“历史”（History）→“记录”（Recording）。然后使用菜单中的“上一个”（Previous）和“下一个”（Next）来逐个查看已经绘制的图形。

   第==三==种方法：可以使用函数dev.new()、dev.next()、dev.prev()、dev.set()和dev.off()同时打开多个图形窗口，并选择将哪个输出发送到哪个窗口中，此法全平台适用，具体参考help(dev.cur)。

### 3.2 一个简单的例子

1. plot(x, y, type="b") #type="b"同时绘制点和线

### 3.3 图形参数

1. 通过修改称为图形参数的选项来自定义一幅图形的多个特征（字体、颜色、坐标轴、 标签par(*optionname=value*,  optionname=name,...)#不加参数地执行par()将生成一个含有当前图形参数设置的列表。添加参数no.readonly=TRUE可以生成一个可以修改的当前图形参数列表

   opar <- par(no.readonly=TRUE)  #复制了一份当前的图形参数设置

   par(lty=2, pch=17) #将默认的线条类型修改为虚线（lty=2）并将默认的点符号改为了实心三角（pch=17）

   plot(dose, drugA, type="b")  

   par(opar) 

   <u>par( )函数可以多次使用</u>，即par(lty=2, pch=17)也可以写成： 

   par(lty=2)  

   par(pch=17) 

#### 3.3.1 符号和线条

1. pch #指定绘制点时使用的符号

   ![PCH](%E7%AC%AC%E4%B8%89%E7%AB%A0%20%E5%9B%BE%E5%BD%A2%E5%88%9D%E9%98%B6.assets/PCH.jpg)

2. cex 指定符号的大小。cex 是一个数值，表示绘图符号相对于默认大小的缩放倍数。默认大小为 1，1.5表示放大为默认值的 1.5 倍，0.5 表示缩小为默认值的 50%，等等

3. lty 指定线条类型

   ![ITY](%E7%AC%AC%E4%B8%89%E7%AB%A0%20%E5%9B%BE%E5%BD%A2%E5%88%9D%E9%98%B6.assets/ITY.jpg)

4. lwd 指定线条宽度。lwd 是以默认值的相对大小来表示的（默认值为 1）。例如，lwd=2 将生成一条两倍于默认宽度的线条

#### 3.3.2 颜色

1. 指定颜色的参数

   ![指定颜色](%E7%AC%AC%E4%B8%89%E7%AB%A0%20%E5%9B%BE%E5%BD%A2%E5%88%9D%E9%98%B6.assets/%E6%8C%87%E5%AE%9A%E9%A2%9C%E8%89%B2.jpg)

   可以通过颜色下标、颜色名称、十六进制的颜色值、RGB值或HSV值来指定颜色：col=1、col="white"、col="#FFFFFF"、col=rgb(1,1,1)和col=hsv(0,0,1) 都是白色

2. 函数rgb()可基于红－绿－蓝三色值生成颜色，而hsv()则基于色相－ 饱和度－亮度值来生成颜色

3. 函数colors()可以返回所有可用颜色的名称

4. R中也有许多用于创建连续型颜色向量的函数，包括rainbow()、heat.colors()、terrain.colors()、topo.colors()以及cm.colors()

   rainbow(10)#生成10种连续的“彩虹型”颜色
   
5. RColorBrewer#在第一次使用之前先进行下载(install.packages("RColorBrewer"))

   library(RColorBrewer)  

   n <- 7  

   mycolors <- brewer.pal(n, "Set1")  

   barplot(rep(1,n), col=mycolors) #从Set1调色板中抽取了7种用十六进制表示的颜色并返回一个向量

   brewer.pal.info 或 display.brewer.all()在一个显示输出中产生每个调色板的图形

6. 多阶灰度色gray()要通过一个元素值为0和1之间的向量来指定各颜色的灰度

   gray(0:10/10)#生成10阶灰度色

   n <- 10  

   mycolors <- rainbow(n)  

   pie(rep(1, n), labels=mycolors, col=mycolors)  

   mygrays <- gray(0:n/n)  

   pie(rep(1, n), labels=mygrays, col=mygrays) 

#### 3.3.3 文本属性

1. 指定文本大小的参数

   ![指定文本大小参数](%E7%AC%AC%E4%B8%89%E7%AB%A0%20%E5%9B%BE%E5%BD%A2%E5%88%9D%E9%98%B6.assets/%E6%8C%87%E5%AE%9A%E6%96%87%E6%9C%AC%E5%A4%A7%E5%B0%8F%E5%8F%82%E6%95%B0.jpg)

   ![指定文本大小参数2](%E7%AC%AC%E4%B8%89%E7%AB%A0%20%E5%9B%BE%E5%BD%A2%E5%88%9D%E9%98%B6.assets/%E6%8C%87%E5%AE%9A%E6%96%87%E6%9C%AC%E5%A4%A7%E5%B0%8F%E5%8F%82%E6%95%B02-1572507557861.jpg)

#### 3.3.4图形尺寸与边界尺寸

1. 控制图形尺寸和边界大小

   ![控制图形](%E7%AC%AC%E4%B8%89%E7%AB%A0%20%E5%9B%BE%E5%BD%A2%E5%88%9D%E9%98%B6.assets/%E6%8E%A7%E5%88%B6%E5%9B%BE%E5%BD%A2.jpg)

###　3.4 添加文本、自定义坐标轴和图例

1. 标题（main）、副标题（sub）、坐标轴标签（xlab、ylab）并指定了坐标轴范围（xlim、ylim）

   plot(dose, drugA, type="b",
   col="red", lty=2, pch=2, lwd=2,
   main="Clinical Trials for Drug A",
   sub="This is hypothetical data",
   xlab="Dosage", ylab="Drug Response",
   xlim=c(0, 60), ylim=c(0, 70))

#### 3.4.1标题

​	title(main="main title", sub="subtitle",xlab="x-axis label", ylab="y-axis label")

#### 3.4.2 坐标轴

​	axis(side, at=, labels=, pos=, lty=, col=, las=, tck=, ...)

#### 3.4.3 参考线

1. abline(h=yvalues, v=xvalues)

 	2. abline(h=c(1,5,7))#在y为1、5、7的位置添加了水平实线
     abline(v=seq(1, 10, 2), lty=2, col="blue")#在x为1、3、5、7、9的位置添加了垂直的蓝色虚线

#### 3.4.4 图例

​	legend(location, title, legend, ...)、

#### 3.4.5 文本标注

​	text(location, "text to place", pos, ...)#可向绘图区域内部添加文本

​	mtext("text to place", side, line=n, ...)#向图形的四个边界之一添加文本

#### 3.4.6 数学标注

### 3.5 图形的组合

1. 在par()函数中使用图形参数mfrow=c(nrows, ncols)来创建按行填充的、行数为nrows、列数为ncols的图形矩阵。另外，可以使用mfcol=c(nrows, ncols)按列填充矩阵
2. 对于自带标题的高级绘图函数可以使用ann=FALSE来禁用所有标题和标签
3. 函数layout()的调用形式为layout(mat)，其中的mat是一个矩阵，它指定了所要组合的多个图形的所在位置

​	



