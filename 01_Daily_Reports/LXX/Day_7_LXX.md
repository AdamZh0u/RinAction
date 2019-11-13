# 第八章 回归

## 8.1回归的多面性

![回归的各种变体](D:%5C%E5%AD%A6%E4%B9%A0%5CR%E8%AF%AD%E8%A8%80%E5%AD%A6%E4%B9%A0%5C%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%5C%E5%9B%9E%E5%BD%92%E7%9A%84%E5%90%84%E7%A7%8D%E5%8F%98%E4%BD%93.jpg)

## 8.2 OLS回归

​		OLS（是普通最小二乘）回归是通过预测变量的加权和来预测量化的因变量，其中权重是通过数据估计而得的参数。

### 8.2.1 用 **lm()**拟合回归模型

​		拟合线性模型最基本的函数就是lm()，格式为： 

​		myfit <- lm(*formula*, *data*)  

​		其中，*formula*指要拟合的模型形式，*data*是一个数据框，包含了用于拟合模型的数据。结果对象存储在一个列表中，包含了所拟合模型的大量信息。表达式（formula）形式如下： 

​		Y ~ X1 + X2 + ... + Xk  

​		~左边为响应变量，右边为各个预测变量，预测变量之间用+符号分隔。

![表达式常用符号](D:%5C%E5%AD%A6%E4%B9%A0%5CR%E8%AF%AD%E8%A8%80%E5%AD%A6%E4%B9%A0%5C%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%5C%E8%A1%A8%E8%BE%BE%E5%BC%8F%E5%B8%B8%E7%94%A8%E7%AC%A6%E5%8F%B7.jpg)

![对拟合线性](D:%5C%E5%AD%A6%E4%B9%A0%5CR%E8%AF%AD%E8%A8%80%E5%AD%A6%E4%B9%A0%5C%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%5C%E5%AF%B9%E6%8B%9F%E5%90%88%E7%BA%BF%E6%80%A7.jpg)

​		当回归模型包含一个因变量和一个自变量时，我们称为简单线性回归。当只有一个预测变量，但同时包含变量的幂（比如，X、X^2^，X^3^）时，我们称为多项式回归。当有不止一个预测变量时，则称为多元线性回归。

### 8.2.2 简单线性回归

### 8.2.3 多项式回归

1. 拟合含二次项的等式： 

   fit2 <- lm(weight ~ height + I(height^2), data=women) 

   I(height^2)表示向预测等式添加一个身高的平方项。I函数将括号的内容看作R的一个常规表达式。

2. 拟合三次多项式： 

   fit3 <- lm(weight ~ height + I(height^2) +I(height^3), data=women) 

3. car包中的scatterplot()函数，它可以很容易、方便地绘制二元关系图。以下代码能绘制二元关系图： 

   ~~~
library(car) 
   scatterplot(weight ~ height, data=women, 
    spread=FALSE, smoother.args=list(lty=2), pch=19, 
    main="Women Age 30-39", 
    xlab="Height (inches)", 
    ylab="Weight (lbs.)")
   ~~~
   
   spread=FALSE选项删除了残差正负均方根在平滑曲线上的展开和非对称信息。smoother.args=list(lty=2)选项设置loess拟合曲线为虚线。pch=19选项设置点为实心圆（默认为空心圆）。

### 8.2.4 多元线性回归

1. 多元回归分析中，第一步最好检查一下变量间的相关性。cor()函数提供了二变量之间的相关系数，car包中scatterplotMatrix()函数则会生成散点图矩阵。scatterplotMatrix()函数默认在非对角线区域绘制变量间的散点图，并添加平滑和线性拟合曲线。对角线区域绘制每个变量的密度图和轴须图。

2. 使用lm()函数拟合多元线性回归模型。

   ~~~
   fit <- lm(Murder ~ Population + Illiteracy + Income + Frost, data=states)
   ~~~

3. 当预测变量不止一个时，回归系数的含义为：一个预测变量增加一个单位，其他预测变量保持不变时，因变量将要增加的数量。

### 8.2.5 有交互项的多元线性回归

~~~
 lm(mpg ~ hp + wt + hp:wt, data=mtcars)
~~~

​		通过effects包中的effect()函数，可以用图形展示交互项的结果。格式为： 

~~~
plot(effect(*term*, *mod*,, *xlevels*), multiline=TRUE) 
~~~

​		term*即模型要画的项，*mod*为通过lm()拟合的模型，*xlevels*是一个列表，指定变量要设定的常量值，multiline=TRUE选项表示添加相应直线。

