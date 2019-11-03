# DAY_3

## 第四章  基本数据管理

### 重要部分

4.2 创建新变量与transform使用方法
4.3 within使用方法
4.4 变量的重命名
4.7 类型转换
4.9 向数据框中添加行和列
4.10 **极重要** 常用的数据索引方式与subset函数使用方法 

### 4.2 创建新变量

创建新变量或者对现有的变量进行变换，可以通过此形式的语句完成：变量名 <- 表达式

算术运算符：  \+ 加；– 减；\* 乘；/ 除；^或** 求幂；x%%y 求余（ x mod y）。5%%2 的结果为1；x%/%y 整数除法。5%/%2 的结果为2

#### 例1

假设有一个名为mydata的数据框，其中的变量为x1和x2， 现在想创建一个新变量sumx存储以上两个变量的加和，并创建一个名为meanx的新变量存储这两个变量的均值，  同时将两个新变量整合到原始的数据框中 

mydata<-data.frame(x1 = c(2, 2, 6, 4),x2 = c(3, 4, 2, 8))

****

mydata\$sumx <- mydata​\$x1 + mydata\$x2
mydata\$meanx <- (mydata​\$x1 + mydata​\$x2)/2       第一种方式

****

attach(mydata)
mydata​\$sumx <- x1 + x2
mydata$meanx <- (x1 + x2)/2
detach(mydata)           第二种方式

****

mydata <- transform(mydata,
                    sumx = x1 + x2,
                    meanx = (x1 + x2)/2)            第三种方式（比较重要）

****

### 4.3 变量的重编码

逻辑运算符

< 小于    <= 小于或等于    \> 大于   \> = 大于或等于   \> == 严格等于   \!= 不等于   \!x 非x    x | y x或y   x & y x和y

isTRUE(x) 测试x是否为TRUE

leadership <- within(leadership,{
agecat <- NA
agecat[age > 75] <- "Elder"
agecat[age >= 55 & age <= 75] <- "Middle Aged"
agecat[age < 55] <- "Young" })

首先，创建了agecat变量，并将每一行都设为缺失值。括号中剩下的语句接下来依次执行。

### 4.4 变量的重命名

将变量名manager修改为managerID，并将date修改为testDate，可以使用语句：fix(leadership)

来调用一个交互式的编辑器。然后单击变量名后在弹出的对话框中将其重命名

若以编程方式，可以通过names()函数来重命名变量。例如：names(leadership)[2] <- "testDate"，将重命名date为testDate

names(leadership)[6:10] <- c("item1", "item2", "item3", "item4", "item5")将重命名q1到q5为item1到item5

最后， plyr包中有一个rename()函数，可用于修改变量名。这个函数默认并没有被安装，首先要使用命令install.packages("plyr")对之进行安装。
rename()函数的使用格式为：rename(dataframe, c(oldname="newname", oldname="newname",...))
这里是一个示例：
library(plyr)
leadership <- rename(leadership,
c(manager="managerID", date="testDate"))

### 4.5 缺失值

在R中，缺失值以符号NA（ Not Available，不可用）表示；R中字符型和数值型数据使用的缺失值符号是相同的

函数is.na()允许你检测缺失值是否存在。
假设你有一个向量：y <- c(1, 2, 3, NA)；然后使用函数：is.na(y)；将返回c(FALSE, FALSE, FALSE, TRUE)。

确定了缺失值的位置以后，进一步分析数据之前应当以某种方式删除缺失值。原因是，含有缺失值的算术表达式和函数的计算结果也是缺失值

x <- c(1, 2, NA, 3)
y <- x[1] + x[2] + x[3] + x[4]
z <- sum(x)
由于x中的第3个元素是缺失值，所以y和z也都是NA（缺失值）。

多数的数值函数都拥有一个na.rm=TRUE选项，可以在计算之前移除缺失值并使用剩余
值进行计算：
x <- c(1, 2, NA, 3)
y <- sum(x, na.rm=TRUE)
这里， y等于6

na.omit()可以删除所有含有缺失数据的行。

### 4.6 日期值

可以使用函数format(x, format="output_format")来输出指定格式的日期值，并且
可以提取日期值中的某些部分：
today <- Sys.Date()
format(today, format="%B %d %Y")
[1] "November 27 2014"
format(today, format="%A")
[1] "Thursday"

Sys.Date()可以返回当天的日期，而date()则返回当前的日期和时间

Sys.Date()
[1] "2014-11-27"
date()
[1] "Fri Nov 27 13:21:54 2014"

startdate <- as.Date("2004-02-13")
enddate <- as.Date("2011-01-22")
days <- enddate - startdate
days
Time difference of 2535 days
显示了2004年2月13日和2011年1月22日之间的天数。

也可以使用函数difftime()来计算时间间隔，并以星期、天、时、分、秒来表示。
today <- Sys.Date()
dob <- as.Date("1956-10-12")
difftime(today, dob, units="weeks")
Time difference of 3033 weeks

as.character()可将日期值转换为字符型：strDates <- as.character(dates)

### 4.7 类型转换

