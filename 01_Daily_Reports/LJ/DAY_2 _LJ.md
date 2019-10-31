# DAY_2

##  第三章 图形初阶

### 3.1 使用图形

#### 例1

attach(mtcars)     **绑定了数据框mtcars**
plot(wt, mpg)    **打开了一个图形窗口并生成了一幅散点图，横轴表示车身重量，纵轴为每加仑汽油行驶的英里数**
abline(lm(mpg~wt))    **向图形添加了一条最优拟合曲线**
title("Regression of MPG on Weight")    **添加了标题**
detach(mtcars)    **为数据框解除了绑定**

#### 例2 将图形保存到pdf中

pdf("mygraph.pdf")
attach(mtcars)
plot(wt, mpg)
abline(lm(mpg~wt))
title("Regression of MPG on Weight")
detach(mtcars)
dev.off()  

 **将图形保存到当前工作目录中名为mygraph.pdf的PDF文件中**

#### 例3   在创建一幅新图形之前打开一个新的图形窗口  

  dev.new()  

  dev.new()、 dev.next()、 dev.prev()、 dev.set()和dev.off()同时打开多个图形窗口，并选择将哪个输出发送到哪个窗口中  

### 3.2 简单例子

#### 例四   创建描述药物A的剂量和响应关系的图形  

dose <- c(20, 30, 40, 45, 60)
drugA <- c(16, 20, 27, 40, 60)
drugB <- c(15, 18, 25, 31, 40)       **输入数据**

****

  plot(dose, drugA, type="b")     **创建描述药物A的剂量和响应关系的图形**

****

### 3.3 图形参数

#### 例五   实心三角代替空心圆圈，虚线代替实线  

opar <- par(no.readonly=TRUE)
par(lty=2, pch=17)  
plot(dose, drugA, type="b")
par(opar) 

#####   3.3.1 符号和线条  

pch 指定绘制点时使用的==符号==
cex 指定符号的==大小==。 cex 是一个数值，表示绘图符号相对于默认大小的缩放倍数。默认大小为 1， 1.5 表示放大为默认值的 1.5 倍， 0.5 表示缩小为默认值的 50%，等等
lty 指定==线条类型==
lwd 指定==线条宽度==。 lwd 是以默认值的相对大小来表示的（默认值为 1）。例如， lwd=2 将生成一条两倍于默认宽度的线条  

#### 例六

plot(dose, drugA, type="b", lty=3, lwd=3, pch=15, cex=2)  

线条类型为点线，宽度为默认宽度的3倍，点的符号为实心正方形，大小为默认符号大小的2倍。  

#####   3.3.2 颜色  

 col ==默认==的绘图颜色。某些函数（如 lines 和 pie）可以接受一个含有颜色值的向量并自动循环使用。
例如，如果设定 col=c("red", "blue")并需要绘制三条线，则第一条线将为红色，第二条线为蓝色，第三条线又将为红色
col.axis ==坐标轴刻度文字==的颜色
col.lab 坐标轴==标签（名称）==的颜色
col.main ==标题==颜色
col.sub ==副标题==颜色
fg 图形的==前景==色
bg 图形的==背景==色  

#### 例七

library(RColorBrewer)
n <- 7
mycolors <- brewer.pal(n, "Set1")
barplot(rep(1,n), col=mycolors)  

 从Set1调色板中抽取了7种用十六进制表示的颜色并返回一个向量  

#### 例八

n <- 10
mycolors <- rainbow(n)
pie(rep(1, n), labels=mycolors, col=mycolors)
mygrays <- gray(0:n/n)
pie(rep(1, n), labels=mygrays, col=mygrays)

多阶灰度色可使用基础安装所自带的gray()函数生成。

通过一个元素值为0和1之间的向量来指定各颜色的灰度。 gray(0:10/10)将生成10阶灰度色。  

##### 3.3.3 文本属性

cex 表示相对于默认大小缩放倍数的数值。默认大小为 1， 1.5 表示放大为默认值的 1.5 倍， 0.5 表示缩小为默认值的 50%，等等
cex.axis 坐标轴==刻度文字==的缩放倍数。类似于 cex
cex.lab 坐标轴==标签（名称）==的缩放倍数。类似于 cex
cex.main ==标题==的缩放倍数。类似于 cex
cex.sub==副标题==的缩放倍数。类似于 cex

****

