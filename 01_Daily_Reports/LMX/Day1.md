# Day1

## 一.实验一：做一个自己的词云

### 1.步骤

（1）安装与词云有关的**packages**：==wordcloud2==

右下角，packages >> install >> 输入包的名称并安装

![image-20191029163523509](C:\Users\Echo\AppData\Roaming\Typora\typora-user-images\image-20191029163523509.png)

![image-20191029171240431](C:\Users\Echo\AppData\Roaming\Typora\typora-user-images\image-20191029171240431.png)

（2）导出数据为表格：==write.table函数==

```R
write.table(demoFreq,"Demo1.scv",sep=",")
```

​        此时在右下角Files中出现Demo1.scv文件，点击Home之后的`···`，可以查询到Demo1文件所在的位置，在电脑中相应磁盘找到该CSV文件。

![image-20191029172647548](C:\Users\Echo\AppData\Roaming\Typora\typora-user-images\image-20191029172647548.png)

（3）更改csv文件中的词为自己想要的，例：中国省份及城市

（4）运行代码作图

​       代码包括两行：1.提取数据；2.作图

```r
demo<-read.table("Demo2.csv",sep=",")
wordcloud2(data=demo,size=1.6)
```

*\#对代码的理解：wordcloud2对数据demo构建词云，大小为1.6，其中demo的值为表格Demo2.csv中的值，中间进行了提取的操作。*

*\#原始数据为Demo1，为了避免数据覆盖出现问题，不能获得自己构造的词云，另存为Demo2*

## 2.结果

![wordcloud](C:\Users\Echo\Documents\R\Day1-罗明霞\wordcloud.png)

## 二.读书笔记

### 第一章 R语言介绍

1. R语言的主要作用：（1）统计计算；（2）绘图
2. R的优点
   - 免费
   - 兼容各类数据源
   - 计算方法新颖且更新速度快
   - 顶尖制图功能
   - 能够很好的整合进其他语言编写的程序之中
   - 兼容多平台

3. **R的基础知识**

   （1）区分大小写

   （2）数据类型包括：向量、矩阵、数据框与各种列表      *#第二章#*

   （3）功能实现：内置函数、用户自编函数、对对象操作   *\#基本函数默认可用，高级函数需加载程序包#*

   （4）==赋值符号==：<- 而非==，可以反向赋值，x <- rorm(5)等于 rorm(5) >- x

   （5）注释符号：#

4. 相关函数

   （1）帮助函数

   ![image-20191029192745425](C:\Users\Echo\AppData\Roaming\Typora\typora-user-images\image-20191029192745425.png)

   （2）管理工作空间的函数

![image-20191029193743005](C:\Users\Echo\AppData\Roaming\Typora\typora-user-images\image-20191029193743005.png)

（3）图形输出函数

![image-20191029194553080](C:\Users\Echo\AppData\Roaming\Typora\typora-user-images\image-20191029194553080.png)

***

*练习代码清单1-1*

```r
age <- c(1,3,5,2,11,9,3,9,12,3)
weight <- c(4.4,5.3,7.2,5.2,8.5,7.3,6.0,10.4,10.2,6.1)
mean(weight)
sd(weight)
cor(age,weight)
plot(age,weight)
```

![image-20191029194219236](C:\Users\Echo\AppData\Roaming\Typora\typora-user-images\image-20191029194219236.png)

*练习代码清单1-2*

```R
setwd("E:/课外提升/R语言/文件")
options()
options(digits=3)
x <- runif(20)
summary(x)
hist(x)
q()
```

![image-20191029200528486](C:\Users\Echo\AppData\Roaming\Typora\typora-user-images\image-20191029200528486.png)

*练习清单代码1-3*

```R
help.start()
setwd("C:/Users/Echo/Documents")
help.start()
install.packages("vcd")
library(vcd)
help(Arthritis)
Arthritis
example(Arthritis)
q()
```

![image-20191029201117882](C:\Users\Echo\AppData\Roaming\Typora\typora-user-images\image-20191029201117882.png)



## 第二章 创建数据集

#### 2.1数据集的概念

1. R储存数据的对象类型：标量、向量、矩阵、数组、数据框、列表
2. R可以处理的数据类型：数值型、字符型、逻辑型、复数型（虚数）、原生型（字节）

#### 2.2数据结构

