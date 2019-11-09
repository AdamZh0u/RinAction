# 第六章 基本图形

## 6.1 条形图

### 6.1.1 简单的条形图

~~~
barplot(height,main=" ",xlab=" ",ylab=" ",horiz=TURE)#height是一个向量或一个矩阵，horiz=TRUE会生成一幅水平条形图
~~~

~~~
plot(因子或有序型因子, horiz=TRUE, main=" ",xlab=" ", ylab=" ")#可生成和barplot一样的条形图
~~~

### 6.1.2堆砌条形图和分组条形图

~~~
barplot(矩阵,main=" ",xlab=" ", ylab=" ",col=c(" "),legend=rownames(矩阵)，beside=FALSE（默认值）)#堆砌条形图，矩阵中的每一列都将生成图中的一个条形，各列中的值将给出堆砌的“子条”的高度。
barplot(矩阵,main=" ",xlab=" ", ylab=" ",col=c(" "),legend=rownames(矩阵), beside=TRUE)#分组条形图，矩阵中的每一列都表示一个分组，各列中的值将
并列而不是堆砌
~~~

### 6.1.3均值条形图

~~~
states <- data.frame(state.region, state.x77)
means <- aggregate(states$Illiteracy, by=list(state.region), FUN=mean)
means <- means[order(means$x),]
barplot(means$x, names.arg=means$Group.1)
title("Mean Illiteracy Rate")#order( )可以排序
~~~

### 6.1.4条形图的微调

~~~
cex.names#减小字号
names.arg#指定一个字符向量作为条形的标签名
par()#能够让你对R的默认图形做出大量修改
~~~

~~~
par(mar=c(5,8,4,2))#增加y边界大小
par(las=2)#旋转条形的标签
counts <- table(Arthritis$Improved)
barplot(counts,
main="Treatment Outcome",
horiz=TRUE,
cex.names=0.8,#缩小字体大小
names.arg=c("No Improvement", "Some Improvement","Marked Improvement"))#修改标签文本
~~~

### 6.1.5 棘状图

棘状图对堆砌条形图进行了重缩放，这样每个条形的高度均为1，每一段的高度即
表示比例。棘状图可由vcd包中的函数spine()绘制。

## 6.2饼图

~~~
pie(x, labels)#绘制饼图，x是一个非负数值向量，表示每个扇形的面积，而labels则是表示各扇形标签的字符型向量
~~~

~~~
fan.plot(x,lables)#绘制扇形图，需要安装plotrix包
~~~

## 6.3 直方图

直方图通过在x轴上将值域分割为一定数量的组，在y轴上显示相应值的频数，展示了连续型变量的分布。可以使用如下函数创建直方图：

~~~
hist(x，freq=FALSE,breaks= ,col= ,xlab= ,main= )#x是一个由数据值组成的数值向量。参数freq=FALSE表示根据概率密度而不是频数绘制图形。参数breaks用于控制组的数量。在定义直方图中的单元时，默认将生成等距切分。
rug(jitter(mtcars$mpg))#添加轴须图
lines(density(mtcars$mpg), col="blue", lwd=2)#添加密度曲线
xfit<-seq(min(x), max(x), length=40)
yfit<-dnorm(xfit, mean=mean(x), sd=sd(x))
yfit <- yfit*diff(h$mids[1:2])*length(x)
lines(xfit, yfit, col="blue", lwd=2)#添加正态曲线
box()#添加外框
~~~

## 6.4 核密度图

核密度估计是用于估计随机变量概率密度函数的一种非参数方法。核密度图不失为一种用来观察连续型变量分布的有效方法。

~~~
plot(density(x))#绘制一副新的核密度图
lines()#向一幅已经存在的图形上叠加一条密度曲线
~~~

~~~
polygon( )#可以填充曲线，根据顶点的x和y坐标绘制多边形
~~~

## 6.5 箱线图

箱线图（又称盒须图）通过绘制连续型变量的五数总括，即最小值、下四分位数（第25百分位数）、中位数（第50百分位数）、上四分位数（第75百分位数）以及最大值，描述了连续型变量的分布。箱线图能够显示出可能为离群点（范围±1.5*IQR以外的值，IQR表示四分位距，即上四分位数与下四分位数的差值）的观测。

~~~
boxplot(mtcars$mpg, main="Box plot", ylab="Miles per Gallon")
~~~

默认情况下，两条须的延伸极限不会超过盒型各端加1.5倍四分位距的范围。此范围以外的值将以点来表示。

### 6.5.1使用并列箱线图进行跨组比较

~~~
boxplot(formula, data=dataframe，（notch=TRUE）,varwidth=TRUE,)#formula是一个公式，dataframe代表提供数据的数据框（或列表），varwidth=TRUE使箱线图的宽度与它们各自的样本大小成正比，notch=TRUE，可以得到含凹槽的箱线图。
~~~

### 6.5.2 小提琴图

小提琴图是箱线图与核密度图的结合，可以使用vioplot包中的vioplot()函数绘制它

~~~
vioplot(x1, x2, ... , names=, col=)#其中x1, x2, ...表示要绘制的一个或多个数值向量（将为每个向量绘制一幅小提琴图）。参数names是小提琴图中标签的字符向量，而col是一个为每幅小提琴图指定颜色的向量。
~~~

## 6.6点图

点图提供了一种在简单水平刻度上绘制大量有标签值的方法。

~~~
dotchart(x, labels=)#创建点图，x是一个数值向量，而labels则是由每个点的标签组成的向量。
~~~

~~~
x <- mtcars[order(mtcars$mpg),]#排序
x$cyl <- factor(x$cyl)#数值转因子
x$color[x$cyl==4] <- "red"
x$color[x$cyl==6] <- "blue"
x$color[x$cyl==8] <- "darkgreen"#添加一个字符型向量（color）到数据框x中，根据cyl的值，它所含的值为"red"、"blue"或"darkgreen"
dotchart(x$mpg,
labels = row.names(x),
cex=.7,
groups = x$cyl,#groups来选定一个因子，用以指定x中元素的分组方式
gcolor = "black",
color = x$color,
pch=19,
main = "Gas Mileage for Car Models\ngrouped by cylinder",
xlab = "Miles Per Gallon")
~~~
