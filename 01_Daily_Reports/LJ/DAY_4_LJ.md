# DAY_4

## 第五章 高级数据管理

### 任务

学习第五章，掌握常用数据方法；

读懂5.3 数据处理难题的一套解决方案

### 重要部分

​                      5.2 数值和字符处理函数
​                            5.2.2 统计函数
​                            5.2.5 其他实用函数
​                            5.2.6 将函数应用于矩阵和数据框
​                      5.3 数据处理难题的一套解决方案
​                      5.4 控制流
​                      5.5 用户自编函数

### 5.2 数值和字符处理函数

##### 5.2.1 数学函数

abs(x) 绝对值；abs(-4)返回值为 4
sqrt(x) 平方根；sqrt(25)返回值为 5，和 25^(0.5)等价
ceiling(x) 不小于 x 的最小整数；ceiling(3.475)返回值为 4
floor(x) 不大于 x 的最大整数；floor(3.475)返回值为 3
trunc(x) 向 0 的方向截取的 x 中的整数部分；trunc(5.99)返回值为 5
round(x, digits=n) 将 x 舍入为指定位的小数；round(3.475, digits=2)返回值为 3.48
signif(x, digits=n) 将 x 舍入为指定的有效数字位数；signif(3.475, digits=2)返回值为 3.5
cos(x)、 sin(x)、 tan(x) 余弦、正弦和正切；cos(2)返回值为–0.416
acos(x)、 asin(x)、 atan(x) 反余弦、反正弦和反正切；acos(-0.416)返回值为 2
cosh(x)、 sinh(x)、 tanh(x) 双曲余弦、双曲正弦和双曲正切；sinh(2)返回值为 3.627
acosh(x)、 asinh(x)、 atanh(x) 反双曲余弦、反双曲正弦和反双曲正切；asinh(3.627)返回值为 2
log(x,base=n)；log(x)；log10(x)；对 x 取以 n 为底的对数；
为了方便起见：
• log(x)为自然对数
• log10(x)为常用对数
• log(10)返回值为 2.3026
• log10(10)返回值为 1
exp(x) 指数函数；exp(2.3026)返回值为 10

##### 5.2.2 统计函数

mean(x) 平均数；mean(c(1,2,3,4))返回值为 2.5
median(x) 中位数；median(c(1,2,3,4))返回值为 2.5
sd(x) 标准差；sd(c(1,2,3,4))返回值为 1.29
var(x) 方差；var(c(1,2,3,4))返回值为 1.67
mad(x) 绝对中位差（ median absolute deviation）；mad(c(1,2,3,4))返回值为 1.48
quantile(x,probs) 求分位数。其中 x 为待求分位数的数值型向量， probs 为一个由[0,1]之间的概率值组成的数值向量
求 x 的 30%和 84%分位点；y <- quantile(x, c(.3,.84))
range(x) 求值域；x <- c(1,2,3,4)，range(x)返回值为 c(1,4)，diff(range(x))返回值为 3；
sum(x) 求和；sum(c(1,2,3,4))返回值为 10
diff(x, lag=n) 滞后差分， lag 用以指定滞后几项。默认的 lag 值为 1；x<- c(1, 5, 23, 29)，diff(x)返回值为 c(4, 18, 6)
min(x) 求最小值；min(c(1,2,3,4))返回值为 1
max(x) 求最大值；max(c(1,2,3,4))返回值为 4
scale(x,center=TRUE,scale=TRUE)；为数据对象 x 按列进行中心化(center=TRUE)或标准化(center=TRUE,scale=TRUE)；

#### 例 均值和标准差的计算

x <- c(1,2,3,4,5,6,7,8)  输入数据
mean(x)
sd(x)     方法一

****

n <- length(x)
meanx <- sum(x)/n
css <- sum((x - meanx)^2)
sdx <- sqrt(css / (n-1))
meanx
sdx   方法二

****

==数据的标准化问题==需要再仔细看一下

##### 5.2.3 概率函数

==正态分布函数==
密度函数（ dnorm）、分布函数（ pnorm）、分位数函数（ qnorm）和随机数生成函数（ rnorm）

函数runif()可以用来生成0到1区间上服从均匀分布的伪随机数

MASS包中的mvrnorm()函数可以获取来自给定均值向量和协方差阵的多元正态分布的数据
mvrnorm(n, mean, sigma)，其中n是你想要的样本大小， mean为均值向量，而sigma是方差协方差矩阵（或相关矩阵）。

#### 例 生成服从多元正态分布的数据

library(MASS)
options(digits=3)
set.seed(1234)    #设定随机种子
mean <- c(230.7, 146.7, 3.6)
sigma <- matrix(c(15360.8, 6721.2, -47.1,
                    6721.2, 4700.9, -16.5,
                    -47.1, -16.5, 0.3), nrow=3, ncol=3)     #指定均值向量、协方差阵
