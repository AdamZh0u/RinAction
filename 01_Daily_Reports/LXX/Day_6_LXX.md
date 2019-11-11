# 第七章 基本统计分析

## 7.1 描述性统计分析

### 7.1.1 方法云集

1. summary()函数提供了最小值、最大值、四分位数和数值型变量的均值，以及因子向量和逻辑型向量的频数统计。

2. 使用apply()函数或sapply()函数计算所选择的任意描述性统计量。对于sapply()函数，其使用格式为： 

   sapply(*x*, *FUN*, *options*)  

   其中的*x*是你的数据框（或矩阵），*FUN*为一个任意的函数。如果指定了*options*，它们将被传递给*FUN*。你可以在这里插入的典型函数有mean()、sd()、var()、min()、max()、median()、length()、range()和quantile()。

3. fivenum()可返回图基五数总括（Tukey’s five-number summary，即最小值、下四分位数、中位数、上四分位数和最大值）。

4. 偏度和峰度可自定义计算函数。

   ~~~
   mystats <- function(x, na.omit=FALSE){ 
    if (na.omit) 
    x <- x[!is.na(x)] 
    m <- mean(x) 
    n <- length(x) 
    s <- sd(x) 
    skew <- sum((x-m)^3/s^3)/n 
    kurt <- sum((x-m)^4/s^4)/n - 3 
    return(c(n=n, mean=m, stdev=s, skew=skew, kurtosis=kurt)) 
    }
   ~~~

### 7.1.2更多方法

1. 若干用户贡献包都提供了计算描述性统计量的函数，其中包括Hmisc、pastecs和psych。 

2. Hmisc包中的describe()函数可返回变量和观测的数量、缺失值和唯一值的数目、平均值、分位数，以及五个最大的值和五个最小的值。

3. pastecs包中有一个名为stat.desc()的函数，它可以计算种类繁多的描述性统计量。使用格式为： 

   stat.desc(*x*, basic=TRUE, desc=TRUE, norm=FALSE, p=0.95)  

   其中的*x*是一个数据框或时间序列。若basic=TRUE（默认值），则计算其中所有值、空值、缺失值的数量，以及最小值、最大值、值域，还有总和。若desc=TRUE（同样也是默认值），则计算中位数、平均数、平均数的标准误、平均数置信度为95%的置信区间、方差、标准差以及变异系数。最后，若norm=TRUE（不是默认的），则返回正态分布统计量，包括偏度和峰度（以及它们的统计显著程度）和Shapiro-Wilk正态检验结果。这里使用了*p*值来计算平均数的置信区间（默认置信度为0.95）。

4. psych包也拥有一个名为describe()的函数，它可以计算非缺失值的数量、平均数、标准差、中位数、截尾均值、绝对中位差、最小值、最大值、值域、偏度、峰度和平均值的标准误。

### 7.1.3 分组计算描述性统计量

1. 可以使用aggregate()函数来分组获取描述性统计量，aggregate()仅允许在每次调用中使用平均数、标准差这样的单返回值函数，无法一次返回若干个统计量。

2. 使用by()函数可以一次返回若干个统计量，格式为： 

   by(*data*, *INDICES*, *FUN*)  

   其中*data*是一个数据框或矩阵，*INDICES*是一个因子或因子组成的列表，定义了分组，*FUN*是任意函数。

### 7.1.4分组计算的扩展

1. doBy包和psych包也提供了分组计算描述性统计量的函数。

2. doBy包中summaryBy()函数的使用格式为： 

   summaryBy(*formula*, data=*dataframe*, FUN=*function*) 

   其中的*formula*接受以下的格式： 

   *var1* + *var2* + *var3* + ... + *varN* ~ *groupvar1* + *groupvar2* + ... + *groupvarN* 

   在~左侧的变量是需要分析的数值型变量，而右侧的变量是类别型的分组变量。function可为任何内建或用户自编的R函数。

3. psych包中的describeBy()函数可计算和describe()相同的描述性统计量，只是按照一个或多个分组变量分层，describeBy()函数不允许指定任意函数，所以它的普适性较低。

## 7.2 频数表与列联表

### 7.2.1 生成频数表

