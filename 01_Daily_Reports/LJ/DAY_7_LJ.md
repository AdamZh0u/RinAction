# DAY_7

## 第八章 回归

### 任务

 学习第八章回归，掌握OLS的适用条件，回归诊断与异常值处理
 针对数据使用多种回归方法模型进行比较

### 重要的部分

8.1 回归的适用
8.2 OLS 重要
8.3 回归诊断
      8.3.1 标准方法
8.4 异常观测值
     8.4.1 离群点
8.7 交叉验证

### 8.2  OLS回归

##### 8.2.1 用lm()拟合回归模型

在R中，拟合线性模型最基本的函数就是lm()，格式为：myfit <- lm(formula, data) 
其中，formula指要拟合的模型形式，data是一个数据框，包含了用于拟合模型的数据。
结果对象（本例中是myfit）存储在一个列表中，包含了所拟合模型的大量信息。
表达式（formula）形式如下：Y ~ X1 + X2 + ... + Xk 
~左边为响应变量，右边为各个预测变量，预测变量之间用+符号分隔。

##### 8.2.2 简单线性回归

#### 例 简单线性回归

fit <- lm(weight ~ height, data=women) 
summary(fit) 
women\$weight
fitted(fit)
residuals(fit)
plot(women\$height,women\$weight, 
     xlab="Height (in inches)", 
     ylab="Weight (in pounds)") 
abline(fit)

##### 8.2.3 多项式回归

如下代码可以拟合含二次项的等式：
fit2 <- lm(weight ~ height + I(height^2), data=women) 

#### 例 多项式回归

fit2 <- lm(weight ~ height + I(height^2), data=women) 
summary(fit2) 
plot(women\$height,women\$weight, 
     xlab="Height (in inches)", 
     ylab="Weight (in lbs)") 
lines(women\$height,fitted(fit2))

一般来说，n次多项式生成一个n–1个弯曲的曲线。拟合三次多项式，可用：
fit3 <- lm(weight ~ height + I(height^2) +I(height^3), data=women) 

#### 例 多项式回归

library(car) 
scatterplot(weight ~ height, data=women, 
spread=FALSE, smoother.args=list(lty=2), pch=19, 
main="Women Age 30-39", 
xlab="Height (inches)", 
ylab="Weight (lbs.)")
既提供了身高与体重的散点图、线性拟合曲线和平滑拟合（loess）曲线，还在相应边界展示了每个变量的箱线图。spread=FALSE选项删除了残差正负均方根在平滑曲线上的展开和非对称信息。
smoother.args=list(lty=2)选项设置loess拟合曲线为虚线。pch=19选项设置点为实心圆（默认为空心圆）。

##### 8.2.4 多元线性回归

### 例 检测二变量关系

states <- as.data.frame(state.x77[,c("Murder", "Population", 
                                     "Illiteracy", "Income", "Frost")]) 
cor(states)
library(car) 
scatterplotMatrix(states, spread=FALSE, smoother.args=list(lty=2), 
                    main="Scatter Plot Matrix") 
scatterplotMatrix()函数默认在非对角线区域绘制变量间的散点图，并添加平滑和线性拟合曲线。
对角线区域绘制每个变量的密度图和轴须图。

### 例 多元线性回归

states <- as.data.frame(state.x77[,c("Murder", "Population", 
                                     "Illiteracy", "Income", "Frost")]) 
fit <- lm(Murder ~ Population + Illiteracy + Income + Frost, 
            data=states) 
summary(fit)

##### 8.2.5 有交互项的多元线性回归

#### 例 有显著交互项的多元线性回归

fit <- lm(mpg ~ hp + wt + hp:wt, data=mtcars) 
summary(fit)

通过effects包中的effect()函数，可以用图形展示交互项的结果。格式为：
plot(effect(term, mod,, xlevels), multiline=TRUE) 
term即模型要画的项，mod为通过lm()拟合的模型，xlevels是一个列表，指定变量要设定
的常量值，multiline=TRUE选项表示添加相应直线。
plot(effect("hp:wt", fit,, list(wt=c(2.2,3.2,4.2))), multiline=TRUE)

### 8.3 回归诊断

##### 8.3.1 标准方法

R基础安装中提供了大量检验回归分析中统计假设的方法。最常见的方法就是对lm()函数
返回的对象使用plot()函数，可以生成评价模型拟合情况的四幅图形。
下面是简单线性回归的例子：
fit <- lm(weight ~ height, data=women) 
par(mfrow=c(2,2)) 
plot(fit) 

fit2 <- lm(weight ~ height + I(height^2), data=women) 
par(mfrow=c(2,2)) 
plot(fit2)

使用：newfit <- lm(weight~ height + I(height^2), data=women[-c(13,15),]) 
即可拟合剔除点后的模型。

