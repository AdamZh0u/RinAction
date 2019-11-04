# DAY 3 R笔记

## Chapter 4 基本数据管理



### 4.2创建新变量

* mydata<-data.frame(x1 = c(2, 2, 6, 4),  

  x2 = c(3, 4, 2, 8)) 

  mydata/$sumx <- mydata$x1 + mydata$x2  

  mydata$meanx <- (mydata$x1 + mydata$x2)/2  

* attach(mydata)  

  mydata$sumx <- x1 + x2  

  mydata$meanx <- (x1 + x2)/2 

  detach(mydata)   

* mydata <- ==transform==(mydata,  

  sumx = x1 + x2,  

  meanx = (x1 + x2)/2) 

### 4.3变量的重编码

语句variable==[==condition==]== <- expression将仅在condition的值为TRUE时执行赋值。

通过创建agecat变量： 

leadership$agecat[leadership$age > 75] <- "Elder"  

leadership$agecat[leadership$age >= 55 &  

 leadership$age <= 75] <- "Middle Aged"  

leadership$agecat[leadership$age < 55] <- "Young" 

也可以通过within函数来简化语句，如

leadership <- within(leadership,=={== 

 agecat <- NA  

 agecat[age > 75] <- "Elder"  

 agecat[age >= 55 & age <= 75] <- "Middle Aged"  

 agecat[age < 55] <- "Young" ==}==) 

注：需先指定好缺失值后，再进行重编码

### 4.4变量的重命名

* 使用语句： fix(leadership)  来调用一个交互式的编辑器。然后单击变量名，在弹出的对话框中将其重命名。

* 通过names()函数来重命名变量。例如： names(leadership)[2] <- "testDate" 

可批量修改多个变量名，如：names(leadership)[6==:==10]<- c("item1", "item2", "item3", "item4", "item5") 

* plyr包中有一个rename()函数，可用于修改变量名。这个函数默认并没有被安装， 所以首先要使用命令install.packages("plyr")对之进行安装。 

rename()函数的使用格式为： rename(*dataframe*, c(*oldname*="*newname*", *oldname*="*newname*",...)) 

### 4.5缺失值

* 缺失值以符号NA（Not Available，不可用）表示。R中字符型和数值 型数据使用的缺失值符号是相同的。 

* 函数is.na()允许你检测缺失值是否存在。 如果某个元素是缺失值，相应的位置将被改写为TRUE，不是缺失值的位置则为FALSE。

  注：*R中行列表示[行，列]，如leadership[,6:10]将数据框限定到第6列至第10列​*

  ​        *R中无法使用比较运算符来检测缺失值是否存在。例如， 逻辑测试myvar == NA的结果永远不会为TRUE。*

  ​       *R 并不把无限的或者不可能出现的数值标记成缺失值。正无穷和负无穷分别用Inf和–Inf所标记。不可能的值（比如说，sin(Inf)）用NaN符号来标记（not a number，不是一个数）。需要用到is.infinite()或is.nan()来识别这些数值。*

* 可以使用赋值语句将某些值重编码为缺失值。如：leadership$age[leadership$age == 99] <- NA 

==含有缺失值的算术表达式和函数的计算结果也是缺失值.==

* 部分数值函数可以通过使用na.rm=TRUE，在计算之前移除缺失值并使用剩余值进行计算： 

  如：x <- c(1, 2, NA, 3)  

  y <- sum(x, na.rm=TRUE)  

  这里，y等于6。 

  在使用函数处理不完整的数据时，需查阅它们的帮助文档（例如，help(sum)），检查 这些函数是如何处理缺失数据的。

* 可以通过函数na.omit()移除所有含有缺失值的观测。na.omit()可以删除所有含有缺失数据的行

### 4.6日期值

函数 ==as.Date()==可以将以字符串形式输入的日期值转化为以数值形式存储的日期变量。其语法为as.Date(x, "*input_format*")，其中x是字符型数 据，*input_format*则给出了用于读入日期的适当格式。具体符号含义参考p76

