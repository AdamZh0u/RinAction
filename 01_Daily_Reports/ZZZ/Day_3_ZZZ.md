# R in Action

##  Basic Data Management

### Leadership data frame

```R
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

## mean deferantial score

## handling incomplete data

## create a subset dataset

## recode

## limit data period

```

### Creating new variables

```R
## Arithmetic operators
+ - * /
^ or ** ## Exponentiation
x%%y ## modulus
x%/%y ## integer division

## 3 ways to incorporate new variables into the origin data frame 
mydata$sumx  <-  mydata$x1 + mydata$x2
mydata$meanx <- (mydata$x1 + mydata$x2)/2

attach(mydata)
mydata$sumx  <-  x1 + x2
mydata$meanx <- (x1 + x2)/2
detach(mydata)

mydata <- transform(mydata,
                    sumx  =  x1 + x2,
                    meanx = (x1 + x2)/2)## create and add
```



### Recoding variables

```R
## logical operators
< <= > >= == !=
!x ## not x    
x|y ## x or y
x&y ## x and y
isTRUE(x) ## whether x is True

## Change a continuous variables into a set of categories
## Replace miscoded values  with correct values
## Create a pass/fail variable based on a set of cutoff scores
leadership$age[leadership$age  == 99]     <- NA

leadership$agecat[leadership$age  > 75]   <- "Elder"
leadership$agecat[leadership$age >= 55 & 
                  leadership$age <= 75]   <- "Middle Aged"
leadership$agecat[leadership$age  < 55]   <- "Young"

leadership <- within(leadership,{
                     agecat <- NA
                     agecat[age > 75]              <- "Elder"
                     agecat[age >= 55 & age <= 75] <- "Middle Aged"
                     agecat[age < 55]              <- "Young" })
## within allows to modify the data frame      with()
## recoding functions
library(car)
recode()
library(doBy)
recodevar()

cut() in R

```



### Renaming variables

```R
names(leadership)[2] <- "testData"
names(leadership)[6:10] <- c("item1", "item2", "item3", "item4", "item5")

library(plyr)
rename(dataframe, c(oldname="newname", oldname="newname",...))
leadership <- rename(leadership, 
                     c(manager="managerID", date="testDate"))
```

### Missing value

* about NA
    * NA for character and numeric is the same
    * is.na() to test whether it is na
    * ==na is never TRUE
    * Inf and -Inf :  5/0
    * NaN : sin(Inf)  not a number 

```R
## recoding values to missing
leadership$age <- NA
leadership$age[leadership$age == 99] <- NA

## Excluding missing value from analyses
na.rm = TRUE
x <- c(1, 2, NA, 3)
y <- sum(x, na.rm=TRUE)

na.omit(df)
newdata <- na.omit(leadership)

```

### Data values

| Symbol |        Meaning        | Example |
| :----: | :-------------------: | :-----: |
|   %d   |     day as number     |  1-31   |
|   %a   |  Abbreviated weekday  |   Mon   |
|   %A   | Unabbreviated weekday | Monday  |
|   %m   |         month         |  00-12  |
|   %b   |   Abbreviated month   |   Jan   |
|   %B   |  Unabbreviated month  | January |
|   %y   |    Two-digit year     |   19    |
|   %Y   |    four-digit year    |  2019   |

```R
as.Date(x, "input_format")
strDates <- c("01/05/1965", "08/16/1975")
dates <- as.Date(strDates, "%m/%d/%Y")

Sys.date()## today's date
date()## current date and time

today <- Sys.Date()
format(today, format="%B %d %Y")

## perform arithmetic operations on date
startdate <- as.Date("2004-02-13")
enddate   <- as.Date("2011-01-22")
days      <- enddate - startdate

difftime(enddate, startdate, units="weeks")

## Converting dates to character variables
strDates <- as.character(dates)
```

### Type conversions

|      Test       |     Convert     |
| :-------------: | :-------------: |
|  is.numeric()   |  as.numeric()   |
| is.character()  | as.character()  |
|   is.vector()   |   as.vector()   |
|   is.matrix()   |   as.matrix()   |
| is.data.frame() | as.data.frame() |
|   is.factor()   |   as.factor()   |
|  is.logical()   |  as.logical()   |

### Sorting data

```R
newdata <- leadership[order(leadership$age),]
newdata <- leadership[order(leadership$age, -leadership$gender),] # add - to indicate descending 
```

### Merge data

#### Merge Cols

```R
total <- merge(dataframeA, dataframeB, by="ID")
total <- merge(dataframeA, dataframeB, by=c("ID","Country")) 

## dont need a specified common key
total <- cbind(A, B)
```

#### Merge rows

```R
total <- rbind(dataframeA, dataframeB) 
```

### Subset datasets

#### Selecting

```R
dataframe[row indices, column indices]

myvars <- c("q1", "q2", "q3", "q4", "q5") 
newdata <-leadership[myvars]

myvars <- paste("q", 1:5, sep="") 
newdata <- leadership[myvars]

```

#### Excluding

```R
myvars <- names(leadership) %in% c("q3", "q4") 
newdata <- leadership[!myvars]

newdata <- leadership[c(-8,-9)]

leadership$q3 <- leadership$q4 <- NULL
```

#### Selecting observations

```R
newdata <- leadership[1:3,] 
newdata <- leadership[leadership$gender=="M" &            
                      leadership$age > 30,]  

leadership$date <- as.Date(leadership$date, "%m/%d/%y")
startdate <- as.Date("2009-01-01") 
enddate   <- as.Date("2009-10-31")

newdata <- leadership[which(leadership$date >= startdate &   
           leadership$date <= enddate),]


```

#### The subset() function

```R
newdata <- subset(leadership, age >= 35 | age < 24,
                  select=c(q1, q2, q3, q4))  
newdata <- subset(leadership, gender=="M" & age > 25,  
                  select=gender:q4) 
```

#### Random samples

```R
mysample <- leadership[sample(1:nrow(leadership), 3, replace=FALSE),] 
## vector to choose from
## number of elements
## sampling without replacement 
library(sampling)
library(survey)
```

### Using SQL

```R
library(sqldf)
```

