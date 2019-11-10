# DAY_7

## 第七章 基本统计分析

### 任务

学习第七章基本统计分析
 整理几种检验的适用条件

### 重要部分

- 7.1 描述性统计
  - 7.1.3 分组计算描述性统计量
- 7.2 频数表与列联表
  - 7.2.2 独立性检验
  - 7.2.3 相关性的度量
- 7.3 相关
  - 7.3.1 相关的类型
  - 7.3.2 相关性的显著性检验
- 7.4 t检验
  - 7.4.1 独立样本t检验

### 7.1 描述性统计分析

##### 7.1.1 方法云集

#### 例 通过summary()计算描述性统计量

myvars <- c("mpg", "hp", "wt") 
summary(mtcars[myvars])
summary()函数提供了最小值、最大值、四分位数和数值型变量的均值，以及因子向量和逻辑型向量的频数统计。

可以使用apply()函数或sapply()函数计算所选择的任意描述性统计量。
对于sapply()函数，其使用格式为：sapply(x, FUN, options) 
其中的x是数据框（或矩阵），FUN为一个任意的函数。
如果指定了options，它们将被传递给FUN。
可以插入的典型函数有mean()、sd()、var()、min()、max()、median()、length()、range()和quantile()。

#### 例 通过sapply()计算描述性统计量

mystats <- function(x, na.omit=FALSE){ 
  if (na.omit) 
    x <- x[!is.na(x)] 
  m <- mean(x) 
  n <- length(x) 
  s <- sd(x) 
  skew <- sum((x-m)^3/s^3)/n 
  kurt <- sum((x-m)^4/s^4)/n - 3 
  return(c(n=n, mean=m, stdev=s, skew=skew, kurtosis=kurt)) } 
myvars <- c("mpg", "hp", "wt") 
sapply(mtcars[myvars], mystats)
每加仑汽油行驶英里数的平均值为20.1，标准差为6.0。分布呈现右偏（偏度+0.61），并且较正态分布稍平（峰度–0.37）。

##### 7.1.2 更多方法

#### 例 通过Hmisc包中的describe()函数计算描述性统计量

library(Hmisc) 
myvars <- c("mpg", "hp", "wt") 
describe(mtcars[myvars]) 
Hmisc包中的describe()函数可返回变量和观测的数量、缺失值和唯一值的数目、平均值、分位数，以及五个最大的值和五个最小的值。

pastecs包中有一个名为stat.desc()的函数，它可以计算种类繁多的描述性统计量。
使用格式为：stat.desc(x, basic=TRUE, desc=TRUE, norm=FALSE, p=0.95) 
x是一个数据框或时间序列。若basic=TRUE（默认值），则计算其中所有值、空值、缺失值的数量，以及最小值、最大值、值域，还有总和。
若desc=TRUE（同样也是默认值），则计算中位数、平均数、平均数的标准误、平均数置信度为95%的置信区间、方差、标准差以及变异系数。
最后，若norm=TRUE（不是默认的），则返回正态分布统计量，包括偏度和峰度（以及它们的统计显著程度）和Shapiro-Wilk正态检验结果。这里使用了p值来计算平均数的置信区间（默认置信度为0.95）

#### 例 通过pastecs包中的stat.desc()函数计算描述性统计量

library(pastecs) 
myvars <- c("mpg", "hp", "wt") 
stat.desc(mtcars[myvars]) 

可以计算非缺失值的数量、平均数、标准差、中位数、截尾均值、绝对中位差、最小值、最大值、值域、偏度、峰度和平均
值的标准误。

#### 例 通过psych包中的describe()计算描述性统计量

library(psych) 
Attaching package: 'psych' 
The following object(s) are masked from package:Hmisc : 
  describe 
myvars <- c("mpg", "hp", "wt") 
describe(mtcars[myvars])

psych包和Hmisc包均提供了名为describe()的函数。最后载入的程序包优先。在这里，psych在Hmisc之后被载入，然后显示了一条信息，提示Hmisc包中的describe()函数被psych包中的同名函数所屏蔽（masked）。键入describe()后，R在搜索这个函数时将首先找到psych包中的函数并执行它。如果想改而使用Hmisc包中的版本，可以键入misc::describe(mt)。这个函数仍然在那里。只是需要给予R更多信息以找到它。

##### 7.1.3 分组计算描述性统计量

#### 例 使用aggregate()分组获取描述性统计量

myvars <- c("mpg", "hp", "wt") 
aggregate(mtcars[myvars], by=list(am=mtcars\$am), mean) 
aggregate(mtcars[myvars], by=list(am=mtcars\$am), sd) 

