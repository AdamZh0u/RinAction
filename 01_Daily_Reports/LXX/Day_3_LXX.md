# 第四章 基本数据管理 

## 4.1 一个例子

## 4.2 创建新变量

方法1

~~~
mydata<-data.frame(x1 = c(2, 2, 6, 4),x2 = c(3, 4, 2, 8))
mydata$sumx <- mydata$x1 + mydata$x2
mydata$meanx <- (mydata$x1 + mydata$x2)/2
~~~

方法2

~~~
attach(mydata)
mydata$sumx <- x1 + x2
mydata$meanx <- (x1 + x2)/2
detach(mydata)
~~~

方法3

~~~
mydata <- transform(mydata,
sumx = x1 + x2,
meanx = (x1 + x2)/2)
~~~

## 4.3变量的重编码

特定值设置为缺失值

~~~
leadership$age[leadership$age == 99] <- NA
~~~

数据分类方法1

~~~
leadership$agecat[leadership$age > 75] <- "Elder"
leadership$agecat[leadership$age >= 55 &
leadership$age <= 75] <- "Middle Aged"
leadership$agecat[leadership$age < 55] <- "Young"
~~~

数据分类方法2

~~~
leadership <- within(leadership,{
agecat <- NA
agecat[age > 75] <- "Elder"
agecat[age >= 55 & age <= 75] <- "Middle Aged"
agecat[age < 55] <- "Young" }) #数据分类方法2，agecat只是字符型变量
~~~

## 4.4 变量的重命名

~~~
fix(leadership)#调用交互式编辑器，直接点击命名
~~~

~~~
names(leadership)[2] <- "testDate"#将第二列命名为testdate
names(leadership)[6:10] <- c("item1", "item2", "item3", "item4", "item5")
~~~

~~~
rename(dataframe, c(oldname="newname", oldname="newname",...))#要先install.packages("plyr")
~~~

## 4.5 缺失值

~~~
is.na()#检测缺失值是否存在
na.omit()#移除所有含有缺失值的观测
na.omit()#删除所有含有缺失数据的行
~~~

## 4.6 日期值

~~~
as.Date(x, "input_format")#转化以数值形式储存的日期变量，其中x是字符型数据，input_format则给出了用于读入日期的适当格式
Sys.Date()#可以返回当天的日期
date()#返回当前的日期和时间
format(x, format="output_format")#输出指定格式的日期值
difftime()#计算时间间隔
as.character()#可将日期值转换为字符型
~~~

## 4.7类型转换

~~~
is.datatype()#这样的函数返回TRUE或FALSE
as.datatype()#这样的函数则将其参数转换为对应的类型
~~~

## 4.8 数据排序

~~~
order()#对一个数据框进行排序，默认的排序顺序是升序
~~~

~~~
attach(leadership)
newdata <-leadership[order(gender, -age),]#“-”表示降序
detach(leadership)
~~~

## 4.9 数据集的合并

~~~
merge()#横向合并两个数据框（数据集）
rbind()#纵向合并两个数据框（数据集），要具有相同的变量
~~~

## 4.10数据集取子集

选入

~~~
newdata <- leadership[, c(6:10)]
~~~

剔除

~~~
myvars <- names(leadership) %in% c("q3", "q4")
newdata <- leadership[!myvars]
#剔除变量q3和q4。
~~~

~~~
leadership$q3 <- leadership$q4 <- NULL
~~~

~~~
在知道q3和q4是第8个和第9个变量的情况下，可以使用语句：
newdata <- leadership[c(-8,-9)]
将它们剔除。这种方式的工作原理是，在某一列的下标之前加一个减号（–）就会剔除那一列
~~~

subset函数

~~~
newdata <- subset(leadership, age >= 35 | age < 24,
select=c(q1, q2, q3, q4))#选择所有age值大于或等于35或age值小于24的行，保留变量q1到q4
~~~

~~~
newdata <- subset(leadership, gender=="M" & age > 25,
select=gender:q4)
~~~

随机抽样

~~~
sample()#能够让你从数据集中（有放回或无放回地）抽取大小为n的一个随机样本。
~~~

~~~
mysample <- leadership[sample(1:nrow(leadership), 3, replace=FALSE),]#sample()函数中的第一个参数是一个由要从中抽样的元素组成的向量。在这里，这个向量是1到数据框中观测的数量，第二个参数是要抽取的元素数量，第三个参数表示无放回抽样。sample()函数会返回随机抽样得到的元素，之后即可用于选择数据框中的行。
~~~

















