1. **向量**（一维数组）

   ```R
   a <- c(1, 2, 5, 3, 6, -2, 4)
   b <- c("one", "two", "three")
   c <- c(TRUE, TRUE, TRUE, FALSE, TRUE, FALSE)
   ```

   这里，a是数值型向量，b是字符型向量，而c是逻辑型向量。

2. **标量**：只含一个元素的向量，以向量形式出现

3. **矩阵**：==matrix()函数==

   ```R
   > cells <- c(1,26,24,68) #定义一个向量cells并赋值
   > rnames <- c("R1", "R2") #设置行标签
   > cnames <- c("C1", "C2") #设置列标签
   > mymatrix <- matrix(cells, nrow=2, ncol=2, byrow=TRUE,dimnames=list(rnames, cnames)) #创建2*2的矩阵，以向量cells按行的方向填充，并将行列命名为设置好的行列标签
   > mymatrix #运行结果
   C1 C2
   R1 1 26
   R2 24 68
   ```

4. 数组：==array()函数==，矩阵只有两个维度，数组的维度可以>2

   ```r
   myarray <- array(vector, dimensions, dimnames) #数据，维度及范围，维度标签
   ```

5. 数据框：==data.frame()函数==，可以包含多种类型的数据，上述四种结构的类型必须统一

   ```r
   > patientID <- c(1, 2, 3, 4)
   > age <- c(25, 34, 28, 52)
   > diabetes <- c("Type1", "Type2", "Type1", "Type1")
   > status <- c("Poor", "Improved", "Excellent", "Poor") #前四行是不同类型的向量
   > patientdata <- data.frame(patientID, age, diabetes, status) #创建包含四个向量的数据框
   > patientdata #运行结果
   patientID age diabetes status
   1 1 25 Type1 Poor
   2 2 34 Type2 Improved
   3 3 28 Type1 Excellent
   4 4 52 Type1 Poor
   ```

6. 因子：==factor()函数==，包含名义型变量和有序型变量

7. 列表：==list()函数==

   *#因子和列表了解不深#*

#### 2.3数据的输入

<u>主要了解了有哪些类型的数据输入，具体操作方法打算遇到相关问题时进行练习</u>

1.键盘输入

（1）文本编辑器：==edit()函数==

```R
mydata <- data.frame(age=numeric(0),gender=character(0),weight=numeric(0)) # 定义数据名称及类型
mydata <- edit(mydata) #进行编辑的命令
```

![image-20191029205628028](C:\Users\Echo\AppData\Roaming\Typora\typora-user-images\image-20191029205628028.png)

2. 将带分隔符的文本文件导入数据

   ![image-20191029210413839](C:\Users\Echo\AppData\Roaming\Typora\typora-user-images\image-20191029210413839.png)

3. 导入excel数据（CSV）
4. 导入XML数据
5. 从网页上抓取数据
6. 导入SPSS数据
7. 导入SAS数据
8. 导入Stata数据
9. 导入NetCDF数据
10. 导入HDF5数据

#### 2.4数据集的标注

1. 变量标签：尽可能短，满足重复性输入的需要；可以用下标代替变量标签来访问
2. 值标签：使用时将可以将复杂的值用简单数字、字母之类的进行代替

#### 2.5处理数据对象的实用函数

| 函数                                                         | 用途                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| length(object) <br/>dim(object) <br/>str(object) <br/>class(object) <br/>mode(object) <br/>names(object) <br/>c(object, object,...) <br/>cbind(object, object, ...) <br/>rbind(object, object, ...) <br/>object <br/>head(object) <br/>tail(object) <br/>ls() <br/> <br/>rm(object, object, ...)<br/>newobject <- edit(object) newobject<br/>fix(object) | 显示对象中元素/成分的数量<br/>显示某个对象的维度<br/>显示某个对象的结构<br/>显示某个对象的类或类型<br/>显示某个对象的模式<br/>显示某对象中各成分的名称<br/> 将对象合并入一个向量<br/>按列合并对象<br/>按行合并对象<br/>输出某个对象<br/>列出某个对象的开始部分<br/>列出某个对象的最后部分<br/>显示当前的对象列表<br/>删除一个或更多个对象。语句rm(list = ls())将<br/>删除当前工作环境中的几乎所有对象<br/>编辑对象并另存为newobject<br/>直接编辑对象 |





 