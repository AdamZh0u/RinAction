# 基本统计分析

## 描述性统计分析

- summary()函数来获取描述性统计，包括==最小值、最大值、四分位数和数值型变量的均值，以及因子向量和逻辑型向量的频数==统计，fivenum( )直接返回最小值、下四分位数、中位数、上四分位数和最大值。

也可用apply( ),sapply(x, FUN, options)函数，x为数据框（或矩阵）

可自己进行function( )命令自定义函数：

i.e.

偏度 `skew <- sum((x-m)^3/ s^3)/n`
峰度 `kurt <- sum((x-m)^4/ s^4) /n - 3`

- 其他方法

  - Hmisc包中的describe()函数，返回变量和观测的数量、缺失值和唯一值的数目、平均值、
    分位数，以及五个最大的值和五个最小的值

  - pastecs包中的stat.desc(x, basic=TRUE, desc=TRUE, norm=FALSE, p=0.95)的函数

    1、若basic=TRUE（默认值），则计算其中所有值nbr.val、空值nbr.null、缺失值的数量nbr.na，以及最小值min、最大值max、值域range，还有总和sum。

    2、若desc=TRUE（同样也是默认值），则计算中位数median、平均数mean、平均数的标准误SE.mean、平均数置信度为95%的置信区间CI.mean.0.95、方差var、标准差std.dev以及变异系数coef.var。

    3、若norm=TRUE（不是默认的），则返回正态分布统计量，包括偏度和峰度（以及它们
    的统计显著程度）和Shapiro-Wilk正态检验结果。

  - psych包的describe()的函数，计算非NA的数值n、平均数mean、标准差sd、中位数median、截尾均值trimmed、绝对中位差mad、最小值min、最大值max、值域range、偏度skew、峰度kurtosis和平均值的标准误se。

:thinking:若不同的包均提供了相同的函数，以最后载入的程序包优先。但可运用`Hmisc::describe(mt)`调用先载入的程序包

----

