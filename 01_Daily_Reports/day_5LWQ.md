# 基本图形

- ## 条形图

  - 简单条形图

  - 水平条形图：`horiz=TRUE`

    :thinking:等价于ggplot2中 `coord_flip( )`操作

  - 堆砌条形图：矩阵

  - 分组条形图：`beside=TRUE`

  - 均值条形图：将数据整合传递给函数

  - 调整：cex.names 标签字号 ； names.arg 指定字符向量作为条形的标签名

  - 棘状图：library(vcd)中的spine( )

    ![鄱阳湖](鄱阳湖.png)

- ## 饼图

  pie(x,labels)

  - 将四幅图合成一副: `par(mfrow=c(2,2))`

  - 为饼图添加比例数值: lbls2<-paste(lbls," ", pct, "%", sep=" ")

  - 三维饼图: library(plotrix) pie3D

  - 从表格创建饼图

    `mytable<-table(state.region)`

    `lbls3<-paste(names(mytable),"\n", mytable, sep=" ")`

  - 扇形图：library(plotrix) 中的fan.plot( )

    

- ## 直方图

  - 频数hist(x)

  - freq=FALSE表示概率密度

  - 密度曲线 lines( )

  - 数据打结（相同值）: `rug(jitter(mtcars$mpag, amount=0.01)) 为每个数据点添加一个小的随即值

    

![hist](hist.png)

- ## 核密度图

  plot(density(x))

  library(sm) 中的 `sm.density.compare(x,factor)`函数可向图形叠加两组或更多的核密度图



- ## 箱线图:star:

  - 最小值、下四分位数（第25百分位数）、中位数（第50百分位数）、上四分位数（第75百分位数）以及最大值 `boxplot(mtcars$mpg, main="Box plot", ylab="Miles per Gallon")`
  - 并列箱线图：分组`boxplot(formula, data=dataframe)`
  - 含凹槽的箱线图 notch=TRUE
  - 小提琴图（核密度图以镜像方式在箱线图上的叠加）：library(vioplot)中 vioplot(x1, x2, ... , names=, col= )

![figure全局形态](figure全局形态.png)

- ## 点图

  - dotchart(x, labels=)
  - library(Hmisc)中的dotchart2( )

![Figempirical](Figempirical.png)



----

:thinking:插入图片为什么tiff不可以，只能png!