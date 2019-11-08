# DAY_5

## 第六章 基本图形

### 任务

- 学习第六章，掌握基本图形绘制方法
- 参考示例自定义一幅图上传到仓库

### 重要部分

- 6.1 条形图
- 6.3直方图
- 6.5箱线图（重要）
  - 箱线图各部分的意义
  - 6.5.1 并列箱线图的绘制方法
- 6.6 点图

### 6.1 条形图

函数barplot()的最简单用法是：barplot(height)，其中的height是一个向量或一个矩阵。

#### 6.1.1 简单的条形图

若height是一个向量，则它的值就确定了各条形的高度，并将绘制一幅垂直的条形图。
使用选项horiz=TRUE则会生成一幅水平条形图。
也可以添加标注选项。选项main可添加一个图形标题，而选项xlab和ylab则会分别添加x轴和y轴标签。

library(vcd) 
counts <- table(Arthritis$Improved) 
counts 

barplot(counts, main="Simple Bar Plot", xlab="Improvement", ylab="Frequency")      简单条形图
barplot(counts, main="Horizontal Bar Plot",xlab="Frequency", ylab="Improvement", horiz=TRUE)    水平条形图

若要绘制的类别型变量是一个因子或有序型因子，可以使用函数plot()快速创建一幅垂直条形图。
由于Arthritis\$Improved是一个因子，所以代码：
plot(Arthritis\$Improved, main="Simple Bar Plot", xlab="Improved", ylab="Frequency") 
plot(Arthritis\$Improved, horiz=TRUE, main="Horizontal Bar Plot", xlab="Frequency", ylab="Improved") 

#### 6.1.2 堆砌条形图和分组条形图

如果height是一个矩阵而不是一个向量，则绘图结果将是一幅堆砌条形图或分组条形图。
若beside=FALSE（默认值），则矩阵中的每一列都将生成图中的一个条形，各列中的值将给出堆砌的“子条”的高度。
若beside=TRUE，则矩阵中的每一列都表示一个分组，各列中的值将并列而不是堆砌。

library(vcd) 
counts <- table(Arthritis\$Improved, Arthritis\$Treatment) 
counts    治疗类型和改善情况的列联表

可以将此结果绘制为一幅堆砌条形图或一幅分组条形图
barplot(counts, 
        main="Stacked Bar Plot", 
        xlab="Treatment", ylab="Frequency", 
        col=c("red", "yellow","green"), 
        legend=rownames(counts))     堆砌条形图
barplot(counts, 
        main="Grouped Bar Plot", 
        xlab="Treatment", ylab="Frequency", 
        col=c("red", "yellow", "green"), 
        legend=rownames(counts), beside=TRUE)    分组条形图
同时使用col选项为绘制的条形添加了颜色。参数legend.text为图例提供了各条形的标签（仅在height为一个矩阵时有用）。

#### 6.1.3 均值条形图

可以使用数据整合函数并将结果传递给barplot()函数，来创建表示均值、中位数、标准差等的条形图

### 例 排序后均值的条形图

states <- data.frame(state.region, state.x77) 
means <- aggregate(states\$Illiteracy, by=list(state.region), FUN=mean) 
means 
means <- means[order(means\$x),]       将均值从小到大排列
means 
barplot(means\$x, names.arg=means\$Group.1) 
title("Mean Illiteracy Rate")      添加标题
使用title()函数与调用plot()时添加main选项是等价的。
means\$x是包含各条形高度的向量，而添加选项names.arg=means\$Group.1是为了展示标签。

#### 6.1.4 条形图的微调

可以使用参数cex.names来减小字号。将其指定为小于1的值可以缩小标签的大小。
可选的参数names.arg允许你指定一个字符向量作为条形的标签名。
可以使用图形参数辅助调整文本间隔。

### 例 为条形图搭配标签

par(mar=c(5,8,4,2))      增加y边界的大小
par(las=2)             旋转条形的标签
counts <- table(Arthritis\$Improved) 
barplot(counts, 
        main="Treatment Outcome", 
        horiz=TRUE, 
        cex.names=0.8,                    缩小字体，让标签更合适
        names.arg=c("No Improvement", "Some Improvement", 
                    "Marked Improvement"))

#### 6.1.5 棘状图

棘状图对堆砌条形图进行了重缩放，这样每个条形的高度均为1，每一段的高度即表示比例。
棘状图可由vcd包中的函数spine()绘制

library(vcd) 
attach(Arthritis) 
counts <- table(Treatment, Improved) 
spine(counts, main="Spinogram Example") 
detach(Arthritis) 

## 6.2 饼状图

饼图可由此函数创建：pie(x, labels) 
其中x是一个非负数值向量，表示每个扇形的面积，而labels则是表示各扇形标签的字符型向量。

### 例 饼图