下方函数可以判断数据的类型或者将其转换为指定类型。

判断：is.numeric() 、is.character() 、is.vector() 、is.matrix() 、is.data.frame() 、is.factor() 、is.logical()

转换：as.numeric()、as.character()、as.vector()、as.matrix()、as.data.frame()、as.factor()、 as.logical()

名为is.datatype()这样的函数返回TRUE或FALSE，而as.datatype()这样的函数则将其参数转换为对应的类型。

#### 例

a <- c(1,2,3)
a
[1] 1 2 3
is.numeric(a)
[1] TRUE
is.vector(a)
[1] TRUE
a <- as.character(a)
a
[1] "1" "2" "3"
is.numeric(a)
[1] FALSE
is.vector(a)
[1] TRUE
is.charac
[1] TRUE

### 4.8 数据排序

可以使用order()函数对一个数据框进行排序。默认的排序顺序是升序。在排序变量的前边加一个减号即可得到降序的排序结果

newdata <- leadership[order(leadership$age),]
创建了一个新的数据集，其中各行依经理人的年龄升序排序。语句：
attach(leadership)
newdata <- leadership[order(gender, age),]
detach(leadership)
则将各行依女性到男性、同样性别中按年龄升序排序。
最后，
attach(leadership)
newdata <-leadership[order(gender, -age),]
detach(leadership)
将各行依经理人的性别和年龄降序排序。

### 4.9  数据集的合并

#####   4.9.1 向数据框添加列  

横向合并两个数据框（数据集），请使用merge()函数。在多数情况下，两个数据框是通过一个或多个共有变量进行联结的（即一种内联结， inner join）。例如：
total <- merge(dataframeA, dataframeB, by="ID")
将dataframeA和dataframeB按照ID进行了合并。

total <- merge(dataframeA, dataframeB, by=c("ID","Country"))
将两个数据框按照ID和Country进行了合并。类似的横向联结通常用于向数据框中添加变量

如果要直接横向合并两个矩阵或数据框，并且不需要指定一个公共索引，那么可以直接使用cbind()函数：
total <- cbind(A, B)
这个函数将横向合并对象A和对象B。为了让它正常工作，每个对象必须拥有相同的行数，以同顺序排序。

#####   4.9.2 向数据框添加行  

纵向合并两个数据框（数据集），使用rbind()函数：total <- rbind(dataframeA, dataframeB)
两个数据框必须拥有相同的变量，不过它们的顺序不必一定相同。如果dataframeA中拥有dataframeB中没有的变量，在合并它们之前做以下某种处理：
 删除dataframeA中的多余变量；
 在dataframeB中创建追加的变量并将其值设为NA（缺失）。
纵向联结通常用于向数据框中添加观测

### 4.10   数据集取子集  

##### 4.10.1 选入（保留）变量

newdata <- leadership[, c(6:10)]
从leadership数据框中选择了变量q1、 q2、 q3、 q4和q5，并将它们保存到了数据框newdata中。将行下标留空（ ,）表示默认选择所有行。 语句：
myvars <- c("q1", "q2", "q3", "q4", "q5")
newdata <-leadership[myvars]
实现了等价的变量选择。这里，（引号中的）变量名充当了列的下标，因此选择的列是相同的。
最后，也可以写：
myvars <- paste("q", 1:5, sep="")
newdata <- leadership[myvars]

#####   4.10.2 剔除（丢弃）变量  

可以使用语句：
myvars <- names(leadership) %in% c("q3", "q4")
newdata <- leadership[!myvars]
剔除变量q3和q4

(1) names(leadership) 生 成 了 一 个 包 含 所 有 变 量 名 的 字 符 型 向 量 ：c("managerID","testDate","country","gender","age","q1", "q2","q3","q4","q5")。
(2) names(leadership) %in% c("q3", "q4") 返 回 了 一 个 逻 辑 型 向 量 ，names(leadership)中每个匹配q3或q4的元素的值为TRUE，反之为FALSE： c(FALSE, FALSE,FALSE, FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, FALSE)。
(3) 运算符非（ !）将逻辑值反转： c(TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, FALSE,FALSE, TRUE)。
(4) leadership[c(TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, FALSE, FALSE,TRUE)]选择了逻辑值为TRUE的列，于是q3和q4被剔除了。
在知道q3和q4是第8个和第9个变量的情况下，可以使用语句：newdata <- leadership[c(-8,-9)]将它们剔除。

这种方式的工作原理是，在某一列的下标之前加一个减号（ –）就会剔除那一列。
最后，相同的变量删除工作亦可通过：leadership\$q3 <- leadership\$q4 <- NULL 完成

##### 4.10.3 选入观测

#### 例