aggregate()仅允许在每次调用中使用平均数、标准差这样的单返回值函数。
它无法一次返回若干个统计量。要完成这项任务，可以使用by()函数。格式为：by(data, INDICES, FUN) 
data是一个数据框或矩阵，INDICES是一个因子或因子组成的列表，定义了分组，FUN是任意函数。

#### 例 使用by()分组计算描述性统计量

dstats <- function(x)sapply(x, mystats) 
myvars <- c("mpg", "hp", "wt") 
by(mtcars[myvars], mtcars\$am, dstats) 
dstats()调用了mystats()函数，将其应用于数据框的每一栏中。
再通过by()函数则可得到am中每一水平的概括统计量。

##### 7.1.3 分组计算的扩展

doBy包中summaryBy()函数的使用格式为：summaryBy(formula, data=dataframe, FUN=function)
其中的formula接受以下的格式：
var1+ var2+ var3+ ... + varN~ groupvar1+ groupvar2+ ... + groupvarN
在~左侧的变量是需要分析的数值型变量，而右侧的变量是类别型的分组变量。
function可为任何内建或用户自编的R函数。

#### 例 使用doBy包中的summaryBy()分组计算概述统计量

library(doBy) 
summaryBy(mpg+hp+wt~am, data=mtcars, FUN=mystats) 

psych包中的describeBy()函数可计算和describe()相同的描述性统计量，只是按照一个或多个分组变量分层。

#### 例 使用psych包中的describeBy()分组计算概述统计量

library(psych) 
myvars <- c("mpg", "hp", "wt") 
describeBy(mtcars[myvars], list(am=mtcars\$am))

### 7.2 频数表和列联表

##### 7.2.1 生成频数表

==一维列联表==
可以使用table()函数生成简单的频数统计表。示例如下：
mytable <- with(Arthritis, table(Improved)) 
mytable 

可以用prop.table()将这些频数转化为比例值：
prop.table(mytable) 

或使用prop.table()*100转化为百分比：
prop.table(mytable)*100 

==二维列联表==
对于二维列联表，table()函数的使用格式为：mytable <- table(A, B) 其中的A是行变量，B是列变量。
除此之外，xtabs()函数还可使用公式风格的输入创建列联表，格式为：mytable<- xtabs(~ A+ B, data=mydata) 
其中的mydata是一个矩阵或数据框。总的来说，要进行交叉分类的变量应出现在公式的右侧（即~符号的右方），以+作为分隔符。
若某个变量写在公式的左侧，则其为一个频数向量（在数据已经被表格化时很有用）。
mytable <- xtabs(~ Treatment+Improved, data=Arthritis) 
mytable 

margin.table(mytable, 1)
prop.table(mytable, 1) 
使用margin.table()和prop.table()函数分别生成边际频数和比例，下标1指代table()语句中的第一个变量。

列和与列比例可以这样计算：
margin.table(mytable, 2)
prop.table(mytable, 2)
这里的下标2指代table()语句中的第二个变量。

各单元格所占比例可用如下语句获取
prop.table(mytable) 

可以使用addmargins()函数为这些表格添加边际和
以下代码添加了各行的和与各列的和：
addmargins(mytable)
addmargins(prop.table(mytable)) 

在使用addmargins()时，默认行为是为表中所有的变量创建边际和，作为对照
addmargins(prop.table(mytable, 1), 2) 仅添加了各行的和
addmargins(prop.table(mytable, 2), 1) 添加了各列的和

#### 例 使用CrossTable生成二维列联表

library(gmodels) 
CrossTable(Arthritis\$Treatment, Arthritis\$Improved)

多维列联表
table()和xtabs()都可以基于三个或更多的类别型变量生成多维列联表。
margin.table()、prop.table()和addmargins()函数可以自然地推广到高于二维的情况。
另外，ftable()函数可以以一种紧凑而吸引人的方式输出多维列联表。

#### 例 三维列联表

mytable <- xtabs(~ Treatment+Sex+Improved, data=Arthritis)    #各单元格的频数
mytable
ftable(mytable) 
margin.table(mytable, 1)   #边际频数
margin.table(mytable, 2)   #边际频数
margin.table(mytable, 3)   #边际频数
margin.table(mytable, c(1, 3))  #治疗情况× 改善情况的边际频数
ftable(prop.table(mytable, c(1, 2)))    #治疗情况× 性别的各类改善情况比例 
ftable(addmargins(prop.table(mytable, c(1, 2)), 3)) 
如果想得到百分比而不是比例，可以将结果表格乘以100。例如：
ftable(addmargins(prop.table(mytable, c(1, 2)), 3)) * 100