再应用这个基本的方法，看看states的多元回归问题。
states <- as.data.frame(state.x77[,c("Murder", "Population", 
"Illiteracy", "Income", "Frost")]) 
fit <- lm(Murder ~ Population + Illiteracy + Income + Frost, data=states) 
par(mfrow=c(2,2)) 
plot(fit) 

##### 8.3.2 改进的方法

car包提供了大量函数，大大增强了拟合和评价回归模型的能力

1. 正态性
   与基础包中的plot()函数相比，qqPlot()函数提供了更为精确的正态假设检验方法，
   它画出了在n–p–1个自由度的t分布下的学生化残差，也称学生化删除残差或折叠化残差）图形
   其中n是样本大小，p是回归参数的数目（包括截距项）。代码如下：
   library(car) 
   states <- as.data.frame(state.x77[,c("Murder", "Population", 
                                     "Illiteracy", "Income", "Frost")]) 
   fit <- lm(Murder ~ Population + Illiteracy + Income + Frost, data=states) 
   qqPlot(fit, labels=row.names(states), id.method="identify", 
       simulate=TRUE, main="Q-Q Plot") 
       

residplot()函数生成学生化残差柱状图（即直方图），并添加正态曲线、核密度曲线和轴须图。

#### 例 绘制学生化残差图的函数

residplot <- function(fit, nbreaks=10) { 
z <- rstudent(fit) 
hist(z, breaks=nbreaks, freq=FALSE, 
xlab="Studentized Residual", 
main="Distribution of Errors") 
rug(jitter(z), col="brown") 
curve(dnorm(x, mean=mean(z), sd=sd(z)), 
add=TRUE, col="blue", lwd=2) 
lines(density(z)\$x, density(z)\$y, 
col="red", lwd=2, lty=2) 
legend("topright", 
legend = c( "Normal Curve", "Kernel Density Curve"), 
lty=1:2, col=c("blue","red"), cex=.7) } 
residplot(fit) 

2. 误差的独立性
   时间序列数据通常呈现自相关性——相隔时间越近的观测相关性大于相隔越远的观测
   car包提供了一个可做Durbin-Watson检验的函数，能够检测误差的序列相关性。
   在多元回归中，使用下面的代码可以做Durbin-Watson检验
    durbinWatsonTest(fit) 
3. 线性
   通过成分残差图（component plus residual plot）也称偏残差图（partial residual plot），
   可以看因变量与自变量之间是否呈非线性关系，也可以看是否有不同于已设定线性模型的系统偏差
   图形可用car包中的crPlots()函数绘制。
   平滑拟合曲线（loess）将在第11章介绍。代码如下：
   library(car) 
   crPlots(fit) 
4. 同方差性
   ncvTest()函数生成一个计分检验，零假设为误差方差不变，备择假设为误差方差随着拟合值水平的变化而变化。若检验显著，则说明存在异方差性（误差方差不恒定）。
    spreadLevelPlot()函数创建一个添加了最佳拟合曲线的散点图，展示标准化残差绝对值与拟合值的关系。

#### 例 检验同方差性

library(car) 
ncvTest(fit)
spreadLevelPlot(fit) 

##### 8.3.3  线性模型假设的综合验证

gvlma()函数能对线性模型假设进行综合验证，同时还能做偏斜度、峰度和异方差性的评价。
它给模型假设提供了一个单独的综合检验（通过/不通过）。

#### 例 线性模型假设的综合检验

library(gvlma) 
gvmodel <- gvlma(fit) 
summary(gvmodel) 

##### 8.3.4 多重共线性

多重共线性可用统计量VIF进行检测。VIF的平方根表示变量回归参数的置信区间能膨胀为与模型无关的预测变量的程度（因此而得名）。car包中的vif()函数提供VIF值。一般原则下，vif >2就表明存在多重共线性问题。

#### 例 检测多重共线性

library(car) 
vif(fit)
sqrt(vif(fit)) > 2 # problem?

### 8.4 异常观测值

##### 8.4.1 离群点

离群点是指那些模型预测效果不佳的观测点。它们通常有很大的、或正或负的残差（Yi–Ŷi）。
正的残差说明模型低估了响应值，负的残差则说明高估了响应值。
car包也提供了一种离群点的统计检验方法。outlierTest()函数可以求得最大标准化残差
绝对值Bonferroni调整后的p值：
library(car) 
outlierTest(fit) 

##### 8.4.2 高杠杆值点

高杠杆值观测点，即与其他预测变量有关的离群点。
换句话说，它们是由许多异常的预测变量值组合起来的，与响应变量值没有关系。 