mydata <- mvrnorm(500, mean, sigma)
mydata <- as.data.frame(mydata)
names(mydata) <- c("y","x1","x2")           #生成数据
dim(mydata)
head(mydata, n=10)          #查看结果
R中的概率函数允许生成模拟数据，这些数据是从服从已知特征的概率分布中抽样而得的。

##### 5.2.4 字符处理函数

具体函数及描述见教材表5-6

##### 5.2.5 其他实用函数

表中的最后一个例子演示了在输出时转义字符的使用方法。 \n表示新行， \t为制表符， \\'为单引号， \b为退格，等等。（键入?Quotes以了解更多。）例如，代码：
name <- "Bob"
cat( "Hello", name, "\b.\n", "Isn\'t R", "\t", "GREAT?\n")
可生成：
Hello Bob.
 Isn't   R   GREAT?

##### 5.2.6   将函数应用于矩阵和数据框  

R函数可以应用到一系列的数据对象上，包括标量、向量、矩阵、数组和数据框。
a <- 5
sqrt(a)     #平方根
b <- c(1.243, 5.654, 2.99)
round(b)    四舍五入
c <- matrix(runif(12), nrow=3)    matrix生成矩阵
c
log(c)
mean(c)

R中提供了apply()函数，可将一个任意函数“应用”到矩阵、数组、数据框的任何维度上。
apply()函数的使用格式为：apply(x, MARGIN, FUN, ...)
其中， x为数据对象， MARGIN是维度的下标， FUN是由你指定的函数，而...则包括了任何想传
递给FUN的参数。在矩阵或数据框中， MARGIN=1表示行， MARGIN=2表示列。
mydata <- matrix(rnorm(30), nrow=6)
mydata
apply(mydata, 1, mean)    计算每行的均值
apply(mydata, 2, mean)    计算每列的均值
apply(mydata, 2, mean, trim=0.2)     计算每行的截尾均值
apply()可把函数应用到数组的某个维度上，而lapply()和sapply()则可将函数应用到列表（ list）上。

### 5.3 数据处理难题的一套解决方案

5.1节中提出的问题是：将学生的各科考试成绩组合为单一的成绩衡量指标，基于相对名次（前20%、下20%、等等）给出从A到F的评分，根据学生姓氏和名字的首字母对花名册进行排序。

options(digits=2)      #options(digits=2)限定了输出小数点后数字的位数，并且让输出更容易阅读
Student <- c("John Davis", "Angela Williams", "Bullwinkle Moose",
               "David Jones", "Janice Markhammer", "Cheryl Cushing",
               "Reuven Ytzrhak", "Greg Knox", "Joel England",
               "Mary Rayburn")
Math <- c(502, 600, 412, 358, 495, 512, 410, 625, 573, 522)
Science <- c(95, 99, 80, 82, 75, 85, 80, 95, 89, 86)
English <- c(25, 22, 18, 15, 20, 28, 15, 30, 27, 18)
roster <- data.frame(Student, Math, Science, English, stringsAsFactors=FALSE)    #数据输入

****

z <- scale(roster[,2:4])   #将变量进行标准化，每科考试的成绩是用单位标准差来表示，而不是以原始的尺度表示
score <- apply(z, 1, mean)     #通过函数mean()来计算各行的均值以获得综合得分
roster <- cbind(roster, score)       #使用函数cbind()将其添加到花名册

****

 y <- quantile(roster$score, c(.8,.6,.4,.2))   #函数quantile()给出综合得分的百分位数。成绩A的分界点为0.74， B的分界点为0.44，等等

****

roster\$grade[score >= y[1]] <- "A"
roster\$grade[score < y[1] \& score >= y[2]] <- "B"
roster\$grade[score < y[2] \& score >= y[3]] <- "C"
roster\$grade[score < y[3] & score >= y[4]] <- "D"
roster\$grade[score < y[4]] <- "F"   
#通过使用逻辑运算符，将学生的百分位数排名重编码为一个新的类别型成绩变量，同时在数据框roster中创建了变量grade  

****

name <- strsplit((roster$Student), " ")    #函 数strsplit()以空格为界把学生姓名拆分为姓氏和名字

****

Lastname <- sapply(name, "[", 2)
Firstname <- sapply(name, "[", 1)
roster <- cbind(Firstname,Lastname, roster[,-1])

使用函数sapply()提取列表中每个成分的第一个元素，放入一个储存名字的向量Firstname，并提取每个成分的第二个元素，放入一个储存姓氏的向量Lastname。 "["是一个可以提取某个对象的一部分的函数——在这里它是用来提取列表name各成分中的第一个或第二个元素的。你将使用cbind()把它们添加到花名册中。由于已经不再需要student变量，可以将其丢弃（在下标中使用–1）

****

roster[order(Lastname,Firstname),]   #使用函数order()依姓氏和名字对数据集进行排序

### 5.4 控制流

重复执行某些语句，或仅在满足特定条件的情况下执行另外的语句

##### 5.4.1 重复和循环

循环结构重复地执行一个或一系列语句，直到某个条件不为真为止。循环结构包括for和while结构。