##### 7.2.2 独立性检验

R提供了多种检验类别型变量独立性的方法。
本节中描述的三种检验分别为卡方独立性检验、Fisher精确检验和Cochran-Mantel-Haenszel检验。

1. 卡方独立性检验
   可以使用chisq.test()函数对二维表的行变量和列变量进行卡方独立性检验。

#### 例 卡方独立性检验

library(vcd) 
mytable <- xtabs(~Treatment+Improved, data=Arthritis) 
chisq.test(mytable)    治疗情况和改善情况不独立

mytable <- xtabs(~Improved+Sex, data=Arthritis) 
chisq.test(mytable)    性别和改善情况独立 

2. Fisher精确检验
   可以使用fisher.test()函数进行Fisher精确检验。
   Fisher精确检验的原假设是：边界固定的列联表中行和列是相互独立的。
   其调用格式为fisher.test(mytable)，其中的mytable是一个二维列联表。
   mytable <- xtabs(~Treatment+Improved, data=Arthritis) 
   fisher.test(mytable)

 3. Cochran-Mantel-Haenszel检验
    mantelhaen.test()函数可用来进行Cochran-Mantel-Haenszel卡方检验，
    其原假设是，两个名义变量在第三个变量的每一层中都是条件独立的。
    下列代码可以检验治疗情况和改善情况在性别的每一水平下是否独立。
    mytable <- xtabs(~Treatment+Improved+Sex, data=Arthritis) 
    mantelhaen.test(mytable) 

##### 7.2.3 相关性的度量

vcd包中的assocstats()函数可以用来计算二维列联表的phi系数、列联系数和Cramer’s V系数。

#### 例 二维列联表的相关性度量

library(vcd) 
mytable <- xtabs(~Treatment+Improved, data=Arthritis) 
assocstats(mytable) 

### 7.3 相关

##### 7.3.1 相关的类型

R可以计算多种相关系数，包括Pearson相关系数、Spearman相关系数、Kendall相关系数、偏相关系数、多分格（polychoric）相关系数和多系列（polyserial）相关系数。

1. Pearson、Spearman和Kendall相关
   Pearson积差相关系数衡量了两个定量变量之间的线性相关程度。
   Spearman等级相关系数则衡量分级定序变量之间的相关程度。
   Kendall’s Tau相关系数也是一种非参数的等级相关度量。 

cor()函数可以计算这三种相关系数，而cov()函数可用来计算协方差。
两个函数的参数有很多，其中与相关系数的计算有关的参数可以简化为：
cor(x, use= , method= ) 
默认参数为use="everything"和method="pearson"。

#### 例 协方差和相关系数

states<- state.x77[,1:6] 
cov(states)
cor(states) 
cor(states, method="spearman")
首个语句计算了方差和协方差，第二个语句则计算了Pearson积差相关系数，而第三个语句计算了Spearman等级相关系数。

x <- states[,c("Population", "Income", "Illiteracy", "HS Grad")] 
y <- states[,c("Life Exp", "Murder")] 
cor(x,y) 

2. 偏相关
   偏相关是指在控制一个或多个定量变量时，另外两个定量变量之间的相互关系。
   可以使用ggm包中的pcor()函数计算偏相关系数。函数调用格式为：pcor(u, S) 
   其中的u是一个数值向量，前两个数值表示要计算相关系数的变量下标，其余的数值为条件变量
   （即要排除影响的变量）的下标。S为变量的协方差阵。
   library(ggm) 
   colnames(states)
   pcor(c(1,5,2,3,6), cov(states)) 

3.其他类型的相关
polycor包中的hetcor()函数可以计算一种混合的相关矩阵，其中包括数值型变量的Pearson积差相关系数、数值型变量和有序变量之间的多系列相关系数、有序变量之间的多分格相关系数以及二分变量之间的四分相关系数。多系列、多分格和四分相关系数都假设有序变量或二分变量由潜在的正态分布导出。

##### 7.3.2 相关性的显著性检验

可以使用cor.test()函数对单个的Pearson、Spearman和Kendall相关系数进行检验。
简化后的使用格式为：cor.test(x, y, alternative = , method = ) 
其中的x和y为要检验相关性的变量，alternative则用来指定进行双侧检验或单侧检验（取值为"two.side"、"less"或"greater"），而method用以指定要计算的相关类型（"pearson"、"kendall"或"spearman"）。当研究的假设为总体的相关系数小于0时，请使用alternative="less"。在研究的假设为总体的相关系数大于0时，应使用alternative="greater"。在默认情况下，假设为alternative="two.side"（总体相关系数不等于0）。