par(mfrow=c(2, 2))         将四幅图合并为一幅图
slices <- c(10, 12,4, 16, 8) 
lbls <- c("US", "UK", "Australia", "Germany", "France") 
pie(slices, labels = lbls, 
    main="Simple Pie Chart")        
pct <- round(slices/sum(slices)*100) 
lbls2 <- paste(lbls, " ", pct, "%", sep="") 
pie(slices, labels=lbls2, col=rainbow(length(lbls2)), 
    main="Pie Chart with Percentages")      为饼图添加比例数值
library(plotrix) 
pie3D(slices, labels=lbls,explode=0.1, 
      main="3D Pie Chart ")      三维饼图
mytable <- table(state.region) 
lbls3 <- paste(names(mytable), "\\n", mytable, sep="") 
pie(mytable, labels = lbls3, 
    main="Pie Chart from a Table\\n (with sample sizes)")    从表格创建饼图

扇形图提供了一种同时展示相对数量和相互差异的方法。
在R中，扇形图是通过plotrix包中的fan.plot()函数实现的。 
library(plotrix) 
slices <- c(10, 12,4, 16, 8) 
lbls <- c("US", "UK", "Australia", "Germany", "France") 
fan.plot(slices, labels = lbls, main="Fan Plot") 
扇形的宽度（width）是重要的，而半径并不重要

##  6.3 直方图

直方图通过在x轴上将值域分割为一定数量的组，在y轴上显示相应值的频数，展示了连续型变量的分布。
可以使用此函数创建直方图：hist(x) 

x是一个由数据值组成的数值向量。参数freq=FALSE表示根据概率密度而不是频数绘制图形。
参数breaks用于控制组的数量。在定义直方图中的单元时，默认将生成等距切分。

### 例 直方图

par(mfrow=c(2,2)) 
hist(mtcars\$mpg)          简单直方图
hist(mtcars\$mpg, 
breaks=12, 
col="red", 
xlab="Miles Per Gallon", 
main="Colored histogram with 12 bins")            指定组数、颜色、标签和标题
hist(mtcars\$mpg, 
freq=FALSE, 
breaks=12, 
col="red", 
xlab="Miles Per Gallon", 
main="Histogram, rug plot, density curve") 
rug(jitter(mtcars\$mpg)) 
lines(density(mtcars\$mpg), col="blue", lwd=2)      
保留了上一幅图中的颜色、组数、标签和标题设置，又叠加了一条密度曲线和轴须图（rug plot）
使用lines()函数叠加了这条蓝色、双倍默认线条宽度的曲线
x <- mtcars\$mpg 
h<-hist(x, 
breaks=12, 
col="red", 
xlab="Miles Per Gallon", 
main="Histogram with normal curve and box") 
xfit<-seq(min(x), max(x), length=40) 
yfit<-dnorm(xfit, mean=mean(x), sd=sd(x)) 
yfit <- yfit\*diff(h$mids[1:2])\*length(x) 
lines(xfit, yfit, col="blue", lwd=2) 
box()    添加正态密度曲线和外框 

## 6.4 核密度图

核密度估计是用于估计随机变量概率密度函数的一种非参数方法。
核密度图为一种用来观察连续型变量分布的有效方法。绘制密度图的方法（不叠加到另一幅图上方）为：plot(density(x)) 
x是一个数值型向量。plot()函数会创建一幅新的图形，要向一幅已经存在的图形上叠加一条密度曲线，可使用lines()函数

par(mfrow=c(2,1)) 
d <- density(mtcars\$mpg) 
plot(d)              完全使用默认设置创建最简图形
d <- density(mtcars\$mpg) 
plot(d, main="Kernel Density of Miles Per Gallon")      添加一个标题
polygon(d, col="red", border="blue")                    将曲线修改为蓝色，并使用实心红色填充曲线下方的区域
rug(mtcars\$mpg, col="brown")                           添加棕色的轴须图 

核密度图可用于比较组间差异。使用sm包中的sm.density.compare()函数可向图形叠加两组或更多的核密度图。
使用格式为：sm.density.compare(x, factor) x是一个数值型向量，factor是一个分组变量。

### 例 可比较的核密度图

library(sm) 
attach(mtcars) 
cyl.f <- factor(cyl, levels= c(4,6,8), 
                labels = c("4 cylinder", "6 cylinder", 
                           "8 cylinder"))         创建分组因子
sm.density.compare(mpg, cyl, xlab="Miles Per Gallon") 
title(main="MPG Distribution by Car Cylinders")          绘制密度图
colfill<-c(2:(1+length(levels(cyl.f)))) 
legend(locator(1), levels(cyl.f), fill=colfill)         通过鼠标单击添加图例
detach(mtcars) 

## 6.5 箱线图

箱线图（又称盒须图）通过绘制连续型变量的五数总括，即最小值、下四分位数（第25百分位数）、中位数（第50百分位数）、上四分位数（第75百分位数）以及最大值，描述了连续型变量的分布。
boxplot(mtcars$mpg, main="Box plot", ylab="Miles per Gallon") 