font 整数。用于指定==绘图==使用的==字体样式==。 1=常规， 2=粗体， 3=斜体， 4=粗斜体， 5=符号字体（以 Adobe符号编码表示）
font.axis 坐标轴==刻度文字==的字体样式
font.lab 坐标轴==标签（名称）==的字体样式
font.main== 标题==的字体样式
font.sub ==副标题==的字体样式
ps 字体==磅值==（ 1 磅约为 1/72 英寸）。文本的最终大小为 ps*cex
family 绘制文本时使用的==字体族==。标准的取值为 serif（衬线）、 sans（无衬线）和 mono（等宽）

#### 例九

  par(font.lab=3, cex.lab=1.5, font.main=4, cex.main=2)  

创建的所有图形都将拥有斜体、 1.5倍于默认文本大小的坐标轴标签（名称），以及粗斜体、2倍于默认文本大小的标题

##### 3.3.4   图形尺寸与边界尺寸  

  par(pin=c(4,3), mai=c(1,.5, 1, .2))  

  生成一幅4英寸宽、 3英寸高、上下边界为1英寸、左边界为0.5英寸、右边界为0.2英寸的图形  

#### 例十

dose <- c(20, 30, 40, 45, 60)
drugA <- c(16, 20, 27, 40, 60)
drugB <- c(15, 18, 25, 31, 40)
opar <- par(no.readonly=TRUE)
par(pin=c(2, 3))
par(lwd=2, cex=1.5)
par(cex.axis=.75, font.axis=3)
plot(dose, drugA, type="b", pch=19, lty=2, col="red")
plot(dose, drugB, type="b", pch=23, lty=6, col="blue", bg="green")
par(opar)

以向量的形式输入了数据，然后保存了当前的图形参数设置（这样就可以在稍后恢复设置）。修改了默认的图形参数，得到的图形将为2英寸宽、 3英寸高。除此之外，线条的宽度将为默认宽度的两倍，符号将为默认大小的1.5倍。坐标轴刻度文本被设置为斜体、缩小为默认大小的75%。之后，使用红色实心圆圈和虚线创建了第一幅图形，并使用绿色填充的绿色菱形加蓝色边框和蓝色虚线创建了第二幅图形。最后，还原了初始的图形参数设置。  

通过par()设定的参数对两幅图都有效，而在plot()函数中指定的参数仅对特定图形有效  

#### 3.4   添加文本、自定义坐标轴和图例 

#### 例十一

plot(dose, drugA, type="b",col="red", lty=2, pch=2, lwd=2,main="Clinical Trials for Drug A",sub="This is hypothetical data",xlab="Dosage", ylab="Drug Response",xlim=c(0, 60), ylim=c(0, 70))  

添加了标题（ main）、副标题（ sub）、坐标轴标签（ xlab、 ylab）并指定了坐标轴范围（ xlim、 ylim）。  

##### 3.4.1 标题

 使用title()函数为图形添加标题和坐标轴标签 

 调用格式为： title(main="main title", sub="subtitle",xlab="x-axis label", ylab="y-axis label")  

#### 例十二

title(main="My Title", col.main="red",sub="My Subtitle", col.sub="blue",xlab="My X label", ylab="My Y label",
col.lab="green", cex.lab=0.75)  

生成红色的标题和蓝色的副标题，以及比默认大小小25%的绿色x轴、 y轴标签  

##### 3.4.2 坐标轴

可以使用函数axis()来创建自定义的坐标轴，而非使用R中的默认坐标轴。

格式为： axis(side, at=, labels=, pos=, lty=, col=, las=, tck=, ...)  

side 一个整数，表示在图形的哪边绘制坐标轴（ 1=下， 2=左， 3=上， 4=右）

at 一个数值型向量，表示需要绘制刻度线的位置

labels 一个字符型向量，表示置于刻度线旁边的文字标签（如果为 NULL，则将直接使用 at 中的值）

pos 坐标轴线绘制位置的坐标（即与另一条坐标轴相交位置的值）

lty 线条类型

col 线条和刻度线颜色

las 标签是否平行于（ =0）或垂直于（ =2）坐标轴

tck 刻度线的长度，以相对于绘图区域大小的分数表示（负值表示在图形外侧，正值表示在图形内侧， 0
表示禁用刻度， 1 表示绘制网格线）；默认值为–0.01
(…) 其他图形参数  

创建自定义坐标轴时，应当禁用高级绘图函数自动生成的坐标轴。参数axes=FALSE将禁用全部坐标轴（包括坐标轴框架线，除非你添加了参数frame.plot=TRUE）。参数xaxt="n"和yaxt="n"将分别禁用X轴或Y轴（会留下框架线，只是去除了刻度）。  

