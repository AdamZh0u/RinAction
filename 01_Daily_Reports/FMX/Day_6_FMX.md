# Day 6 R笔记

## Chapter 7 基本统计分析

### 7.1描述性统计分析(连续型变量)

* summary()函数提供了最小值、最大值、四分位数和数值型变量的均值，以及因子向量和逻辑型向量的频数统计。

* apply()函数或sapply()函数乐意计算所选择的任意描述性统计量。对于sapply()函数，其使用格式为： sapply(*x*, *FUN*, *options*)  

  其中的*x*是数据框（或矩阵），*FUN*为一个任意的函数。如果指定了*options*，它们将被传递 给*FUN*。在这里插入的典型函数有mean()、sd()、var()、min()、max()、median()、length()、range()和quantile()。

* 函数fivenum()可返回图基五数总括（Tukey’s five-number  summary，即最小值、下四分位数、中位数、上四分位数和最大值）。

* Hmisc、pastecs和psych等包都提供了计算描述性统计量的函数。  

  * Hmisc包中的describe()函数可返回变量和观测的数量、缺失值和唯一值的数目、平均值、分位数，以及五个最大的值和五个最小的值。

  * pastecs包中有一个名为stat.desc()的函数，它可以计算种类繁多的描述性统计量。使用格式为： stat.desc(*x*, basic=TRUE, desc=TRUE, norm=FALSE, p=0.95)  

    其中的*x*是一个数据框或时间序列。若basic=TRUE（默认值），则计算其中所有值、空值、缺失值的数量，以及最小值、最大值、值域，还有总和。若desc=TRUE（同样也是默认值），则计算中位数、平均数、平均数的标准误、平均数置信度为95%的置信区间、方差、标准差以及变异系数。最后，若norm=TRUE（不是默认的），则返回正态分布统计量，包括偏度和峰度（以及它们的统计显著程度）和Shapiro-Wilk正态检验结果。

  * psych包也拥有一个名为describe()的函数，它可以计算非缺失值的数量、平均数、标准差、中位数、截尾均值、绝对中位差、最小值、最大值、值域、偏度、峰度和平均 值的标准误。

* 可以使用aggregate()函数来分组 获取描述性统计量。

  注：aggregate()函数一次只能返回一个统计量。想要单次返回多个统计量，可以使用by()函数。格式为：by(*data*, *INDICES*, *FUN*)  

  其中*data*是一个数据框或矩阵，*INDICES*是一个因子或因子组成的列表，定义了分组，*FUN*是任意函数。

* doBy包和psych包也提供了分组计算描述性统计量的函数。

  doBy包中summaryBy()函数的使用格式为： summaryBy(*formula*, data=*dataframe*, FUN=*function*) 

  其中的*formula*接受以下的格式： *var1* + *var2* + *var3* + ... + *varN* ~ *groupvar1* + *groupvar2* + ... + *groupvarN* ，在~左侧的变量是需要分析的数值型变量，而右侧的变量是类别型的分组变量。 

### 7.2 频数表和列联表(类别型变量)

#### 7.2.1 频数表

生成和处理频数表的函数见p137-138表7-1

1. 一维列联表

   使用table()函数生成简单的频数统计表。

   可以用prop.table()将这些频数转化为比例值；或使用prop.table()*100转化为百分比： 

2. 二维列联表

   * table()函数的使用格式为： mytable <- table(*A*, *B*)  ，其中的*A*是行变量，*B*是列变量。
   * xtabs()函数还可使用公式风格的输入创建列联表， 格式为： mytable* <- xtabs(~ *A* + *B*, data=*mydata*) ， 其中的*mydata*是一个矩阵或数据框，要进行交叉分类的变量应出现在公式的右侧（即~符号的右方），以+作为分隔符
   * 使用gmodels包中的CrossTable()函数是创建二维列联表的第三种方法。CrossTable() 函数仿照SAS中PROC FREQ或SPSS中CROSSTABS的形式生成二维列联表。

3. 多维列联表

   * table() 和 xtabs() 都可以基于三个或更多的类别型变量生成多维列联表。 
   * margin.table()、prop.table()和addmargins()函数可以推广到高于二维的情况。 
   * ftable()函数可以以紧凑地输出多维列联表。

#### 7.2.2 独立性检验

1. 卡方独立性检验 

   可以使用chisq.test()函数对二维表的行变量和列变量进行卡方独立性检验。

2. Fisher精确检验 

   可以使用fisher.test()函数进行Fisher精确检验。Fisher精确检验的原假设是：边界固定的列联表中行和列是相互独立的。其调用格式为fisher.test(*mytable*)，其中的*mytable*是一个二维列联表。

3. Cochran-Mantel-Haenszel检验 

   mantelhaen.test()函数可用来进行Cochran-Mantel-Haenszel卡方检验，其原假设是，两个 名义变量在第三个变量的每一层中都是条件独立的。

#### 7.2.3 相关性的度量

vcd包中的assocstats()函数可以用来计算二维列联表的phi系数、列联系数和Cramer’s V系数。

### 7.3 相关

