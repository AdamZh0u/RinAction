### Day 4

#### 5 高级数据管理

##### 5.2 数值和字符处理函数

1.  ==数学函数==

abs(x):绝对值
sqrt(x): 平方根,sqrt(25)返回值为5，和25^(0.5)等价
ceiling(x): 不小于x 的最小整数
floor(x) 不大于x 的最大整数

trunc(x):向0 的方向截取的x 中的整数部分
round(x, digits=n): 将x 舍入为指定位的小数
signif(x, digits=n): 将x 舍入为指定的有效数字位数
cos(x)、sin(x)、tan(x):余弦、正弦和正切
acos(x)、asin(x)、atan(x): 反余弦、反正弦和反正切
cosh(x)、sinh(x)、tanh(x):双曲余弦、双曲正弦和双曲正切
acosh(x)、asinh(x)、atanh(x): 反双曲余弦、反双曲正弦和反双曲正切
log(x,base=n):对x 取以n 为底的对数
log(x)           为了方便起见：
log10(x)       log(x)为自然对数
                     log10(x)为常用对数

exp(x):指数函数

2.  ==统计函数==

mean(x) 平均数
median(x) 中位数
sd(x) 标准差
var(x) 方差
mad(x) 绝对中位差
quantile(x,probs) 求分位数。其中x 为待求分位数的数值型向量，probs 为一个由[0,1]之间的概率值组成的数值向量
range(x) 求值域
sum(x) 求和
diff(x, lag=n) 滞后差分，lag 用以指定滞后几项。默认的lag 值为1
x<- c(1, 5, 23, 29)
min(x) 求最小值
max(x) 求最大值
scale(x,center=TRUE,scale=TRUE)
为数据对象x 按列进行中心化(center=TRUE)或标准化(center=TRUE,scale=TRUE)

3.  ==字符处理函数==

nchar(x) 计算x 中的字符数量

substr(x, start, stop) 提取或替换一个字符向量中的子串

grep(pattern, x, ignore.
case=FALSE, fixed=FALSE) 在x 中搜索某种模式。若fixed=FALSE，则pattern 为一个正则表达式。

sub(pattern, replacement,
x, ignore.case=FALSE,
fixed=FALSE) 在x 中搜索pattern，并以文本replacement 将其替换。

strsplit(x, split,
fixed=FALSE) 在split 处分割字符向量x 中的元素。

paste(…, sep="") 连接字符串，分隔符为sep

toupper(x) 大写转换

tolower(x) 小写转换

4.  ==其他函数==

length(x) 对象x 的长度

seq(from, to, by) 生成一个序列

rep(x, n) 将x 重复n 次

cut(x, n) 将连续型变量x 分割为有着n 个水平的因子

pretty(x, n) 创建美观的分割点

cat(... , file ="myfile",
append =FALSE) 连接...中的对象，并将其输出到屏幕上或文件中

##### 5.3 数据处理难题的一套解决方案

##### 5.4 控制流

1. for结构：for循环重复地执行一个语句，直到某个变量的值不再包含在序列seq中为止
2. while结构：while循环重复地执行一个语句，直到条件不为真为止
3. if-else结构：控制结构if-else在某个给定条件为真时执行语句
4. ifelse结构：ifelse结构是if-else结构比较紧凑的向量化版本
5. switch结构：switch根据一个表达式的值选择语句执行

##### 5.5 用户自编函数

1. 使用函数warning()来生成一条错误提示信息
2. 用message()来生成一条诊断信息
3. 用stop()停止当前表达式的执行并提示错误

##### 5.6 整合与重构

1. 转置：使用函数t()即可对一个矩阵或数据框进行转置
2. 整合数据

``` R
aggregate(x, by, FUN)
```

*x是待折叠的数据对象，by是一个变量名组成的列表，这些变量将被去掉以形成新的观测，而FUN则是用来计算描述性统计量的标量函数*

3. Reshape2包

* 融合

``` R
library(reshape2)
md <- melt(mydata, id=c("ID", "Time"))
```

* 重铸

``` R
newdata <- dcast(md, formula, fun.aggregate)
```

*md为已融合的数据，formula描述了想要的最后结果，而fun.aggregate是（可选的）数据整合函数*

