# 高级数据管理

## 1.数字和字符处理函数

- 数学函数

  abs( )绝对值 ； sqrt( )平方根 ； ceiling( ) 不小于x的最小整数 ； floor( ) 不大于x的最大整数 ；trunc( )：截取整数部分 ； round(x, digit=n )：四舍五入 为指定为小数 ； signif(x,digits=n): 指定有效数字位 ； cos( ) sin( ) tan( ) acos( ) asin( ) atan( ) ; 双曲cosh( ) sinh( ) tanh( ) ; 反双曲 acos( ) asinh( ) atanh( ) ; log(x,base=n)  ; exp( )

  也可用于矩阵或数据库 

  i.e. `sqrt(c(4,16,25))` 

  `c（2，4，5）`

- 统计函数

  mean( ) ; median( )中位数 ; sd( )标准差 ; var( )方差 ；mad( ) 绝对中位差 ； ==quantile(x, probs)==分位数，i.e. 求x的30%和84%分位点， `y <- quantile(x, c(.3,.84))` ； range( )值域 ； sum( ) ; diff(x, lag=n) 滞后差分 (:partly_sunny: 滞后项一般是指该变量的前一期的值，而差分则是当期值与前一期的值之差 )  ; min( ) max( ) ; scale(x,center=TRUE ,scale=TRUE) ==为数据对象x 按列进行中心化(center=TRUE)或标准化(center=TRUE,scale=TRUE)==

  `newdata <- scale(mydata)*SD + M`

   i.e. `newdata <- transform(mydata, myvar = scale(myvar)*10+50)`

- 概率函数

  [dpqr] distribution_abbreviation( )

  d:密度函数density

  p:分布函数distribution function

  q: 分位数函数 quantile function

  r: 生成随机数(随机偏差)

  ==密度函数（dnorm）、分布函数（pnorm）、分位数函数（qnorm）和随机数生成函数（rnorm）==

  - 常用概率函数

    Beta 分布 beta 

    Logistic 分布 logis
    二项分布 binom 

    多项分布 multinom
    柯西分布 cauchy 

    负二项分布 nbinom
    （非中心）卡方分布 chisq 

    正态分布 norm
    指数分布 exp 

    泊松分布 pois
    F 分布 f 

    Wilcoxon 符号秩分布   signrank
    Gamma 分布 gamma

     t 分布 t
    几何分布 geom 

    均匀分布 unif
    超几何分布 hyper

     Weibull 分布 weibull
    对数正态分布 lnorm 

    Wilcoxon 秩和分布 wilcox

i.e. 在区间[-3,3]上绘制正态曲线

`x <- pretty(c(-3,3), 30)`
`y <- dnorm(x)`
`plot(x, y, type = "l", xlab = "Normal Deviate", ylab = "Density", yaxs = "i" )`

位于z=1.96 左侧的标准正态曲线下方面积是多少？

 `pnorm(1.96)等于0.975`
均值为500，标准差为100 的正态分布的0.9 分位点值为多少？

 `qnorm(.9, mean=500, sd=100)`

`628.16`
生成50 个均值为50，标准差为10 的正态随机数 

`rnorm(50, mean=50, sd=10)`

- 设定随机数种子

runif( )用来生成0到1区间上服从均匀分布的伪随机数

set.seed()显式指定种子，重现结果

- 生成多元正态数据

MASS包中的mvrnorm(n， mean, sigma)函数

n是样本大小，mean为均值向量，而sigma是方差-协方差矩阵（或相关矩阵)

- 字符处理函数

  1. nchar(x) 计算x中的字符数量 

  x <- c("ab", "cde", "fghij") 

  length(x)返回值为 3 

  nchar(x[3])返回值为5 ； 

  2. substr(x, start, stop)==提取或替换==一个字符向量中的子串 

  `x <- "abcdef"`
  `substr(x, 2, 4)返回值为"bcd"  #提取`
  `substr(x, 2, 4) <- "22222"（x 将变成"a222ef"） #替换` ；

  3. grep(pattern, x, ignore. case=FALSE, fixed=FALSE) ：在x 中搜索某种模式；

  4. sub(pattern, replacement, x, ignore.case=FALSE, fixed=FALSE)：在x 中搜索pattern，并以文本replacement 将其替换 ；

  5. strsplit(x, split, fixed=FALSE) ： 在split 处分割字符向量x 中的元素

  i.e. `y <- strsplit("abc", "")`将返回一个含有1 个成分、3 个元素的列表，包含的内容为"a" "b" "c"
  `unlist(y)[2]` 和 `sapply(y, "[", 2)`均会返回"b" ;

  6. paste(…, sep="") :连接字符串，分隔符为sep;
  7. toupper(x) 大写转换
  8. tolower(x) 小写转换

- 其他实用函数

  length(x) ; 

  seq(from, to ,by ) 

  i.e. `indices <- seq(1,10,2)`   

   `c(1, 3, 5, 7, 9)` ; 

  rep(x, n) 将x重复n次; cut(x, n)  将连续型变量x 分割为有着n 个水平的因子；

  pretty(x, n)  创建美观的分割点。通过选取n+1 个等间距的取整值，将一个连续型变量x分割为n 个区间 ； 

  cat(... , file ="myfile", append =FALSE)  连接...中的对象，并将其输出到屏幕上或文件中

 

apply()函数，可将一个任意函数“应用”到矩阵、数组、数据框的任何维度上 apply(x, MARGIN, FUN, ...)

x为数据对象，MARGIN是维度的下标，FUN是由你指定的函数。在矩阵或数据框中，MARGIN=1表示行，MARGIN=2表示列

