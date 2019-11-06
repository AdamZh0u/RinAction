# 第五章 高级数据管理

## 5.1 一个数据处理难题

## 5.2 数值和字符处理函数

### 5.2.1 数学函数

![数学函数](D:%5C%E5%AD%A6%E4%B9%A0%5CR%E8%AF%AD%E8%A8%80%E5%AD%A6%E4%B9%A0%5C%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%5C%E6%95%B0%E5%AD%A6%E5%87%BD%E6%95%B0.jpg)

![#](D:%5C%E5%AD%A6%E4%B9%A0%5CR%E8%AF%AD%E8%A8%80%E5%AD%A6%E4%B9%A0%5C%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%5C%E6%95%B0%E5%AD%A6%E5%87%BD%E6%95%B02.jpg)

### 5.2.2 统计函数

![统计函数](D:%5C%E5%AD%A6%E4%B9%A0%5CR%E8%AF%AD%E8%A8%80%E5%AD%A6%E4%B9%A0%5C%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%5C%E7%BB%9F%E8%AE%A1%E5%87%BD%E6%95%B0.jpg)

## 5.2.3概率函数

![概率分布](D:%5C%E5%AD%A6%E4%B9%A0%5CR%E8%AF%AD%E8%A8%80%E5%AD%A6%E4%B9%A0%5C%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%5C%E6%A6%82%E7%8E%87%E5%88%86%E5%B8%83.jpg)

### 5.2.4 字符处理器

![字符处理函数](2019-11-6%20Day_4_LXX%20163855.assets/%E5%AD%97%E7%AC%A6%E5%A4%84%E7%90%86%E5%87%BD%E6%95%B0.jpg)

### 5.2.5 其他实用函数

![其他实用函数](2019-11-6%20Day_4_LXX%20163855.assets/%E5%85%B6%E4%BB%96%E5%AE%9E%E7%94%A8%E5%87%BD%E6%95%B0.jpg)

### 5.2.6 将函数应用于矩阵和数据框

R中提供了一个apply()函数，可将一个任意函数“应用”到矩阵、数组、数据框的任何维度上

~~~
apply(x, MARGIN, FUN, ...)#x为数据对象，MARGIN是维度的下标，FUN是由你指定的函数，而...则包括了任何想传递给FUN的参数。在矩阵或数据框中，MARGIN=1表示行，MARGIN=2表示列
~~~

## 5.3 数据处理难题的一套解决方案

## 5.4 控制流

### 5.4.1 重复和循环

1. **for**结构

   ~~~
   for (var in seq) statement
   ~~~

2. **while**结构

   ~~~
   while (cond) statement
   ~~~

### 5.4.2 条件执行

1. **if-else**结构

   ~~~
   if (cond) statement
   if (cond) statement1 else statement2
   ~~~

2. **ifelse**结构

   ~~~
   ifelse(cond, statement1, statement2)
   ~~~

3. **switch**结构

   ~~~
   switch(expr, ...)
   > feelings <- c("sad", "afraid") 
   > for (i in feelings) 
    print( 
    switch(i, 
    happy = "I am glad you are happy", 
    afraid = "There is nothing to fear", 
    sad = "Cheer up", 
    angry = "Calm down now" 
    ) 
    ) 
   [1] "Cheer up" 
   [1] "There is nothing to fear"
   ~~~

## 5.5 用户自编函数

~~~
myfunction <- function(arg1, arg2, ... ){ 
statements 
 return(object) 
}
~~~

## 5.6 整合与重构

### 5.6.1 转置

转置（反转行和列）也许是重塑数据集的众多方法中最简单的一个了。使用函数t()即可对一个矩阵或数据框进行转置。对于后者，行名将成为变量（列）名。

### 5.6.2 整合数据

~~~
aggregate(x, by, FUN)#中x是待折叠的数据对象，by是一个变量名组成的列表，这些变量将被去掉以形成新的观测，而FUN则是用来计算描述性统计量的标量函数，它将被用来计算新观测中的值
~~~

### 5.6.3 **reshape2** 包

需要install.packages("reshape2")

1. 融合

   数据集的融合是将它重构为这样一种格式：每个测量变量独占一行，行中带有要唯一确定这个测量所需的标识符变量。

   ~~~
   library(reshape2) 
   md <- melt(mydata, id=c("ID", "Time"))
   ~~~

2. 重铸

   ~~~
   newdata <- dcast(md, formula, fun.aggregate)#的md为已融合的数据，formula描述了想要的最后结果，而fun.aggregate是（可选的）数据整合函数
   ~~~

   