#### 6.5.1 使用并列箱线图进行跨组比较

箱线图可以展示单个变量或分组变量。使用格式为：boxplot(formula, data=dataframe) 
其中的formula是一个公式，dataframe代表提供数据的数据框（或列表）。
参数varwidth=TRUE将使箱线图的宽度与其样本大小的平方根成正比。参数horizontal=TRUE可以反转坐标轴的方向

boxplot(mpg ~ cyl, data=mtcars, 
main="Car Mileage Data", 
xlab="Number of Cylinders", 
ylab="Miles Per Gallon")      使用并列箱线图重新研究了四缸、六缸、八缸发动机对每加仑汽油行驶的英里数的影响

通过添加notch=TRUE，可以得到含凹槽的箱线图。若两个箱的凹槽互不重叠，则表明它们的中位数有显著差异
boxplot(mpg ~ cyl, data=mtcars, 
notch=TRUE, 
varwidth=TRUE, 
col="red", 
main="Car Mileage Data", 
xlab="Number of Cylinders", 
ylab="Miles Per Gallon") 
参数col以红色填充了箱线图，而varwidth=TRUE则使箱线图的宽度与它们各自的样本大小成正比。

### 例 两个交叉因子的箱线图

mtcars\$cyl.f <- factor(mtcars\$cyl, 
                       levels=c(4,6,8), 
                       labels=c("4","6","8"))           创建汽缸数量的因子
mtcars\$am.f <- factor(mtcars\$am, 
                      levels=c(0,1), 
                      labels=c("auto", "standard"))     创建变速箱类型的因子
boxplot(mpg ~ am.f \*cyl.f, 
        data=mtcars, 
        varwidth=TRUE, 
        col=c("gold","darkgreen"), 
        main="MPG Distribution by Auto Type", 
        xlab="Auto Type", ylab="Miles Per Gallon")       生成箱线图 

#### 6.5.2 小提琴图

小提琴图是箱线图与核密度图的结合。可以使用vioplot包中的vioplot()函数绘制它
vioplot()函数的使用格式为：vioplot(x1, x2, ... , names=, col=) 
其中x1, x2, ...表示要绘制的一个或多个数值向量（将为每个向量绘制一幅小提琴图）。
参数names是小提琴图中标签的字符向量，而col是一个为每幅小提琴图指定颜色的向量。

library(vioplot) 
x1 <- mtcars$mpg[mtcars$cyl==4] 
x2 <- mtcars$mpg[mtcars$cyl==6] 
x3 <- mtcars$mpg[mtcars$cyl==8] 
vioplot(x1, x2, x3, 
        names=c("4 cyl", "6 cyl", "8 cyl"), 
        col="gold") 
title("Violin Plots of Miles Per Gallon", ylab="Miles Per Gallon", 
      xlab="Number of Cylinders") 
      
vioplot()函数要求将要绘制的不同组分离到不同的变量中。
小提琴图基本上是核密度图以镜像方式在箱线图上的叠加。
在图中，白点是中位数，黑色盒型的范围是下四分位点到上四分位点，细黑线表示须。外部形状即为核密度估计。

## 6.6 点线图

点图提供了一种在简单水平刻度上绘制大量有标签值的方法。
可以使用dotchart()函数创建点图，格式为：dotchart(x, labels=) 
x是一个数值向量，而labels则是由每个点的标签组成的向量。
可以通过添加参数groups来选定一个因子，用以指定x中元素的分组方式。
如果这样做，则参数gcolor可以控制不同组标签的颜色，cex可以控制标签的大小。

dotchart(mtcars$mpg, labels=row.names(mtcars), cex=.7, 
         main="Gas Mileage for Car Models", 
         xlab="Miles Per Gallon") 
         
###例 分组、排序、着色后的点图
x <- mtcars[order(mtcars\$mpg),]    
根据每加仑汽油行驶英里数（从最低到最高）对数据框mtcars进行排序，结果保存为数据框x
x\$cyl <- factor(x\$cyl)     将数值向量cyl转换为一个因子
x\$color[x\$cyl==4] <- "red" 
x\$color[x\$cyl==6] <- "blue" 
x\$color[x\$cyl==8] <- "darkgreen" 
添加一个字符型向量（color）到数据框x中，根据cyl的值，它所含的值为"red"、"blue"或"darkgreen"
dotchart(x\$mpg, 
         labels = row.names(x),   各数据点的标签取自数据框的行名（车辆型号）
         cex=.7, 
         groups = x\$cyl,           数据点根据汽缸数量分组
         gcolor = "black",          数字4、6和8以黑色显示
         color = x\$color,          点和标签的颜色来自向量color 
         pch=19, 
         main = "Gas Mileage for Car Models\ngrouped by cylinder", 
         xlab = "Miles Per Gallon")