1. 一维列联表 

   可以使用table()函数生成简单的频数统计表，

   用prop.table()将这些频数转化为比例值，

   用prop.table()*100转化为百分比。

2. 二维列联表

   （1）方法1：对于二维列联表，table()函数的使用格式为： 

   mytable <- table(*A*, *B*)  

   其中的*A*是行变量，*B*是列变量。

   （2）方法2：xtabs()函数还可使用公式风格的输入创建列联表， 格式为： 

   *mytable* <- xtabs(~ *A* + *B*, data=*mydata*)  

   其中的*mydata*是一个矩阵或数据框。总的来说，要进行交叉分类的变量应出现在公式的右侧（即~符号的右方），以+作为分隔符。若某个变量写在公式的左侧，则其为一个频数向量（在数据已经被表格化时很有用)。

   ①可以使用margin.table()和prop.table()函数分别生成边际频数和比例。行和与行比例可以这样计算： 

   \> margin.table(mytable, 1) 

   列和与列比例可以这样计算： 

   \> margin.table(mytable, 2) 

   ②可以使用addmargins()函数为这些表格添加边际和，使用addmargins()时，默认行为是为表中所有的变量创建边际和。

   \> addmargins(prop.table(mytable, 1), 2)  

   仅添加了各行的和。类似地， 

   \> addmargins(prop.table(mytable, 2), 1)   

   添加了各列的和

   （3）方法3：使用gmodels包中的CrossTable()函数是创建二维列联表的第三种方法。CrossTable()函数有很多选项，可以做许多事情：计算（行、列、单元格）的百分比；指定小数位数；进行卡方、Fisher和McNemar独立性检验；计算期望和（皮尔逊、标准化、调整的标准化）残差；将缺失值作为一种有效值；进行行和列标题的标注；生成SAS或SPSS风格的输出。

3. 多维列联表

   ①table() 和 xtabs() 都可以基于三个或更多的类别型变量生成多维列联表。margin.table()、prop.table()和addmargins()函数可以自然地推广到高于二维的情况。

   ②ftable()函数可以以一种紧凑而吸引人的方式输出多维列联表。

   如果想得到百分比而不是比例，可以将结果表格乘以100。例如：ftable(addmargins(prop.table(mytable, c(1, 2)), 3)) * 100

### 7.2.2独立性检验

1. 卡方独立性检验

   使用chisq.test()函数对二维表的行变量和列变量进行卡方独立性检验。

2.  Fisher精确检验 

   可以使用fisher.test()函数进行Fisher精确检验。Fisher精确检验的原假设是：边界固定的列联表中行和列是相互独立的。其调用格式为fisher.test(*mytable*)，其中的*mytable*是 一个二维列联表。

3. Cochran-Mantel-Haenszel检验 

   mantelhaen.test()函数可用来进行Cochran-Mantel-Haenszel卡方检验，其原假设是，两个名义变量在第三个变量的每一层中都是条件独立的。

### 7.2.3 相关性的度量

1. vcd包中的assocstats()函数可以用来计算二维列联表的phi系数、列联系数和Cramer’s V系数。
2. vcd包也提供了一个kappa()函数，可以计算混淆矩阵的Cohen’s kappa值以及加权的kappa值。

## 7.3 相关

### 7.3.1 相关的类型

1. Pearson、Spearman和Kendall相关 

   ①Pearson积差相关系数衡量了两个定量变量之间的线性相关程度。Spearman等级相关系数则衡量分级定序变量之间的相关程度。Kendall’s Tau相关系数也是一种非参数的等级相关度量。

   ②cor()函数可以计算这三种相关系数，而cov()函数可用来计算协方差。两个函数的参数有很多，其中与相关系数的计算有关的参数可以简化为：cor(x, use= , method= )

   ![cor和cov参数](Day_6_LXX.assets/cor%E5%92%8Ccov%E5%8F%82%E6%95%B0.jpg)

2. 偏相关

   偏相关是指在控制一个或多个定量变量时，另外两个定量变量之间的相互关系。你可以使用ggm包中的pcor()函数计算偏相关系数。函数调用格式为： 

   pcor(*u*, *S*)  

   其中的*u*是一个数值向量，前两个数值表示要计算相关系数的变量下标，其余的数值为条件变量（即要排除影响的变量）的下标。*S*为变量的协方差阵。