newdata <- leadership[1:3,]   选择第1行到第3行（前三个观测）
newdata <- leadership[leadership\$gender\=="M\" \&leadership\$age > 30,]     选择所有30岁以上的男性  

****

attach(leadership)
newdata <- leadership[gender\=='M' & age > 30,]
detach(leadership)      使用了attach()函数，所以不必在变量名前加上数据框名称

****

(1) 逻辑比较leadership\$gender=="M\"生成了向量c(TRUE, FALSE, FALSE, TRUE,FALSE)。
(2) 逻辑比较leadership\$age > 30生成了向量c(TRUE, TRUE, FALSE, TRUE, TRUE)。
(3) 逻辑比较c(TRUE, FALSE, FALSE, TRUE,FALSE) & c(TRUE, TRUE, FALSE, TRUE,TRUE)生成了向量c(TRUE, FALSE, FALSE, TRUE, FALSE)。
(4) leadership[c(TRUE, FALSE, FALSE, TRUE, FALSE),]从数据框中选择了第一个和第四个观测（当对应行的索引是TRUE，这一行被选入；当对应行的索引是FALSE，这一行被剔除）。这就满足了我们的选取准则（ 30岁以上的男性）。

*****

#### 例

leadership\$date <- as.Date(leadership\$date, "%m/%d/%y")  使用格式mm/dd/yy将开始作为字符值读入的日期转换为日期值
startdate <- as.Date("2009-01-01")    创建开始日期
enddate <- as.Date("2009-10-31")     创建结束日期
newdata <- leadership[which(leadership\$date >= startdate & leadership\$date <= enddate),] 
由于as.Date()函数的默认格式就是yyyy-mm-dd，所以无需在这里提供这个参数。

##### 4.10.4 subset()函数

使用subset()函数大概是选择变量和观测最简单的方法
newdata <- subset(leadership, age >= 35 | age < 24,select=c(q1, q2, q3, q4))  
选择所有age值大于等于35或age值小于24的行，保留了变量q1到q4

****

newdata <- subset(leadership, gender=="M" \& age > 25,select=gender:q4)
选择所有25岁以上的男性，并保留了变量gender到q4（ gender、 q4和其间所有列）

****

##### 4.10.5 随机抽样

sample()函数能够从数据集中（有放回或无放回地）抽取大小为n的一个随机样本
可以使用以下语句从leadership数据集中随机抽取一个大小为3的样本：
mysample <- leadership[sample(1:nrow(leadership), 3, replace=FALSE),]
sample()函数中的第一个参数是一个由要从中抽样的元素组成的向量。在这里，这个向量是1到数据框中观测的数量，第二个参数是要抽取的元素数量，第三个参数表示无放回抽样。sample()函数会返回随机抽样得到的元素，之后即可用于选择数据框中的行。

### 4.1 问题解决

manager <- c(1, 2, 3, 4, 5)
date <- c("10/24/08", "10/28/08", "10/1/08", "10/12/08", "5/1/09")
country <- c("US", "US", "UK", "UK", "UK")
gender <- c("M", "F", "F", "M", "F")
age <- c(32, 45, 25, 39, 99)
q1 <- c(5, 3, 3, 3, 2)
q2 <- c(4, 5, 5, 3, 2)
q3 <- c(5, 2, 5, 4, 1)
q4 <- c(5, 5, 5, NA, 2)
q5 <- c(5, 5, 2, NA, 1)
leadership <- data.frame(manager, date, country, gender, age,
q1, q2, q3, q4, q5, stringsAsFactors=FALSE)

1. 五个评分（ q1到q5）需要组合起来，即为每位经理人生成一个==平均==服从程度得分。

2. 在问卷调查中，被调查者经常会跳过某些问题。例如，为4号经理人打分的上司跳过了问题4和问题5。

   你需要一种处理==不完整数据==的方法，同时也需要将99岁这样的年龄值重编码为==缺失值==。

3. 一个数据集中也许会有数百个变量，但你可能仅对其中的一些感兴趣。为了简化问题，我们往往希望创建一个只包含那些==感兴趣变量==的数据集。

4. 既往研究表明，领导行为可能随经理人的年龄而改变，二者存在函数关系。要检验这种观点，你希望将当前的年龄值==重编码==为类别型的年龄组（例如年轻、中年、年长）。

5. 领导行为可能随时间推移而发生改变。你可能想重点研究最近全球金融危机期间的服从行为。为了做到这一点，你希望将研究范围限定在某一个==特定时间段==收集的数据上（比如， 2009年1月1日到2009年12月31日）。   

- 第一个问题

​          leadership <- transform(leadership , meanx = (q1+q2+q3+q4+q5)/5)

- 第二个问题

  newdata <- na.omit(leadership)
  newdata

  ****

  leadership\$age[leadership\$age == 99] <- NA

- 第三个问题

​           newdata <- leadership[row indices感兴趣变量的行, column indices感兴趣变量的列]

- 第四个问题 

  leadership <- within(leadership,{
  agecat <- NA
  agecat[age > 75] <- "Elder"
  agecat[age >= 55 & age <= 75] <- "Middle Aged"
  agecat[age < 55] <- "Young" })

- 第五个问题

  leadership\$date <- as.Date(leadership$date, "%m/%d/%y")
  startdate <- as.Date("2009-01-01")
  enddate <- as.Date("2009-12-31")
  newdata <- leadership[which(leadership\$date >= startdate & leadership\$date <= enddate),]