## 8.3 回归诊断

​		使用lm()函数来拟合OLS回归模型，通过summary()函数获取模型参数和相关统计量。但是，没有任何输出告诉你模型是否合适，你对模型参数推断的信心依赖于它在多大程度上满足OLS模型统计假设。虽然summary()函数对模型有了整体的描述，但是它没有提供关于模型在多大程度上满足统计假设的任何信息。 

​		因为数据的无规律性或者错误设定了预测变量与响应变量的关系，都将致使模型产生巨大的偏差。一方面，可能得出某个预测变量与响应变量无关的结论，但事实上它们是相关的；另一方面，情况可能恰好相反。当模型应用到真实世界中时，预测效果可能很差，误差显著。 

### 8.3.1 标准方法

1. 检验回归分析中统计假设的方法。最常见的方法就是对lm()函数返回的对象使用plot()函数，可以生成评价模型拟合情况的四幅图形。

   简单线性回归诊断图： 

   ~~~
fit <- lm(weight ~ height, data=women) 
   par(mfrow=c(2,2)) 
   plot(fit)
   ~~~
   
   二次拟合的诊断图： 

   ~~~
fit2 <- lm(weight ~ height + I(height^2),data=women) 
   par(mfrow=c(2,2))  
   plot(fit2) 
   ~~~
   
2. 拟合剔除观测点13和15后的模型：

   ~~~
   newfit <- lm(weight~ height + I(height^2), data=women[-c(13,15),])
   ~~~

### 8.3.2 改进的方法

![回归诊断实用函数](D:%5C%E5%AD%A6%E4%B9%A0%5CR%E8%AF%AD%E8%A8%80%E5%AD%A6%E4%B9%A0%5C%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%5C%E5%9B%9E%E5%BD%92%E8%AF%8A%E6%96%AD%E5%AE%9E%E7%94%A8%E5%87%BD%E6%95%B0.jpg)

![回归诊断实用函数2](D:%5C%E5%AD%A6%E4%B9%A0%5CR%E8%AF%AD%E8%A8%80%E5%AD%A6%E4%B9%A0%5C%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%5C%E5%9B%9E%E5%BD%92%E8%AF%8A%E6%96%AD%E5%AE%9E%E7%94%A8%E5%87%BD%E6%95%B02.jpg)

1. 正态性 

   ①与基础包中的plot()函数相比，qqPlot()函数提供了更为精确的正态假设检验方法，它画出了在*n*–*p*–1个自由度的t分布下的学生化残差（studentized residual，也称学生化删除残差或折叠化残差）图形，其中*n*是样本大小，*p*是回归参数的数目（包括截距项）。代码如下： 

   ~~~
   qqPlot(fit, labels=row.names(states), id.method="identify", 
    simulate=TRUE, main="Q-Q Plot")
   ~~~

   id.method = "identify"选项能够交互式绘图——待图形绘制后，用鼠标单击图形内的点，将会标注函数中labels选项的设定值。敲击Esc键，从图形下拉菜单中选择Stop，或者在图形上右击，都将关闭这种交互模式。

   ②可视化误差还有其他方法，residplot()函数生成学生化残差柱状图（即直方图），并添加正态曲线、核密度曲线和轴须图。

   ~~~
   residplot <- function(fit, nbreaks=10) { 
    z <- rstudent(fit) 
    hist(z, breaks=nbreaks, freq=FALSE, 
    xlab="Studentized Residual", 
    main="Distribution of Errors") 
    rug(jitter(z), col="brown") 
    curve(dnorm(x, mean=mean(z), sd=sd(z)), 
    add=TRUE, col="blue", lwd=2) 
    lines(density(z)$x, density(z)$y, 
    col="red", lwd=2, lty=2) 
    legend("topright", 
    legend = c( "Normal Curve", "Kernel Density Curve"), 
    lty=1:2, col=c("blue","red"), cex=.7) 
    } 
   residplot(fit)
   ~~~

2. 误差的独立性

   car包提供了一个可做Durbin-Watson检验的函数，能够检测误差的序列相关性。在多元回归中，使用下面的代码可以做Durbin-Watson检验： 

   ~~~
    durbinWatsonTest(fit) 
   ~~~

3. 线性

   通过成分残差图（component plus residual plot）也称偏残差图（partial residual plot），你可以看看因变量与自变量之间是否呈非线性关系，也可以看看是否有不同于已设定线性模型的系统偏差，图形可用car包中的crPlots()函数绘制。

   ~~~
   library(car) 
   crPlots(fit)
   ~~~