1. for结构
   for循环重复地执行一个语句，直到某个变量的值不再包含在序列seq中为止。语法为：
   for (var in seq) statement、
2. while结构
   while循环重复地执行一个语句，直到条件不为真为止。语法为：
   while (cond) statement

##### 5.4.2 条件执行

在条件执行结构中，一条或一组语句仅在满足一个指定条件时执行。条件执行结构包括if-else、 ifelse和switch。

1. if-else结构
   控制结构if-else在某个给定条件为真时执行语句。也可以同时在条件为假时执行另外的语
   句。语法为：
   if (cond) statement
   if (cond) statement1 else statement2
2. ifelse结构
   ifelse结构是if-else结构比较紧凑的向量化版本，其语法为：
   ifelse(cond, statement1, statement2)
   在程序的行为是二元时，或者希望结构的输入和输出均为向量时，使用ifelse
3. switch根据一个表达式的值选择语句执行。语法为：
   switch(expr, ...)

#### 例 switch示例

feelings <- c("sad", "afraid")
for (i in feelings)
print(switch(i,happy = "I am glad you are happy",afraid = "There is nothing to fear",sad = "Cheer up",angry = "Calm down now"))
[1] "Cheer up"
[1] "There is nothing to fear"

### 5.5 用户自编函数

#### 例  mystats()：一个由用户编写的描述性统计量计算函数

mystats <- function(x, parametric=TRUE, print=FALSE) 
{if (parametric) { center <- mean(x); spread <- sd(x)}
 else {center <- median(x); spread <- mad(x)}
   if (print & parametric) {cat("Mean=", center, "\n", "SD=", spread, "\n")} 
else if (print & !parametric) {cat("Median=", center, "\n", "MAD=", spread, "\n")}
   result <- list(center=center, spread=spread)
   return(result)}
set.seed(1234)
x <- rnorm(500)   需要生成一些数据（服从正态分布的，大小为500的随机样本）
y <- mystats(x)    y\$center将包含均值（ 0.001 84）， y$spread将包含标准差（ 1.03）
y <- mystats(x, parametric=FALSE, print=TRUE)      #y\$center将包含中位数（ –0.0207）， y\$spread将包含绝对中位差（ 1.001）

#### 例 用户选择输出当天日期的格式

mydate <- function(type="long") 
   {switch(type,
          long = format(Sys.time(), "%A %B %d %Y"),
          short = format(Sys.time(), "%m-%d-%y"),
          cat(type, "is not a recognized type\n"))}
函数cat()仅会在输入的日期格式类型不匹配"long"或"short"时执行
同时，有若干函数可以用来为函数添加错误捕获和纠正功能。可以使用函数warning()来生成一条错误提示信息，用message()来生成一条诊断信息，或用stop()停止当前表达式的执行并提示错误。   

### 5.6 整合与重构

##### 5.6.1 转置

使用函数t()即可对一个矩阵或数据框进行转置。对于后者，行名将成为变量（列）名。

#### 例 数据集的转置

##### 5.6.2 整合数据

在R中使用一个或多个by变量和一个预先定义好的函数来折叠（ collapse）数据是比较容易的。
调用格式为：aggregate(x, by, FUN)
其中x是待折叠的数据对象， by是一个变量名组成的列表，这些变量将被去掉以形成新的观测
而FUN则是用来计算描述性统计量的标量函数，它将被用来计算新观测中的值。

options(digits=3)
attach(mtcars)
aggdata <-aggregate(mtcars, by=list(cyl,gear), FUN=mean, na.rm=TRUE)
aggdata

 Group.1表示汽缸数量（ 4、 6或8）， Group.2代表挡位数（ 3、 4或5）。举例来说，拥有4个汽缸和3个挡位车型的每加仑汽油行驶英里数（ mpg）均值为21.5。
在使用aggregate()函数的时候， by中的变量必须在一个列表中（即使只有一个变量）。可以在列表中为各组声明自定义的名称，例如by=list(Group.cyl=cyl, Group.gears=gear)。

##### 5.6.3 reshape2 包

###### 5.6.3.1 融合

library(reshape2)
md <- melt(mydata, id=c("ID", "Time"))
数据集的融合是将它重构为这样一种格式：每个测量变量独占一行，行中带有要唯一确定这个测量所需的标识符变量。

###### 5.6.3.2 重铸

dcast()函数读取已融合的数据，并使用你提供的公式和一个（可选的）用于整合数据的函数将其重塑。调用格式为：
newdata <- dcast(md, formula, fun.aggregate)
其中的md为已融合的数据， formula描述了想要的最后结果，而fun.aggregate是（可选的）数据整合函数。其接受的公式形如：
rowvar1 + rowvar2 + ... ~ colvar1 + colvar2 + ...
在这一公式中， rowvar1 + rowvar2 + ...定义了要划掉的变量集合，以确定各行的内容，而colvar1 + colvar2 + ...则定义了要划掉的、确定各列内容的变量集合。