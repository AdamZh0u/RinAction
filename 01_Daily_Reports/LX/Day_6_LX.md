### Day 6

#### 7 基本统计分析

##### 7.1描述性统计分析

1. ``` R
   summary()#提供了最小值、最大值、四分位数和数值型变量的均值，以及因子向量和逻辑型向量的频数统计
   sapply(x, FUN, options)#X是数据框，FUN为一个任意的函数；计算描述统计量
   stat.desc(x, basic=TRUE, desc=TRUE, norm=FALSE, p=0.95#x是一个数据框或时间序列,basic=TRUE计算其中所有值、空值、缺失值的数量，以及最小值、最大值、值域，还有总和。desc=TRUE计算中位数、平均数、平均数的标准误、平均数置信度为95%的置信区间、方差、标准差以及变异系数。norm=TRUE返回正态分布统计量，包括偏度和峰度。
   aggregate()#分组获取描述性统计量,仅允许在每次调用中使用平均数、标准差这样的单返回值函数。
   by(data, INDICES, FUN)#data是一个数据框或矩阵，INDICES是一个因子或因子组成的列表，定义了分组，FUN是任意函数
   summaryBy(formula, data=dataframe, FUN=function)
   ```

##### 7.2 频数表和列联表

1. ``` R
   一维列联变量
   table(var1, var2, ..., varN)#使用N个类别型变量（因子）创建一个N维列联表
   prop.table()#将频数转化为比例值
   prop.table()*100#转换为百分比
   ```

2. ``` R
   二维列联变量
   mytable <- table(A, B)#A是行变量，B是列变量
   mytable <- xtabs(~ A + B, data=mydata)#，要进行交叉分类的变量应出现在公式的右侧（即~符号的右方），以+作为分隔符
   margin.table()/prop.table()#生成边际频数和比例
   addmargins()#给表格添加边际和
   CrossTable()#创建二维列联表
   ```

3. ``` R
   三维列联表
   mytable <- xtabs(~ Treatment+Sex+Improved, data=Arthritis)
   ftable(mytable)
   ```

4. ==独立性检验==

``` R
卡方独立性检验
chisq.test()#对二维表的行变量和列变量进行卡方独立性检验
fisher.test()#Fisher精确检验
mantelhaen.test()
```

##### 7.3 相关的类型

1. ``` R
   Pearson、Spearman和Kendall相关
   cor()#可计算着三种相关系数
   cov()#可用来计算协方差
   cor(x, use= , method= )
   ```

2. ``` R
   偏相关
   pcor(u, S)#u是一个数值型向量，S为变量的协方差阵
   ```

3. ``` R
   相关性的显著性检验
   cor.test(x, y, alternative = , method = )#x和y为要检验相关性的变量,alternative则用来指定进行双侧检验或单侧检验,method用以指定要计算的相关类型
   ```

##### 7.4 t检验

1. ``` R
   独立样本的t检验
   t.test(y ~ x, data)#y是数值型变量，x是一个二分变量
   t.test(y1, y2)#y1和y2是数值型变量
   非独立样本的t检验
   t.test(y1, y2, paired=TRUE)
   ```

##### 7.5 组间差异的非参数检验

``` R
两组的比较
wilcox.test(y ~ x, data)#y是数值型变量，x是一个二分变量
多组比较
kruskal.test(y ~ A, data)#y是一个数值型结果变量,A是一个拥有两个或更多水平的分组变量
friedman.test(y ~ A | B, data)#y是数值型结果变量，A是一个分组变量，而B是一个用以认定匹配观测的区组变量
```