#### 例十三

x <- c(1:10)
y <- x
z <- 10/x
opar <- par(no.readonly=TRUE)   #生成数据

****

par(mar=c(5, 4, 4, 8) + 0.1)
plot(x, y, type="b",
pch=21, col="red",
yaxt="n", lty=3, ann=FALSE)
lines(x, z, type="b", pch=22, col="blue", lty=2)  #增加边界的大小；绘制X对Y的图形；添加X对1/X的直线

****

axis(2, at=x, labels=x, col.axis="red", las=2)
axis(4, at=z, labels=round(z, digits=2)，col.axis="blue", las=2, cex.axis=0.7, tck=-.01)   #绘制自己的坐标轴

****

mtext("y=1/x", side=4, line=3, cex.lab=1, las=2, col="blue")
title("An Example of Creative Axes",xlab="X values",ylab="Y=X")
par(opar)                #添加标题和文本

****

使用lines()语句，可以为一幅现有图形添加新的图形元素  

函数mtext()用于在图形的边界添加文本  

#####   3.4.3 参考线  

函数abline()可以用来为图形添加参考线。其使用格式为：abline(h=yvalues, v=xvalues)  

函数abline()中也可以指定其他图形参数（如线条类型、颜色和宽度），例如

abline(h=c(1,5,7))在y为1、 5、 7的位置添加了水平实线，

而代码：abline(v=seq(1, 10, 2), lty=2, col="blue")则在x为1、 3、 5、 7、 9的位置添加了垂直的蓝色虚线  。

##### 3.4.4 图例

可以使用函数legend()来添加图例（果然不出所料）。其使用格式为：legend(location, title, legend, ...)  

location 有许多方式可以指定图例的位置。你可以直接给定图例左上角的 x、 y 坐标，也可以执行 locator(1)，然后通过鼠标单击给出图例的位置，还可以使用关键字 bottom、 bottomleft、 left、 topleft、 top、topright、 right、 bottomright 或 center 放置图例。如果你使用了以上某个关键字，那么可以同时使用参数 inset=指定图例向图形内侧移动的大小（以绘图区域大小的分数表示）
title 图例标题的字符串（可选）
legend 图例标签组成的字符型向量… 其他选项。如果图例标示的是颜色不同的线条，需要指定 col=加上颜色值组成的向量。如果图例标示的是符号不同的点，则需指定 pch=加上符号的代码组成的向量。如果图例标示的是不同的线条宽度或线条类型，请使用 lwd=或 lty=加上宽度值或类型值组成的向量。要为图例创建颜色填充的盒形（常见于条形图、箱线图或饼图），需要使用参数 fill=加上颜色值组成的向量。

其他常用的图例选项包括用于指定盒子样式的bty、指定背景色的bg、指定大小的cex，以及指定文本颜色的text.col。指定horiz=TRUE将会水平放置图例，而不是垂直放置。

#### 例十四

dose <- c(20, 30, 40, 45, 60)
drugA <- c(16, 20, 27, 40, 60)
drugB <- c(15, 18, 25, 31, 40)
opar <- par(no.readonly=TRUE)
par(lwd=2, cex=1.5, font.lab=2)  #增加线条、文本、符号、标签的宽度或大小

****

plot(dose, drugA, type="b",pch=15, lty=1, col="red", ylim=c(0, 60),  main="Drug A vs. Drug B", xlab="Drug Dosage", ylab="Drug Response")
lines(dose, drugB, type="b",      pch=17, lty=2, col="blue")
abline(h=c(30), lwd=1.5, lty=2, col="gray")      #绘制图形

****

library(Hmisc)
minor.tick(nx=3, ny=3, tick.ratio=0.5)  #添加次要刻度线

****

legend("topleft", inset=.05, title="Drug Type", c("A","B")
 lty=c(1, 2), pch=c(15, 17), col=c("red", "blue"))   #添加图例

****

par(opar)  

##### 3.4.5 文本标注

text()可向绘图区域内部添加文本，而mtext()则向图形的四个边界之一添加文本。使用格式分别为：
text(location, "text to place", pos, ...)         mtext("text to place", side, line=n, ...)

location 文本的位置参数。可为一对 x、 y 坐标，也可通过指定 location 为 locator(1)使用鼠标交互式地确定摆放位置
pos 文本相对于位置参数的方位。 1=下， 2=左， 3=上， 4=右。 如果指定了 pos，就可以同时指定参数 offset=作为偏移量，以相对于单个字符宽度的比例表示
side 指定用来放置文本的边。 1=下， 2=左， 3=上， 4=右。你可以指定参数 line=来内移或外移文本，随着值的增加，文本将外移。也可使用 adj=0 将文本向左下对齐，或使用 adj=1 右上对齐