高杠杆值的观测点可通过帽子统计量（hat statistic）判断。
对于一个给定的数据集，帽子均值为p/n，其中p是模型估计的参数数目（包含截距项），n是样本量。
一般来说，若观测点的帽子值大于帽子均值的2或3倍，就可以认定为高杠杆值点。下面代码画出了帽子值的分布：
hat.plot <- function(fit) { 
  p <- length(coefficients(fit)) 
  n <- length(fitted(fit)) 
  plot(hatvalues(fit), main="Index Plot of Hat Values") 
  abline(h=c(2,3)*p/n, col="red", lty=2) 
  identify(1:n, hatvalues(fit), names(hatvalues(fit))) } 
hat.plot(fit)

##### 8.4.3 强影响点

即对模型参数估计值影响有些比例失衡的点。
例如，若移除模型的一个观测点时模型会发生巨大的改变，那么你就需要检测一下数据中是否存在强影响点了。
有两种方法可以检测强影响点：Cook距离，或称D统计量，以及变量添加图（added variable plot）。、一般来说，Cook’s D值大于4/(n–k–1)，则表明它是强影响点，其中n为样本量大小，k是预测变量数目。

可通过如下代码绘制Cook’s D图形
cutoff <- 4/(nrow(states)-length(fit\$coefficients)-2) 
plot(fit, which=4, cook.levels=cutoff) 
abline(h=cutoff, lty=2, col="red") 

Cook’s D图有助于鉴别强影响点，但是并不提供关于这些点如何影响模型的信息。
变量添加图弥补了这个缺陷。对于一个响应变量和k个预测变量，你可以如下图创建k个变量添加图。
所谓变量添加图，即对于每个预测变量Xk，绘制Xk在其他k–1个预测变量上回归的残差值相
对于响应变量在其他k–1个预测变量上回归的残差值的关系图。car包中的avPlots()函数可提
供变量添加图：
library(car) 
avPlots(fit, ask=FALSE, id.method="identify") 

利用car包中的influencePlot()函数，可以将离群点、杠杆值和强影响点的信息整合到一幅图形中：
library(car) 
influencePlot(fit, id.method="identify", main="Influence Plot", 
sub="Circle size is proportional to Cook's distance") 
纵坐标超过+2或小于–2的州可被认为是离群点，水平轴超过0.2或0.3的州有高杠杆值（通常为预测值的组合）。圆圈大小与影响成比例，圆圈很大的点可能是对模型参数的估计造成的不成比例影响的强影响点

### 8.5 改进措施

##### 8.5.1 删除观测点

删除离群点通常可以提高数据集对于正态假设的拟合度，而强影响点会干扰结果，通常也会被删除。
删除最大的离群点或者强影响点后，模型需要重新拟合。若离群点或强影响点仍然存在，重复以上过程直至获得比较满意的拟合。

##### 8.5.2 变量变换

当模型不符合正态性、线性或者同方差性假设时，一个或多个变量的变换通常可以改善或调整模型效果。变换多用Y
λ替代Y，λ的常见值和解释见表8-5。若Y是比例数，通常使用logit变换[ln (Y/1–Y)]。

#### 例 Box-Cox正态变换

library(car) 
summary(powerTransform(states\$Murder))

car包中的boxTidwell()函数通过获得预测变量幂数的最大似然估计来改善线性关系。
library(car) 
boxTidwell(Murder~Population+Illiteracy,data=states) 

### 8.6 选择“最佳”的回归模型

##### 8.6.1 模型比较

基础安装中的anova()函数可以比较两个嵌套模型的拟合优度。
所谓嵌套模型，即它的一些项完全包含在另一个模型中。
在states的多元回归模型中，Income和Frost的回归系数不显著
此时可以检验不含这两个变量的模型与包含这两项的模型预测效果是否一样好

### 例 用anova()函数比较

states <- as.data.frame(state.x77[,c("Murder", "Population", 
                                     "Illiteracy", "Income", "Frost")]) 
fit1 <- lm(Murder ~ Population + Illiteracy + Income + Frost, 
             data=states) 
fit2 <- lm(Murder ~ Population + Illiteracy, data=states) 
anova(fit2, fit1) 

AIC也可以用来比较模型，它考虑了模型的统计拟合度以及用来拟合的参数数目。
AIC值较小的模型要优先选择，它说明模型用较少的参数获得了足够的拟合度。该准则可用AIC()函数实现

#### 例 用AIC来比较模型

fit1 <- lm(Murder ~ Population + Illiteracy + Income + Frost, 
           data=states) 
fit2 <- lm(Murder ~ Population + Illiteracy, data=states) 
AIC(fit1,fit2)
此处AIC值表明没有Income和Frost的模型更佳。注意，ANOVA需要嵌套模型，而AIC方法不需要。

##### 8.6.2 变量选择

从大量候选变量中选择最终的预测变量有以下两种流行的方法：逐步回归法和全子集回归。

