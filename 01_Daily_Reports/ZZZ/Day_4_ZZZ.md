# R in Action

## Advanced data management

### Numerical and character functions

#### Mathematical functions

```R
abs(x)   sqrt(x)
ceiling(x)   floor(x)
trunc(x)   round(x, digits=n)
signif(x, digits=n)
cos sin tan acos asin atan cosh sinh tanh acosh asinh atanh
log(x,base = n) log(x)  log10(x)  exp(x)
```

#### Statistical functions

```R
z <- mean(x, trim = 0.05, na.rm=TRUE)
mean()  median() sd() var() 
mad() ## median absolute deviation
quantile(x, probs) ## quantile(x, c(.3,.84))
range()  sum()  diff(x,lag=n)## lagged differences delat between values
min() max() scale(x,center=TRUE,scale=TRUE) ## Column center or standardize

newdata <- scale(mydata)# standarizes the specified df
newdata <- transform(mydata, myvar = scale(myvar)*10+50) ## one col
```

#### Probability functions

```R
[dpqr]distribution_abbreviation()
d = density
p = distribution function
q = quantile function
r = random generation (random deviates)
    
beta
binom #Binomial
cauchy 
chisq #noncentral Chi-squared
exp #Exponential
f
gamma
geom
hyper
lnorm # Lognormal
logis
multinom # multinomial
nbinom # Negative binomial
norm
pois # poisson
signrank # Wilcoxon signed rank
t
unif
weibull
wilcox # wilcoxon rank sum
runif #pseudo-random numbers from a uniform distribution

x <- pretty(c(-3,3), 30)
y <- dnorm(x)
plot(x, y)

pnorm(1.96)
qnorm(.9, mean=500, sd=100)
rnorm(50, mean=50, sd=10)
```

##### Setting the seed for random number generation

```R
runif(5)
set.seed(2)
runif(5)
```

##### Generating multivariate normal data

```R
library(MASS)
options(digits=3)
set.seed(12)
mean<- c(230.7, 146.7, 3.6)  
sigma <- matrix(c(15360.8, 6721.2, -47.1, 
                  6721.2, 4700.9, -16.5,                   
                  -47.1,  -16.5,   0.3), nrow=3, ncol=3)
mydata <- mvrnorm(500, mean, sigma) 
mydata <- as.data.frame(mydata)  
names(mydata) <- c("y","x1","x2")
dim(mydata)
head(mydata, n=10)        
```

#### Character functions

```R
# number of characters
nchar()
x <- c("ab", "cde", "fghij")
length(x) 
nchar(x[3])

# extracts or replace substrings
substr(x, start, stop)
x <- "abcdef" 
substr(x, 2, 4) 
substr(x, 2, 4) <- "22222"

# grep find 
grep(pattern, x, ignore.case=FALSE, fixed=FALSE)

# replace 
sub(pattern, replacement, x, ignore.case=FALSE, fixed=FALSE)

# splits
strsplit(x, split, fixed=FALSE)

# concatenates string 
paste(..., sep="")

# Uppercase
toupper(x)

# Lowercase
tolower(x)
```

#### Useful functions

```R
length()
seq(from,to,by)

#Repeats x n times.
rep(x,n)
y <- rep(1:3, 2)
> c(1, 2, 3, 1, 2, 3)

# divides the continuous variable x into a factor with n levels
cut(x,n)

# creates pretty breakpoints
pretty(x,n)

# concatenates the objects in 
cat(... , file = "myfile", append = FALSE)
cat("Hello" , name, "\n")
# cat separate each by a space so use \b

#
show()
\n 
\t 
\'
\b
?Quotes
```

#### Applying functions to matrices and data frame

```R
# apply
apply(x, MARGIN, FUN, ...)
# margin : demension
mydata <- matrix(rnorm(30), nrow=6)
apply(mydata, 1, mean) 
apply(mydata, 2, mean)
apply(mydata, 2, mean, trim=0.2)
```

### A solution for the data-management challenge

```R
options(digits=2)  
 Student <- c("John Davis", "Angela Williams", "Bullwinkle Moose" ,"David Jones", "Janice Markhammer", "Cheryl Cushing" ,"Reuven Ytzrhak", "Greg Knox", "Joel England","Mary Rayburn")                                      
Math <- c(502, 600, 412, 358, 495, 512, 410, 625, 573, 522)       
Science <- c(95, 99, 80, 82, 75, 85, 80, 95, 89, 86)              
English <- c(25, 22, 18, 15, 20, 28, 15, 30, 27, 18)              
roster <- data.frame(Student, Math, Science, English, stringsAsFactors=FALSE)

z <- scale(roster[,2:4]) 
score <- apply(z, 1, mean)
roster <- cbind(roster, score)

y <- quantile(score, c(.8,.6,.4,.2)) 
roster$grade[score >= y[1]] <- "A"                                
roster$grade[score < y[1] & score >= y[2]] <- "B"             
roster$grade[score < y[2] & score >= y[3]] <- "C"               
roster$grade[score < y[3] & score >= y[4]] <- "D"               
roster$grade[score < y[4]] <- "F"      

name <- strsplit((roster$Student), " ")
Lastname <- sapply(name, "[", 2)
Firstname <- sapply(name, "[", 1)
roster <- cbind(Firstname,Lastname, roster[,-1])
roster <- roster[order(Lastname,Firstname),]
```

### Control flow

```R
## repetition and looping
for (var in seq) statement
while (cond) statement

## conditional execution
if (cond) statement1 else statement2
ifelse (cond,statement1,statement2)
switch (expr, ...)
```

### User-written functions

```R
myfunction <- function(arg1,arg2,...){
	statements
    return(object)
}

mystats <- function(x, parametric=TRUE, print=FALSE) {
  if (parametric) {
    center <- mean(x)
    spread <- sd(x) 
  } else {
    center <- median(x)
    spread <- mad(x) 
  }
  if (print & parametric) {
    cat("Mean=", center, "\n", "SD=", spread, "\n")
  } else if (print & !parametric) {
    cat("Median=", center, "\n", "MAD=", spread, "\n")
  }
  result <- list(center=center, spread=spread)
  return(result)
}

set.seed(1234)
x <- rnorm(500) 
y <- mystats(x)
y <- mystats(x, parametric=FALSE, print=TRUE)

mydate <- function(type="long") {
  switch(type,
         long =  format(Sys.time(), "%A %B %d %Y"),
         short = format(Sys.time(), "%m-%d-%y"),
         cat(type, "is not a recognized type\n")        
   )
}

warning()
message()
stop()

venables&ripley 2000
chambers 2008
```

### Aggregation and reshaping

```R
cars <- mtcars[1:5,1:4]
t(cars) ## transpose

## aggregating
aggregate(x, by, FUN) 
# by group by

attach(mtcars)
aggdata <-aggregate(mtcars, by=list(cyl,gear), FUN=mean, na.rm=TRUE)
```

#### Reshape2

```R
library(reshape2)
#melting
md <- melt(mydata, id=c("ID", "Time"))
#casting
newdata <- dcast(md, formula, fun.aggregate)


```

* In formula,rowvar1 + rowvar2 + ... ~ colvar1 + colvar2 + ...
* rowvar1 + rowvar2+... defines the set of crossed variables that define the rows
* colvar1 + colvar2 + .. defines the set of crossed variables that define the columns