* cor()函数可以计算==Pearson、Spearman和Kendall相关系数==，而cov()函数可用来计算==协方差==。两个函数的参数有很多，其中与相关系数的计算有关的参数可以简化为： cor(x, use= , method= ) ，详细参数信息见p146表7-2。

* 可以使用 ggm包中的==pcor()函数==计算==偏相关系数==。函数调用格式为： pcor(*u*, *S*)  

  其中的*u*是一个数值向量，前两个数值表示要计算相关系数的变量下标，其余的数值为条件变量 （即要排除影响的变量）的下标。*S*为变量的协方差阵。

* polycor包中的hetcor()函数可以计算一种混合的相关矩阵，其中包括数值型变量的Pearson积差相关系数、数值型变量和有序变量之间的多系列相关系数、有序变量之间的多分格相 关系数以及二分变量之间的四分相关系数。多系列、多分格和四分相关系数都假设有序变量或二分变量由潜在的正态分布导出。

* 相关性的显著性检验：

  1. 可以使用cor.test()函数对单个的Pearson、Spearman和Kendall相关系数进行检验。简化后的使用格式为： cor.test(*x*, *y*, alternative = , method = )  

     其中的*x*和*y*为要检验相关性的变量，alternative则用来指定进行双侧检验或单侧检验（取值 为"two.side"、"less"或"greater"），而method用以指定要计算的相关类型（"pearson"、 "kendall" 或 "spearman" ）。当 研 究 的 假 设 为 总 体 的 相 关 系 数 小 于 0 时，请使用alternative="less" 。在研究的假设为总体的相关系数大于 0 时，应使用 alternative="greater"。在默认情况下，假设为alternative="two.side"（总体相关系数不等于0）。

     注：cor.test()每次只能检验一种相关关系。psych包中提供的corr.test()函数可以为Pearson、Spearman或Kendall相关计算相关矩阵和显著性水平。

  2. 在$多元正态性$的假设下，psych包中的pcor.test()函数可以用来检验在控制一个或多个额外变量时两个变量之间的条件独立性。使用格式为： pcor.test(*r*, *q*, *n*)  

     其中的*r*是由pcor()函数计算得到的偏相关系数，*q*为要控制的变量数（以数值表示位置），*n*为 样本大小。

* 









### 7.4 t检验

==针对正态分布的连续型变量==

1. 独立样本

检验的调用格式为： t.test(*y* ~ *x*, *data*)  

其中的*y*是一个数值型变量，*x*是一个二分变量。调用格式或为：t.test(*y1*, *y2*)  

其中的*y1*和*y2*为数值型向量（即各组的结果变量）。可选参数*data*的取值为一个包含了这些变量的矩阵或数据框。

注：这里的t检验默认假定方差不相等，并使用Welsh 的修正自由度。可以添加一个参数var.equal=TRUE以假定方差相等，并使用合并方差估计。 

默认的备择假设是双侧的（即均值不相等，但大小的方向不确定）。你可以添加一个参数alternative="less"或alternative="greater"来进行有方向的检验。

2. 非独立样本

非独立样本的t检验假定组间的差异呈正态分布。对于本例，检验的调用格式为： t.test(*y1*, *y2*, paired=TRUE)  ，其中的*y1*和*y2*为两个非独立组的数值向量。

### 7.5 组间差异的非参数检验

如果数据无法满足t检验或ANOVA的参数假设，可以转而使用非参数方法。举例来说，结果变量在本质上就严重偏倚或呈现有序关系。

1. 两组的比较

   若两组数据独立，可以使用Wilcoxon秩和检验（Mann-Whitney U检验）来评估观测是否是从相同的概率分布中抽得的（即，在一个总体中获得更高得分的概率是否比另 

一个总体要大）。调用格式为： wilcox.test(*y* ~ *x*, *data*)  

其中的*y*是数值型变量，而*x*是一个二分变量。调用格式或为： wilcox.test(*y1*, *y2*)  

其中的*y1*和*y2*为各组的结果变量。可选参数data的取值为一个包含了这些变量的矩阵或数据框。默认进行一个双侧检验。可以添加参数exact来进行精确检验，指定alternative="less"或alternative="greater"进行有方向的检验。

Wilcoxon符号秩检验是非独立样本t检验的一种非参数替代方法。它适用于两组成对数据和 无法保证正态性假设的情境。调用格式与Mann-Whitney U检验完全相同，不过还可以添加参数 paired=TRUE。

2. 多于两组的比较

   * 如果各组 独立，则Kruskal-Wallis检验将是一种实用的方法。

   Kruskal-Wallis检验的调用格式为： kruskal.test(*y* ~ *A*, *data*)  

   其中的*y*是一个数值型结果变量，*A*是一个拥有两个或更多水平的分组变量（grouping variable）。 （若有两个水平，则它与Mann-Whitney U检验等价。）

   * 如果各组不独立（如重复测量设计或随机区组 设计），那么Friedman检验会更合适。 

   Friedman检验的调用格式为： friedman.test(*y* ~ *A* | *B*, *data*)  

   其中的*y*是数值型结果变量，*A*是一个分组变量，而*B*是一个用以认定匹配观测的区组变量（blocking variable）。在以上两例中，*data*皆为可选参数，它指定了包含这些变量的矩阵或数据框。