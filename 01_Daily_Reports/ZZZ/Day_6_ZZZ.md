## Basic Statistics

### Descriptive statistics

* summary

```R
x<-mtcars[c("mpg","hp","wt")]
head(x)
summary(x)
```

* sapply 

  sapply(x,FUN,options)

```R
mystats <- function(x,na.omit=F){
  if (na.omit)
    x <- x[!is.na(x)]
  m <- mean(x)
  n <- length(x)
  s <- sd(x)
  skew <- sum((x-m)^3/s^3)/n
  kurt <- sum((x-m)^4/s^4)/n
  return(c(length=n,mean=m,stdev=s,skew=skew,kurtosis=kurt))
}
sapply(x, mystats) 
sapply(x, mystats,na.omit=T) 
```

* Hmisc::describe()
* pastecs::stat.desc()
* psych::describe()

### Descriptive statistics by group

```R
aggregate(mtcars[myvars], by=list(am=mtcars$am), mean)

dstats <- function(x)sapply(x, mystats) 
by(x, mtcars$am, dstats) 

library(doBy)
summaryBy(mpg+hp+wt~am, data=mtcars, FUN=mystats) 

library(psych)  
describeBy(x, list(am=mtcars$am)) 
```

### Frequency and contingency tables

```R
library(vcd)  
mytable <- with(Arthritis, table(Improved)) #  frequency  counts
prop.table(mytable)#  turn frequencies into proportions

# two-way tables
mytable <- table(A, B) 
mytable <- xtabs(~ Treatment+Improved, data=Arthritis) 
margin.table(mytable, 1) #  marginal frequencies

# gmodels
library(gmodels) 
CrossTable(Arthritis$Treatment, Arthritis$Improved) 
mytable <- xtabs(~ Treatment+Sex+Improved, data=Arthritis) 
ftable(mytable) 
margin.table(mytable, 1)  
margin.table(mytable, c(1, 3))
ftable(prop.table(mytable, c(1, 2)))    
```

#### Test of independence

* chi-square

```R
library(vcd)
mytable <- xtabs(~Treatment+Improved, data=Arthritis)  
chisq.test(mytable)  
fisher.test(mytable)  
mantelhaen.test(mytable) 
```

* fisher
*  Cochran-Mantel-Haenszel

#### Measures of association

```R
assocstats(mytable) 
```

### Correlations

*  Pearson product-moment correlation assesses the degree of linear relationship
    between  two  quantitative  variables
*  Spearman’s  rank-order  correlation  coefficient assesses the degree of relationship between two rank-ordered variables. 
*  Kendall’s tau is  a nonparametric measure of rank correlation. 

```R
cov(states) 
cor(states, method="spearman") 
cor(x,y) 
```

* partial correlations

```R
pcor(c(1,5,2,3,6), cov(states))
```

#### Testing correlations for significance

```R
cor.test(states[,3], states[,5])
corr.test(states, use="complete") 
```

### T-tests

#### Independent t-test

```R
t.test(y1, y2)
```

#### Dependent t-test

```R
t.test(y1, y2, paired=TRUE) 
sapply(UScrime[c("U1","U2")], function(x)(c(mean=mean(x),sd=sd(x))))
```