#### 例 检验某种相关系数的显著性

cor.test(states[,3], states[,5]) 

#### 例 通过corr.test计算相关矩阵并进行显著性检验

library(psych) 
corr.test(states, use="complete") 

4. 其他显著性检验
   在多元正态性的假设下，psych包中的pcor.test()函数可以用来检验在控制一个或多个额外变量时两个变量之间的条件独立性。使用格式为：pcor.test(r, q, n) 
   其中的r是由pcor()函数计算得到的偏相关系数，q为要控制的变量数（以数值表示位置），n为样本大小。

### 7.4 t检验

##### 7.4.1 独立样本的t检验

一个针对两组的独立样本t检验可以用于检验两个总体的均值相等的假设。
假设两组数据是独立的，并且是从正态总体中抽得。检验的调用格式为：t.test(y~ x, data) 
其中的y是一个数值型变量，x是一个二分变量。调用格式或为：t.test(y1, y2) 
其中的y1和y2为数值型向量（即各组的结果变量）。可选参数data的取值为一个包含了这些变量的矩阵或数据框。

这里的t检验默认假定方差不相等，并使用Welsh的修正自由度。
可以添加一个参数var.equal=TRUE以假定方差相等，并使用合并方差估计。
默认的备择假设是双侧的（即均值不相等，但大小的方向不确定）。
可以添加一个参数alternative="less"或alternative="greater"来进行有方向的检验。

使用了一个假设方差不等的双侧检验，比较了南方（group 1）和非南方（group 0）各州的监禁概率
library(MASS) 
t.test(Prob ~ So, data=UScrime) 

##### 7.4.2 非独立样本的t检验

非独立样本的t检验假定组间的差异呈正态分布。对于本例，检验的调用格式为：t.test(y1, y2, paired=TRUE) 
其中的y1和y2为两个非独立组的数值向量。

library(MASS) 
sapply(UScrime[c("U1","U2")], function(x)(c(mean=mean(x),sd=sd(x)))) 
with(UScrime, t.test(U1, U2, paired=TRUE))

##### 7.4.3 多于两组的情况

如果能够假设数据是从正态总体中独立抽样而得的，那么可以使用方差分析（ANOVA）

###7.5 组间差异的非参数检验

##### 7.5.1 两组的比较

若两组数据独立，可以使用Wilcoxon秩和检验来评估观测是否是从相同的概率分布中抽得的（即，在一个总体中获得更高得分的概率是否比另一个总体要大）。调用格式为：wilcox.test(y~ x, data) 
其中的y是数值型变量，而x是一个二分变量。调用格式或为：wilcox.test(y1, y2) 
其中的y1和y2为各组的结果变量。可选参数data的取值为一个包含了这些变量的矩阵或数据框。默认进行一个双侧检验。
可以添加参数exact来进行精确检验，指定alternative="less"或alternative="greater"进行有方向的检验。

Wilcoxon符号秩检验是非独立样本t检验的一种非参数替代方法。它适用于两组成对数据和无法保证正态性假设的情境。
调用格式与Mann-Whitney U检验完全相同，不过还可以添加参数paired=TRUE。
sapply(UScrime[c("U1","U2")], median) 
with(UScrime, wilcox.test(U1, U2, paired=TRUE)) 

##### 7.5.2 多于两组的比较

如果各组独立，则Kruskal-Wallis检验将是一种实用的方法。
如果各组不独立（如重复测量设计或随机区组设计），那么Friedman检验会更合适。
Kruskal-Wallis检验的调用格式为：kruskal.test(y~ A, data) 
其中的y是一个数值型结果变量，A是一个拥有两个或更多水平的分组变量（grouping variable）。
（若有两个水平，则它与Mann-Whitney U检验等价。）
Friedman检验的调用格式为：friedman.test(y~ A| B, data) 
其中的y是数值型结果变量，A是一个分组变量，而B是一个用以认定匹配观测的区组变量（blocking variable）。
在以上两例中，data皆为可选参数，它指定了包含这些变量的矩阵或数据框。

states <- data.frame(state.region, state.x77) 
kruskal.test(Illiteracy ~ state.region, data=states) 

#### 例

source("http://www.statmethods.net/RiA/wmc.txt")    得到函数
states <- data.frame(state.region, state.x77) 
wmc(Illiteracy ~ state.region, data=states, method="holm") 
wmc()函数给出了样本量、样本中位数、每组的绝对中位差