- 分组计算描述性统计量

  - aggregate()函数分组获取描述性统计量

    i.e. `aggregate(mtcars[myvars], by=list(am=mtcars$am), mean)`

  - 多个分组变量则使用 `by=list(name1=groupvar1, name2=groupvar2, ... , nameN=groupvarN)`

  - by(data, INDICES, FUN)。data是一个数据框或矩阵，INDICES是一个因子或因子组成的列表，定义了分组，FUN是任意函数。

    i.e. `dstats <- function(x)sapply(x, mystats)`

    ​       `myvars <- c("mpg", "hp", "wt")`
    ​       `by(mtcars[myvars], mtcars$am, dstats)` 

  - library(doBy) 中的summaryBy(formula, data=dataframe, FUN=function)

    formula接受以下格式：var1 + var2 + var3 + ... + varN (数值型变量）~ groupvar1 + groupvar2 + ... + groupvarN（类别型）

    可视化：直方、密度、箱线、点图

----

- 频数表和列联表

  - 生成频数表

    1. table(var1, var2, ..., varN) 使用N 个类别型变量（因子）创建一个N 维列联表

    2. xtabs(formula, data) 根据一个公式和一个矩阵或数据框创建一个N 维列联表
    3. prop.table(table, margins) 依margins 定义的边际列表将表中条目表示为分数形式（==比例值==），或用prop.table()*100转化为百分比
    4. margin.table(table, margins) 依margins 定义的边际列表计算表中条目的和
    5. addmargins(table, margins) 将概述边margins（默认是求和结果）放入表中
    6. ftable(table) 创建一个紧凑的“平铺”式列联表

  - 一维列联表

  - 二维列联表：mytable <- xtabs(~ A + B, data=mydata)   A为行变量，B为列变量

    1. 可使用margin.table()和prop.table()函数分别生成边际频数和比例；addmargins()函数为表格添加边际和

    2. gmodels包中的CrossTable()函数是创建二维列联表的第三种方法

  - 多维列联表：table( ) 和xtabs( )；margin.table( )、prop.table( )和addmargins( )；ftable( ）

    

- 独立性检验
  - 卡方独立性检验：`chisq.test()`函数对二维表的行变量和列变量进行检验
  - Fisher精确检验：fisher.test(mytable)，mytable是一个二维列联表
  - Cochran-Mantel-Haenszel检验：mantelhaen.test( )

- 相关性度量

library(vcd)中的assocstats()函数可以用来计算二维列联表的phi系数、列联系数和Cramer’s V系数

可视化：马赛克图和关联图

----

- 相关

  - Pearson（线性相关）、Spearman（分级定序变量）和Kendall（非参数的等级相关）相关

    cor(x, use= , method=)

    cov( )协方差

  - 偏相关：library(ggm)中的pcor( u，S)。u是一个数值向量，前两个数值表示要计算相关系数的变量下标，其余的数值为条件变量（即要排除影响的变量）的下标。S为变量的协方差阵

  - polycor包中的hetcor()函数可以计算一种混合的相关矩阵

  - 相关性的显著性检验：

    `cor.test(x, y, alternative = , method = )`

    library(psych)中的corr.test( )可以为Pearson、Spearman或Kendall相关计算相关矩阵和显著性水平

  - library(ggm)中的pcor.test(r,q,n)可以用来检验在控制一个或多个额外变量时两个变量之间的条件独立性

    可视化：散点图，散点图矩阵，相关图（correlogram)

----

- t检验

  - 独立样本t检验：`t.test(y ~ x, data)`

  - 非独立样本的t检验：`t.test(y1, y2, paired=TRUE)`

    i.e. `with(UScrime, t.test(U1, U2, paired=TRUE))`

  - 多于两组的情况：方差分析（ANOVA）

- 组间差异的非参数检验：非参数方法
  - 两组的比较：两组数据独立，Mann-Whitney U检验

    `wilcox.test(y ~ x, data)`或`wilcox.test(y1, y2)`

  - 多于两组的比较

    - 各组独立，kruskal.test(y ~ A, data）

      i.e. `kruskal.test(Illiteracy ~ state.region, data=states)`

    - 各组不独立，friedman.test(y ~ A | B, data)

`source("http://www.statmethods.net/RiA/wmc.txt")`

`states <- data.frame(state.region, state.x77)`
`wmc(Illiteracy ~ state.region, data=states, method="holm")`

得到的结果：基本统计量Descriptive Statistics（样本量，样本中位数，每组的绝对中位差）；成组比较Multiple Comparisons (Wilcoxon Rank Sum Tests) Probability Adjustment = holm

组间差异的可视化：箱线图，核密度图

:thinking:统计学基础不扎实的我，学这一节如履薄冰:pensive:

----

# Regression
- 回归的多面性：回归类型：简单线性，多项式，多层，多元线性，多变量，Logestic，泊松，Cox比例风险，时间序列，非线性，非参数，稳健。

- OLS回归  lm( )   

  `myfit <- lm(formula, data)`

  formula形式，Y ~ X1 + X2 + ... + Xk

  ~分隔符号   +分隔预测变量    ：预测变量的交互项 y ~ x + z + x:z   

  *所有可能交互项的间接方式y~ x * z * w 可展开为y ~ x + z + w + x:z + x:w + z:w +
  x:z:w    

  ^交互项达到某个次数y ~ (x + z + w)^2 可展开为y ~ x + z + w + x:z + x:w + z:w

  · 包含除因变量外的所有变量,若一个数据框包含变量x、y、z 和w，代码y ~ .可展开为y ~x + z + w

  -从等式中移除某个变量   y ~ (x + z + w)^2 – x:w 可展开为y ~ x + z + w +x:z + z:w

  -1删除截距项，y ~ (x + z + w)^2 – x:w 可展开为y ~ x + z + w +x:z + z:w

  I(x)从算术的角度来解释括号中的元素    

  function 可以在表达式中用的数学函数  log(y) ~ x + z + w 表示通过x、z 和w 来预测log(y)

| 函数           | 用途                                                         |
| -------------- | ------------------------------------------------------------ |
| summary（）    | 展示拟合模型的详细结果                                       |
| coefficients() | 列出拟合模型的模型参数（截距项和斜率）                       |
| confint()      | 提供模型参数的置信区间（默认95%）                            |
| fitted()       | 列出拟合模型的预测值                                         |
| residuals()    | 列出拟合模型的残差值                                         |
| anova()        | 生成一个拟合模型的方差分析表，或者比较两个或更多拟合模型的方差分析表 |
| vcov()         | 列出模型参数的协方差矩阵                                     |
| AIC()          | 输出赤池信息统计量                                           |
| plot()         | 生成评价拟合模型的诊断图                                     |
| predict()      | 用拟合模型对新的数据集预测响应变量值                         |

- 

  - 简单线性回归
  - 多项式回归

  i.e. `lm(weight ~ height + I(height^2), data=women)`

  - ==非线性模型==nls( )
  - library(car)中的==scatterplot( )==绘制二元关系图

  `library(car)`
  `scatterplot(weight ~ height, data=women,`
  `spread=FALSE, smoother.args=list(lty=2), pch=19,`
  `main="Women Age 30-39",`
  `xlab="Height (inches)",`
  `ylab="Weight (lbs.)")`

  :thinking:这个函数很强大啊，自带箱线图和拟合曲线！

  - 多元线性回归

    i.e. 先把矩阵变换为数据框

    `states <- as.data.frame(state.x77[,c("Murder", "Population","Illiteracy", "Income", "Frost")])`

    `cor(states)` 检验二变量之间的相关系数

    `scatterplotMatrix(states, spread=FALSE, smoother.args=list(lty=2),`
    `main="Scatter Plot Matrix")` 生成散点图矩阵

    `fit <- lm(Murder ~ Population + Illiteracy + Income + Frost,data=states)`多元线性回归

  - 有交互项的多元线性回归

    library(effects)effect()函数，用图形展示交互项的结果

    plot(effect(term, mod,, xlevels), multiline=TRUE)

    i.e. `plot(effect("hp:wt", fit,, list(wt=c(2.2,3.2,4.2))), multiline=TRUE)`

    

- 回归诊断
  - 对lm()返回结果使用plot()函数生成评价模型拟合情况四幅图

    正态性，独立性，线性，同方差性

    残差与杠杆图：离群点；很高的杠杆值，异常的预测变量值的组合；强影响点：它对模型参数的估计产生的影响过
    大，非常不成比例（通过Cook’s D鉴别）

  - plot(fit)

  - library(car)回归诊断实用函数

    | 函数                | 目的                               |
    | ------------------- | ---------------------------------- |
    | qqPlot()            | 分位数比较图                       |
    | durbinWatsonTest()  | 对误差自相关性做Durbin-Watson 检验 |
    | crPlots()           | 成分与残差图                       |
    | ncvTest()           | 对非恒定的误差方差做得分检验       |
    | spreadLevelPlot()   | 分散水平检验                       |
    | outlierTest()       | Bonferroni 离群点检验              |
    | avPlots()           | 添加的变量图形                     |
    | inluencePlot()      | 回归影响图                         |
    | scatterplot()       | 增强的散点图                       |
    | scatterplotMatrix() | 增强的散点图矩阵                   |
    | vif()               | 方差膨胀因子                       |

    library(gvlma)提供了对所有线性模型假设进行检验的方法

    residplot()函数生成残差柱状图（即直方图），并添加正态曲线、核密度曲线和轴须图

    library(car)中的crPlots()绘制偏残差图，判断因变量与自变量之间是否呈非线性关系

- 异常值观测
  - 离群点，library(car)中的outlierTest( )：根据单个最大(或正或负）残差值的显著性来判断是否有离群点
  - 高杠杆值点：帽子统计量（hat statistic）
  - 强影响点：Cook距离，Cook’s D值大于4/(n–k–1)，则表明它是强影响点，其中n为样本量大小，k是预测变量数目；library(car)中的avPlots()函数

----

- 深层次分析

  - 交叉验证：将一定比例的数据挑选出来作为训练样本，另外的样本作保留样本，先在
    训练样本上获取回归方程，然后在保留样本上做预测。

  - k重交叉验证，样本被分为k个子样本，轮流将k–1个子样本组合作为训练集，另外1个子
    样本作为保留集。library(bootstrap)的crossval( )函数

  - shrinkage()函数，创建了一个包含预测变量和预测值的矩阵，可获得初始R平方以及交叉验证的R平方

    ----

    :thinking:太难了==我要回炉重造温习统计学知识了TAT