除了用来添加文本标注以外， text()函数也通常用来标示图形中的点。

#### 例十五

attach(mtcars)
plot(wt, mpg,     main="Mileage vs. Car Weight",     xlab="Weight", ylab="Mileage",     pch=18, col="blue")
text(wt, mpg,     row.names(mtcars),     cex=0.6, pos=4, col="red")
detach(mtcars)

针对数据框mtcars提供的32种车型的车重和每加仑汽油行驶英里数绘制了散点图。函数text()被用来在各个数据点右侧添加车辆型号。各点的标签大小被缩小了40%，颜色为红色。

#### 例十六

opar <- par(no.readonly=TRUE)
par(cex=1.5)
plot(1:7,1:7,type="n")
text(3,3,"Example of default text")
text(4,4,family="mono","Example of mono-spaced text")
text(5,5,family="serif","Example of serif text")
par(opar)

展示不同字体族的代码

##### 3.4.6 数学标注

函数plotmath()可以为图形主体或边界上的标题、坐标轴名称或文本标注添加数学符号

#### 3.5 图形的组合

在R中使用函数==par()==或==layout()==可以容易地组合多幅图形为一幅总括图形

plot(wt,mpg, main="Scatterplot of wt vs. mpg")
plot(wt,disp, main="Scatterplot of wt vs. disp")
hist(wt, main="Histogram of wt")
boxplot(wt, main="Boxplot of wt")
par(opar)
detach(mtcars)       #  创建了四幅图形并将其排布在两行两列中  

****

attach(mtcars)
opar <- par(no.readonly=TRUE)
par(mfrow=c(3,1))
hist(wt)
hist(mpg)
hist(disp)
par(opar)
detach(mtcars)       #  依三行一列排布三幅图形     #高级绘图函数hist()包含了一个默认的标题（使用  main=""可以禁用它，抑或使用ann=FALSE来禁用所有标题和标签）  

****

attach(mtcars)
layout(matrix(c(1,1,2,3), 2, 2, byrow = TRUE))
hist(wt)
hist(mpg)
hist(disp)
detach(mtcars)   #函数layout()的调用形式为layout(mat)，其中的mat是一个矩阵，它指定了所要组合的多个图形的所在位置。此代码中，一幅图被置于第1行，另两幅图则被置于第2行

****

为了更精确地控制每幅图形的大小，可以有选择地在layout()函数中使用widths=和heights=两个参数。其形式为：
 widths = 各列宽度值组成的一个向量
 heights = 各行高度值组成的一个向量
相对宽度可以直接通过数值指定，绝对宽度（以厘米为单位）可以通过函数lcm()来指定

attach(mtcars)
layout(matrix(c(1, 1, 2, 3), 2, 2, byrow = TRUE),widths=c(3, 1), heights=c(1, 2))
hist(wt)
hist(mpg)
hist(disp)
detach(mtcars)   #  将一幅图形置于第1行，两幅图形置于第2行。但第1行中图形的高度是第2行中图形高度的二分之一。除此之外，右下角图形的宽度是左下角图形宽度的三分之一

##### 图形布局的精细控制  

通过排布或叠加若干图形来创建单幅的、有意义的图形，这需要有对图形布局的精细控制能力，可以使用图形参数fig=完成这个任务

opar <- par(no.readonly=TRUE)
par(fig=c(0, 0.8, 0, 0.8))
plot(mtcars$wt, mtcars$mpg,
     xlab="Miles Per Gallon",
     ylab="Car Weight")   设置散点图

****

par(fig=c(0, 0.8, 0.55, 1), new=TRUE)boxplot(mtcars\$wt, horizontal=TRUE, axes=FALSE)   #在上侧添加箱线图

****

par(fig=c(0.65, 1, 0, 0.8), new=TRUE)boxplot(mtcars$mpg, axes=FALSE)       #在右侧添加箱线图

****

mtext("Enhanced Scatterplot", side=3, outer=TRUE, line=-3)
par(opar) 

第一个fig=将散点图设定为占据横向范围0~0.8，纵向范围0~0.8。上方的箱线图横向占据0~0.8，纵向0.55~1。右侧的箱线图横向占据0.65~1，纵向0~0.8。 fig=默认会新建一幅图形，所以在添加一幅图到一幅现有图形上时，请设定参数new=TRUE。