4. 同方差性

   ncvTest()函数生成一个计分检验，零假设为误差方差不变，备择假设为误差方差随着拟合值水平的变化而变化。若检验显著，则说明存在异方差性（误差方差不恒定）。 

   spreadLevelPlot()函数创建一个添加了最佳拟合曲线的散点图，展示标准化残差绝对值与拟合值的关系。

   ~~~
   library(car) 
   ncvTest(fit)
   spreadLevelPlot(fit)
   ~~~

### 8.3.3 线性模型假设的综合验证

​		gvlma()函数能对线性模型假设进行综合验证，同时还能做偏斜度、峰度和异方差性的评价，它给模型假设提供了一个单独的综合检验（通过/不通过）。

### 8.3.4 多重共线性

​		多重共线性可用统计量VIF（Variance Inflation Factor，方差膨胀因子）进行检测。VIF的平方根表示变量回归参数的置信区间能膨胀为与模型无关的预测变量的程度（因此而得名）。car包中的vif()函数提供VIF值。一般原则下， *vif* >2就表明存在多重共线性问题。

## 8.4 异常观测值

### 8.4.1 离群点

​		离群点是指那些模型预测效果不佳的观测点。它们通常有很大的、或正或负的残差（*Y*~i~–*Ŷ*~i~）。正的残差说明模型低估了响应值，负的残差则说明高估了响应值。

​		outlierTest()函数可以求得最大标准化残差绝对值Bonferroni调整后的*p*值：

~~~
library(car)  
outlierTest(fit) 
~~~

​		该函数只是根据单个最大（或正或负）残差值的显著性来判断是否有离群点。若不显著，则说明数据集中没有离群点；若显著，则你必须删除该离群点，然后再检验是否还有其他离群点存在。

### 8.4.2 高杠杆值点

​		高杠杆值观测点，即与其他预测变量有关的离群点。换句话说，它们是由许多异常的预测变量值组合起来的，与响应变量值没有关系。