i.e. 

 `mydata <- matrix(rnorm(30), nrow=6)`

`mydata`
           `[,1]        [,2]     [,3]        [,4]      [,5]`
`[1,] 0.71298 1.368 -0.8320 -1.234 -0.790`
`[2,] -0.15096 -1.149 -1.0001 -0.725 0.506`
`[3,] -1.77770 0.519 -0.6675 0.721 -1.350`
`[4,] -0.00132 -0.308 0.9117 -1.391 1.558`
`[5,] -0.00543 0.378 -0.0906 -1.485 -0.350`
`[6,] -0.52178 -0.539 -1.7347 2.050 1.569`
`apply(mydata, 1, mean)`

`[1] -0.155 -0.504 -0.511 0.154 -0.310 0.165`

`apply(mydata, 2, mean)`
`[1] -0.2907 0.0449 -0.5688 -0.3442 0.1906`
`apply(mydata, 2, mean, trim=0.2)   #计算每列的截尾均值`（截尾均值基于中间60%的数据，最高和最低20%
的值均被忽略）
`[1] -0.1699 0.0127 -0.6475 -0.6575 0.2312`

----

- 数据处理难题的一套解决方法

  options(digits=2)限定输出小数点后数字位数；

  scale( ) 将变量进行标准化，这样每科考试的成绩就都是用单位标准差来表示

`z <- scale(roster[,2:4])`

`z`
`        Math Science English`
`[1,] 0.013 1.078 0.587`
`[2,] 1.143 1.591 0.037`
`[3,] -1.026 -0.847 -0.697`
`[4,] -1.649 -0.590 -1.247`
`[5,] -0.068 -1.489 -0.330`
``[6,] 0.128 -0.205 1.137`
`[7,] -1.049 -0.847 -1.247`
`[8,] 1.432 1.078 1.504`

`[9,] 0.832 0.308 0.954`
`[10,] 0.243 -0.077 -0.697`；

mean()来计算各行的均值以获得综合得分，并使用函数cbind()将其添加到花名册：

`score <- apply(z, 1, mean)`

`roster <- cbind(roster, score)`；

函数quantile(roster$score, c(.8,.6,.4,.2))给出了学生综合得分的百分位数，确定ABCD等级划分；

将学生的百分位数排名重编码为一个新的类别型成绩变量，在数据框roster中创建了变量grade；

数strsplit()以空格为界把学生姓名拆分为姓氏和名字

`name <- strsplit((roster$Student), " ")`

sapply()提取列表中每个成分的第一个元素，放入一个储存名字的向量Firstname，并提取每个成分的第二个元素，放入一个储存姓氏的向量Lastname。

`Firstname <- sapply(name, "[", 1)`

`Lastname <- sapply(name, "[", 2)`
`roster <- cbind(Firstname, Lastname, roster[,-1])`；

使用函数order()依姓氏和名字对数据集进行排序：

`roster[order(Lastname,Firstname),]`
`   Firstname Lastname Math Science English score grade`
`6   Cheryl Cushing 512   85      28     0.35  C`
`1   John   Davis   502   95      25     0.56  B`
`9   Joel   England 573   89      27     0.70  B`
`4   David  Jones   358   82      15    -1.16  F`
`8   Greg   Knox    625   95      30     1.34  A`
`5 Janice Markhammer495   75      20    -0.63  D`
`3 Bullwinkle Moose 412   80      18    -0.86  D`
`10  Mary   Rayburn 522   86      18    -0.18  C` 
`2 Angela  Williams 600   99      22     0.92  A`
`7 Reuven  Ytzrhak  410   80      15    -1.05  F`

----

- 控制流

  - 循环

    - for循环: for (var in seq) statement

    - while : while (cond) statement

      i <- 10
      while (i > 0) {print("Hello"); i <- i - 1}

  - 条件执行

    - if-else:

      if (cond) statement
      if (cond) statement1 else statement2

      i.e. 

      `if (is.character(grade)) grade <- as.factor(grade)`
      `if (!is.factor(grade)) grade <- as.factor(grade) else print("Grade already`is a factor")`

    - ifelse(if-else紧凑向量化版); felse(cond, statement1, statement2) 若cond为TRUE，则执行第一个语句；若cond为FALSE，则执行第二个语句,

      `ifelse(score > 0.5, print("Passed"), print("Failed"))`
      `outcome <- ifelse (score > 0.5, "Passed", "Failed")`

    - swith:  switch(expr, ...) 根据一个表达式的值选择语句执行

----

- 用户自编函数

  i.e.

`mystats <- function(x, parametric=TRUE, print=FALSE) {`
`if (parametric) {`
`center <- mean(x); spread <- sd(x)`
`} else {`
`center <- median(x); spread <- mad(x)`
`}`
`if (print & parametric) {`
`cat("Mean=", center, "\n", "SD=", spread, "\n")`
`} else if (print & !parametric) {`
`cat("Median=", center, "\n", "MAD=", spread, "\n")`
`}`
`result <- list(center=center, spread=spread)`
`return(result)`
`}

- 整合(aggregate与重构(reshape)
  - 转置       函数t()即可对一个矩阵或数据框进行转置。
  - 整合       aggregate(x, by, FUN)

- reshape2包
  - 融合： 数据集的融合是将它重构为这样一种格式：每个测量变量独占一行，行中带有要唯一确定这
    个测量所需的标识符变量        

    melt(mydata, id=c("ID", "Time"))

  - 重铸： dcast( )函数

​                          dcast(md, formula, fun.aggregate)

​               md为已融合的数据，formula描述了想要的最后结果，而fun.aggregate是（可选的）数据整合函数