1. 逐步回归
   向前逐步回归每次添加一个预测变量到模型中，直到添加变量不会使模型有所改进为止。
   向后逐步回归从模型包含所有预测变量开始，一次删除一个变量直到会降低模型质量为止。
   而向前向后逐步回归（通常称作逐步回归，以避免听起来太冗长），结合了向前逐步回归和向后逐步回归的方法，
   变量每次进入一个，但是每一步中，变量都会被重新评价，对模型没有贡献的变量将会被删除，
   预测变量可能会被添加、删除好几次，直到获得最优模型为止。
   逐步回归法的实现依据增删变量的准则不同而不同。MASS包中的stepAIC()函数可以实现
   逐步回归模型（向前、向后和向前向后），依据的是精确AIC准则。

#### 例 向后回归

library(MASS) 
states <- as.data.frame(state.x77[,c("Murder", "Population", 
                                       "Illiteracy", "Income", "Frost")]) 
fit <- lm(Murder ~ Population + Illiteracy + Income + Frost, 
            data=states) 
stepAIC(fit, direction="backward") 

2. 全子集回归
   全子集回归是指所有可能的模型都会被检验。分析员可以选择展示所有可能的结果，也可以展示n个不同子集大小（一个、两个或多个预测变量）的最佳模型。例如，若nbest=2，先展示两个最佳的单预测变量模型，然后展示两个最佳的双预测变量模型，以此类推，直到包含所有的预测变量。
   全子集回归可用leaps包中的regsubsets()函数实现。

#### 例 全子集回归

library(leaps) 
states <- as.data.frame(state.x77[,c("Murder", "Population", 
"Illiteracy", "Income", "Frost")]) 
leaps <-regsubsets(Murder ~ Population + Illiteracy + Income + 
Frost, data=states, nbest=4) 
plot(leaps, scale="adjr2") 
library(car) 
subsets(leaps, statistic="cp", 
main="Cp Plot for All Subsets Regression") 
abline(1,1,lty=2,col="red") 

### 8.7 深层次分析

##### 8.7.1 交叉验证

bootstrap包中的crossval()函数可以实现k重交叉验证。

#### 例 R平方的k重交叉验证

shrinkage <- function(fit, k=10){ 
require(bootstrap) 
theta.fit <- function(x,y){lsfit(x,y)} 
theta.predict <- function(fit,x){cbind(1,x)%*%fit\$coef} 
x <- fit\$model[,2:ncol(fit$model)] 
y <- fit\$model[,1] 
results <- crossval(x, y, theta.fit, theta.predict, ngroup=k) 
r2 <- cor(y, fit\$fitted.values)^2 
r2cv <- cor(y, results\$cv.fit)^2 
cat("Original R-square =", r2, "\n") 
cat(k, "Fold Cross-Validated R-square =", r2cv, "\n") 
cat("Change =", r2-r2cv, "\n") } 
states <- as.data.frame(state.x77[,c("Murder", "Population", 
"Illiteracy", "Income", "Frost")]) 
fit <- lm(Murder ~ Population + Income + Illiteracy + Frost, data=states) 
shrinkage(fit)
fit2 <- lm(Murder ~ Population + Illiteracy,data=states) 
shrinkage(fit2)

##### 8.7.2 相对重要性

states <- as.data.frame(state.x77[,c("Murder", "Population", 
                                     "Illiteracy", "Income", "Frost")]) 
zstates <- as.data.frame(scale(states)) 
zfit <- lm(Murder~Population + Income + Illiteracy + Frost, data=zstates) 
coef(zfit)

#### 例 relweights()函数，计算预测变量的相对权重

relweights <- function(fit,...){ 
R <- cor(fit\$model) 
nvar <- ncol(R) 
rxx <- R[2:nvar, 2:nvar] 
rxy <- R[2:nvar, 1] 
svd <- eigen(rxx) 
evec <- svd\$vectors 
ev <- svd\$values 
delta <- diag(sqrt(ev)) 
lambda <- evec %\*% delta %\*% t(evec) 
lambdasq <- lambda ^ 2 
beta <- solve(lambda) %\*% rxy 
rsquare <- colSums(beta ^ 2) 
rawwgt <- lambdasq %\*% beta ^ 2 
import <- (rawwgt / rsquare) * 100 
import <- as.data.frame(import) 
row.names(import) <- names(fit\$model[2:nvar]) 
names(import) <- "Weights" 
import <- import[order(import),1, drop=FALSE] 
dotchart(import\$Weights, labels=row.names(import), 
xlab="% of R-Square", pch=19, 
main="Relative Importance of Predictor Variables", 
sub=paste("Total R-Square=", round(rsquare, digits=3)), ...) 
return(import) } 

##### 例 relweights()函数的应用

states <- as.data.frame(state.x77[,c("Murder", "Population", 
                                     "Illiteracy", "Income", "Frost")]) 
fit <- lm(Murder ~ Population + Illiteracy + Income + Frost, data=states) 
relweights(fit, col="blue") 