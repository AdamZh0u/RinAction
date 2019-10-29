# R in Action

## Introduction to R

### Working with R

```flow
s=>start: Import Data
e=>end: Produce report
P=>operation: Prepare,explore,and clean data
F=>operation: Fit a statistical model
C=>operation: Cross-validate the model
E1=>operation: Evaluate the model fit 
E2=>operation: Evaluate model prediction on new data

s->P->F->E1->C->E2->e
```

* R is a case-sensitive, interpreted language.
* For R, everything has an class attribute telling R how to handle it.
* Get help `example(foo)` `apropos("foo",mode=funtion)` `data()`.

### Workspace

```R
getwd()
setwd()
ls()
```

### Input and Output

```R
soure("filename")# input module
sink("filename",expand=TRUE, split=TRUE) # text output redirect
png("filename.png")
pdf("filename.pdf")
```

### Packages

```R
.libPath() # lib path
library()# installed lib
search()# loaded lib
install.packages()
```

### Example

```R
help.start()
install.packages("vcd")
help(package="vcd")
library(vcd)
data()
help(Arthritis)# discribe data
Arthritis
example(Arthritis)
```

---

## Creating a dataset

### Data Structures

*  Vectors: one-dimensional arrays.

    * ```R
        a<-c(1,2,4)#numeric 
        a<-c(1:10)
        b<-c("one","two")#character
        c<-c(TRUE,FALSE)#logical
        d<-4#scalas
        ```

    * ```R
        #Slice
        a[(1,3)]
        a[1:3]
        a[3]
        ```

* Matrix: two-dimensional array.

    * ```R 
        matrix <- matrix(vector, nrow=number_of_rows, ncol=number_of_columns,
                         byrow=logical_value, #filled in by row
                         dimnames=list(char_vector_rownames,char_vector_colnames))
        ```

    * ```R
        y<-matrix(1:20,nrows=5,ncol=4)
        ```

    * ```R
        cells <- c(1,26,24,68)
        rnames <- c("R1", "R2")
        cnames <- c("C1", "C2") 
        mymatrix <- matrix(cells, nrow=2, ncol=2, 
                           byrow=TRUE,dimnames=list(rnames, cnames)) 
        ```

    * ```R
        #slice
        x[i,j]
        x[i,]
        x[,j]
        x[i,c(1,2)]
        ```

* **Array**: can be more than two dimensions.

    * ```R
        myarray <- array(vector, dimensions, dimnames)
        dim1 <- c("A1", "A2")
        dim2 <- c("B1", "B2", "B3")
        dim3 <- c("C1", "C2", "C3", "C4")
        z <- array(1:24, c(2, 3, 4), dimnames=list(dim1, dim2, dim3))
        z[1,3,4]
        ```

* **Data frames**: different columns contain different modes of data

    * ```R
        mydata <- data.frame(col1, col2, col3,...)
        patientdata[1:2]
        patientdata[c("diabetes", "status")]
        # cross-tabulate 
        table(patientdata$diabetes, patientdata$status)
        ```

    * ```R
        attach(df)
        plot(col1,col2)
        detach(df)
        ```

    * ```R
        # with
        with(df,{
            print(summary(df))
            plot(col1,col2)
        })
        #
        with(df,{
            a<-col1  # Local variable
            b<<-col2 # global
        })
        ```

    * ```R
        # case identifier
        patientdata <- data.frame(patientID, age, diabetes, 
                                  status, row.names=patientID)
        ```

    * 

* Factors: Categorical(nominal) and ordered categorical(ordinal) variables in R.

    * nominal example: type 1, type 2.

    * ordinal example: small, big.

    * ```R
        types <- c("Type1", "Type2", "Type1", "Type1")
        nominal <- factor(types)
        #created in alphabetical order by default
        status <- c("Poor", "Improved", "Excellent")
        ordinal <- factor(status, ordered=TRUE) 
        #specifying a levels option
        ordinal <- factor(status, order=TRUE, 
                         levels=c("Poor", "Improved", "Excellent"))
        # convert to unordered factor
        sex <- factor(sex, levels=c(1, 2), labels=c("Male", "Female"))
        ```

    * ```R
        patientID <- c(1, 2, 3, 4)
        age <- c(25, 34, 28, 52)
        diabetes <- c("Type1", "Type2", "Type1", "Type1")
        status <- c("Poor", "Improved", "Excellent", "Poor")
        diabetes <- factor(diabetes)
        status <- factor(status, order=TRUE)
        patientdata <- data.frame(patientID, age, diabetes, status)
        str(patientdata)#str(object) provides information about an object in R
        summary(patientdata)#
        ```

* List： an ordered collections of objects

    * ```R
        mylist <- list(object1, object2)
        mylist <- list(name1=object1, name2=object2)
        mylist[[2]]
        mylist$columnsname
        ```

    * list is important in R:

        * organize and recall disparate information in simple way
        * many R function return lists making it easy for analysis to decide which part they want

    > It is allowed to assign a value to a nonexistent element of any data structures in R.
    >
    > But not in Python.

### Data Input

#### Keyboard Input

```R
mydata <- data.frame(age=numeric(0), gender=character(0), weight=numeric(0))
mydata <- edit(mydata)
```

#### Delimited text file

* default transfer into factors

* ```R
    grades <- read.table("studentgrades.csv", header=TRUE,
        row.names="StudentID", sep=",",
        colClasses=c("character", "character", "character",  
                     "numeric", "numeric", "numeric"))
    ## use colClasses to define date type
    # na.string=c(-1,-9) transfer to NA
    # skip =5 skip five lines
    # stringAsFactors =TRUE 
    ```

#### Excel

* packages: xlsx, xlsxjars, rJava

* ```R
    library(xlsx)
    workbook <- "c:/myworkbook.xlsx"
    mydataframe <- read.xlsx(workbook, 1)
    ```

#### Web

* API -> readLines() -> grep(),gsub()
* Rcurl, XML
* twitteR, Rfacebook, Rflickr

#### DBMSs

* Hadoop

### Annotating datasets

### Useful function

```R
length()
dim()
class()
str()
mode()
names()
cbind()# combines as columns
rbind()# combines as rows
head()
tail()
ls()
fix()# edits an object in place
summary()
edit()
```