日期值的默认输入格式为==*yyyy-mm-dd*==。语句： 

mydates <- as.Date(c("2007-06-22", "2004-02-13"))  

将默认格式的字符型数据转换为了对应日期。相反， 

strDates <- c("01/05/1965", "08/16/1975")  

dates <- as.Date(strDates, "%m/%d/%Y")  

则使用==*mm/dd/yyyy*==的格式读取数据。 

* Sys.Date()可以返回当天的日期，而date()则返回当前的日期和时间.可以使用函数format(x, format="output_format")来输出指定格式的日期值，并且 

可以提取日期值中的某些部分

* R的内部在存储日期时，是使用自1970年1月1日以来的天数表示的，更早的日期则表示为负数。可以在日期值上执行算术运算.

* 也可以使用函数difftime()来计算时间间隔，并以星期、天、时、分、秒来表示

函数==as.character()==可将日期值转换为字符型： strDates <- as.character(dates)  

### 4.7类型转换

判断某个对象的数据类型is.datatype()这样的函数返回TRUE或FALSE，而as.datatype()这样的函数则将其参数转换为对应的类型。

### 4.8数据排序

用order()函数对一个数据框进行排序。默认的排序顺序是升序。在排序变量的前边加一个减号即可得到降序的排序结果。可根据多个条件进行排序，

如attach(leadership)  

newdata <-leadership[order(gender, -age),]  

detach(leadership) 

### 4.9数据集合并

* 向数据框添加列 

使用==merge()==函数横向合并两个数据框（数据集）。在多数情况下，两个数据框是通 过一个或多个共有变量进行联结的（即一种内联结，inner join）。例如： total <- merge(dataframeA, dataframeB, by="ID") 

如果要直接横向合并两个矩阵或数据框，并且不需要指定一个公共索引，那么可以直接使 用==cbind()==函数： total <- cbind(A, B)  这个函数将横向合并对象A和对象B。为了让它正常工作，每个对象必须拥有==相同的行数==， 以==同顺序排序==。

* 向数据框添加行 

要纵向合并两个数据框（数据集），请使用rbind()函数： total <- rbind(dataframeA, dataframeB)  

两个数据框必须拥有==相同的变量==，不过它们的顺序不必一定相同。如果dataframeA中拥有 dataframeB中没有的变量，请在合并它们之前做以下某种处理：  删除dataframeA中的多余变量；  在dataframeB中创建追加的变量并将其值设为NA（缺失）。

### 4.10数据集取子集

* 选入（保留）变量时，newdata <- leadership[, c(6:10)]  ，将行下标留空（,）表示默认选择所有行。

* 剔除（丢弃）变量：

  * myvars <- names(leadership)==%in%==c("q3", "q4")  

    newdata <- leadership[==!==myvars] 

  * 已知需剔除的变量是第几个时，在某一列的下标之前加一个==减号==（–）就会剔除那一列。在知道q3和q4是第8个和第9个变量的情况下，可以使用语句： newdata <- leadership[c(-8,-9)] 

  * 相同的变量删除工作亦可通过将其设为==未定义（NULL）==来完成： leadership$q3 <- leadership$q4 <- NULL  

* 使用==subset()==函数选择变量和观测,示例如下： 

  newdata <- subset(leadership, age >= 35 | age < 24,  

   select=c(q1, q2, q3, q4)) 

  (select表示保留这些变量)

* sample()函数从数据集中（有放回或无放回地）抽取大小为n的一个随机样本。 

  如：mysample <- leadership[sample(1:nrow(leadership), 3, replace=FALSE),]  

  sample()函数中的第一个参数是一个由要从中抽样的元素组成的向量。在这里，这个向量 是1到数据框中观测的数量，第二个参数是要抽取的元素数量，第三个参数表示无放回抽样。 sample()函数会返回随机抽样得到的元素，之后即可用于选择数据框中的行。