​		高杠杆值的观测点可通过帽子统计量（hat statistic）判断。对于一个给定的数据集，帽子均值为*p*/*n*，其中*p*是模型估计的参数数目（包含截距项），*n*是样本量。一般来说，若观测点的帽子值大于帽子均值的2或3倍，就可以认定为高杠杆值点。

~~~
hat.plot <- function(fit) { 
 p <- length(coefficients(fit)) 
 n <- length(fitted(fit)) 
 plot(hatvalues(fit), main="Index Plot of Hat Values") 
 abline(h=c(2,3)*p/n, col="red", lty=2) 
 identify(1:n, hatvalues(fit), names(hatvalues(fit))) 
 } 
hat.plot(fit)
~~~

​		高杠杆值点可能是强影响点，也可能不是，这要看它们是否是离群点。

### 8.4.3 强影响点

1. 强影响点，即对模型参数估计值影响有些比例失衡的点。

2. 有两种方法可以检测强影响点：Cook距离，或称D统计量，以及变量添加图（added variable plot）。

   ①一般来说，Cook’s D值大于4/(*n*–*k*–1)，则表明它是强影响点，其中*n*为样本量大小，*k*是预测变量数目。

~~~
cutoff <- 4/(nrow(states)-length(fit$coefficients)-2) 
plot(fit, which=4, cook.levels=cutoff) 
abline(h=cutoff, lty=2, col="red")
~~~

​		Cook’s D图有助于鉴别强影响点，但是并不提供关于这些点如何影响模型的信息。变量添加图弥补了这个缺陷。对于一个响应变量和*k*个预测变量，你可以如下图创建*k*个变量添加图。

​		②所谓变量添加图，即对于每个预测变量*X~k~*，绘制*X~k~*在其他*k*–1个预测变量上回归的残差值相对于响应变量在其他*k*–1个预测变量上回归的残差值的关系图。car包中的avPlots()函数可提供变量添加图： 

~~~
library(car) 
avPlots(fit, ask=FALSE, id.method="identify")
~~~

3. influencePlot()函数，你还可以将离群点、杠杆值和强影响点的信息整合到一幅图形中： 

   ~~~ 
library(car)  
   influencePlot(fit, id.method="identify", main="Influence Plot",  
    sub="Circle size is proportional to Cook's distance") 
   ~~~

## 8.5 改进措施

1. 删除观测点

2. 变量变换

   ①当模型不符合正态性、线性或者同方差性假设时，一个或多个变量的变换通常可以改善或调整模型效果。

   ②当模型违反正态假设时，通常可以对响应变量尝试某种变换。car包中的powerTransform()函数通过*λ*的最大似然估计来正态化变量*X*^*λ*^。

   ③当违反了线性假设时，对预测变量进行变换常常会比较有用。car包中的boxTidwell()函数通过获得预测变量幂数的最大似然估计来改善线性关系。

   ④响应变量变换还能改善异方差性（误差方差非恒定）。car包中spreadLevelPlot()函数提供幂次变换。

3. 增删变量

4. 尝试其他方法

## 8.6 选择“最佳”的回归模型

### 8.6.1 模型比较

1. 用基础安装中的anova()函数可以比较两个嵌套模型的拟合优度。所谓嵌套模型，即它的一些项完全包含在另一个模型中。

2. AIC（Akaike Information Criterion，赤池信息准则）也可以用来比较模型，它考虑了模型的统计拟合度以及用来拟合的参数数目。AIC值较小的模型要优先选择，它说明模型用较少的参数获得了足够的拟合度。该准则可用AIC()函数实现

   ~~~
    fit1 <- lm() 
   > fit2 <- lm() 
   > AIC(fit1,fit2)
   ~~~

### 8.6.2 变量选择

​		从大量候选变量中选择最终的预测变量有以下两种流行的方法：逐步回归法（stepwise method）和全子集回归。

1. 逐步回归

   逐步回归中，模型会一次添加或者删除一个变量，直到达到某个判停准则为止。例如，向前逐步回归（forward stepwise regression）每次添加一个预测变量到模型中，直到添加变量不会使模型有所改进为止。向后逐步回归（backward stepwise regression）从模型包含所有预测变量开始，一次删除一个变量直到会降低模型质量为止。而向前向后逐步回归（stepwise stepwise regression，通常称作逐步回归，以避免听起来太冗长），结合了向前逐步回归和向后逐步回归的方法，变量每次进入一个，但是每一步中，变量都会被重新评价，对模型没有贡献的变量将会被删除，预测变量可能会被添加、删除好几次，直到获得最优模型为止。

2. MASS包中的stepAIC()函数可以实现逐步回归模型（向前、向后和向前向后），依据的是精确AIC准则。

   ~~~
   stepAIC(fit, direction="backward")
   ~~~

   逐步回归法其实存在争议，虽然它可能会找到一个好的模型，但是不能保证模型就是最佳模型，因为不是每一个可能的模型都被评价了。

3. 全子集回归

   顾名思义，全子集回归是指所有可能的模型都会被检验。分析员可以选择展示所有可能的结果，也可以展示*n*个不同子集大小（一个、两个或多个预测变量）的最佳模型。例如，若nbest=2，先展示两个最佳的单预测变量模型，然后展示两个最佳的双预测变量模型，以此类推，直到包含所有的预测变量。 

   全子集回归可用leaps包中的regsubsets()函数实现。

## 8.7 深层次分析

### 8.7.1 交叉验证

​		交叉验证，即将一定比例的数据挑选出来作为训练样本，另外的样本作保留样本，先在训练样本上获取回归方程，然后在保留样本上做预测。由于保留样本不涉及模型参数的选择，该样本可获得比新数据更为精确的估计。		bootstrap 包中的 crossval() 函数可以实现 *k* 重交叉验证。

### 8.7.2 相对重要性

​		若预测变量不相关，过程就相对简单得多，你可以根据预测变量与响应变量的相关系数来进行排序。但大部分情况中，预测变量之间有一定相关性，这就使得评价变得复杂很多。 

​		评价预测变量相对重要性的方法一直在涌现。最简单的莫过于比较标准化的回归系数，它表示当其他预测变量不变时，该预测变量一个标准差的变化可引起的响应变量的预期变化（以标准差单位度量）。在进行回归分析前，可用scale()函数将数据标准化为均值为0、标准差为1的数据集，这样用R回归即可获得标准化的回归系数。（注意，scale()函数返回的是一个矩阵，而lm()函数要求一个数据框，你需要用一个中间步骤来转换一下。）代码和多元回归的结果如下： 

~~~
states <- as.data.frame(state.x77[,c("Murder","Population",  
 "Illiteracy", "Income", "Frost")])  
zstates <- as.data.frame(scale(states))  
zfit <- lm(Murder~Population + Income + Illiteracy + Frost, data=zstates)  
coef(zfit) 
~~~

​		相对权重（relative weight）是一种比较有前景的新方法，它是对所有可能子模型添加一个预测变量引起的R平方平均增加量的一个近似值。

~~~
relweights()
~~~