### 7.3.2 相关性的显著性检验

1. 使用cor.test()函数对单个的Pearson、Spearman和Kendall相关系数进行检验。简化后的使用格式为： 

   cor.test(*x*, *y*, alternative = , method = )  

   其中的*x*和*y*为要检验相关性的变量，alternative则用来指定进行双侧检验或单侧检验（取值为"two.side"、"less"或"greater"），而method用以指定要计算的相关类型（"pearson"、"kendall" 或 "spearman" ）。当 研 究 的 假 设 为 总 体 的 相 关 系 数 小 于 0 时，请使用alternative="less" 。在研究的假设为总体的相关系数大于 0 时，应使用alternative="greater"。在默认情况下，假设为alternative="two.side"（总体相关系数不等于0）。cor.test()每次只能检验一种相关关系。

2. psych包中提供的corr.test()函数可以一次做更多事情。corr.test()函数可以为Pearson、Spearman或Kendall相关计算相关矩阵和显著性水平。

   \> library(psych)  

   \> corr.test(states, use="complete") 

   参数use=的取值可为"pairwise"或"complete"（分别表示对缺失值执行成对删除或行删除）。参数method=的取值可为"pearson"（默认值）、"spearman"或"kendall"。

### 7.4 t检验

###　7.4.1独立样本的t检验

t.test(*y* ~ *x*, *data*)  

其中的*y*是一个数值型变量，*x*是一个二分变量。

调用格式或为： t.test(*y1*, *y2*)  

其中的*y1*和*y2*为数值型向量（即各组的结果变量）。可选参数*data*的取值为一个包含了这些变量的矩阵或数据框。

### 7.4.2非独立样本的t检验

非独立样本的t检验假定组间的差异呈正态分布。对于本例，检验的调用格式为： 

t.test(*y1*, *y2*, paired=TRUE)  

其中的*y1*和*y2*为两个非独立组的数值向量。

### 7.4.3 多于两组的情况

使用方差分析（ANOVA）。ANOVA是一套覆盖了许多实验设计和准实验设计的综合方法。

## 7.5 组间差异的非参数检验

### 7.5.1 两组的比较

1. 若两组数据独立，可以使用Wilcoxon秩和检验（更广为人知的名字是Mann-Whitney U检验） 来评估观测是否是从相同的概率分布中抽得的（即，在一个总体中获得更高得分的概率是否比另一个总体要大）。调用格式为： 

   wilcox.test(*y* ~ *x*, *data*)  

   其中的*y*是数值型变量，而*x*是一个二分变量。调用格式或为： 

   wilcox.test(*y1*, *y2*)  

   其中的*y1*和*y2*为各组的结果变量。可选参数data的取值为一个包含了这些变量的矩阵或数据框。默认进行一个双侧检验。你可以添加参数exact来进行精确检验，指定alternative="less" 或alternative="greater"进行有方向的检验。

2. Wilcoxon符号秩检验是非独立样本t检验的一种非参数替代方法。它适用于两组成对数据和无法保证正态性假设的情境。调用格式与Mann-Whitney U检验完全相同，不过还可以添加参数paired=TRUE。

### 7.5.2多于两组的比较

1. 如果各组独立，则Kruskal-Wallis检验将是一种实用的方法。 

   Kruskal-Wallis检验的调用格式为： 

   kruskal.test(*y* ~ *A*, *data*)  

   其中的*y*是一个数值型结果变量，*A*是一个拥有两个或更多水平的分组变量（grouping variable）。（若有两个水平，则它与Mann-Whitney U检验等价。）

2. 如果各组不独立（如重复测量设计或随机区组设计），那么Friedman检验会更合适。Friedman检验的调用格式为： 

   friedman.test(*y* ~ *A* | *B*, *data*)  

   其中的*y*是数值型结果变量，*A*是一个分组变量，而*B*是一个用以认定匹配观测的区组变量 （blocking variable）。在以上两例中，*data*皆为可选参数，它指定了包含这些变量的矩阵或数据框。

