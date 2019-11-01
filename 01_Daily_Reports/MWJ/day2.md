# R语言的数据结构
### 1）向量 vector
##### 用于存储数值类型（123），字符型类型（abc)，或者逻辑型的一堆数组(TRUE,FALSE)(p-布尔数组第一个字母大写）
#####  单个向量中必须是相同的数据类型（p is not）
#####   访问向量中第n个元素，a[n] (p-a[n-1])
#####   访问向量第一个和第四个，a[c(1,4)],(p-a[0,3])
***

### 2）矩阵 matrix(类似numpy)
##### 二维数据集matrix(vector,ncol,nrow,byrow=FALSE,dimnames=list(,))
##### 例如; `m1<-matrix(1:20,nrow=5,ncol=4)#按照列排列`
##### 若想按照列排序，`m2<-matrix(1:20,nrow=5,ncol=4,byrow=TRUE)`
##### dimnames指的是定义行列的名字
##### 访问矩阵的元素:
* m1[2,4] 访问第二行第四列的元素-(p: m1[1,3]
* m1[2,c(2,3)] 访问第二行第三和第四列的元素（p: m1[1,1:2])
* m1[3,]访问第三行所有元素（p:m1[2,:])
* m1[,4]访问第四列所有元素（p:m1[:,3])
##### 与numpy,索引不同（没有：）
##### numpy中创建array的方法（np.arange(),np.linspace(),np.zeros/ones/full(shape=(),fill_value=),np.random.randint/random/normal(size=))
***
### 3）数组 array
##### 与矩阵类似，但是唯独可以大于2
##### array(vector,dimension,dimnames=list(,,))
#####  例如`array1<-array(1:24,c(2,3,4))` 表示1-24个数字，2×3的矩阵，一共4个矩阵，dimnames可以取三个分别是行，列，每个矩阵名
```n1<-c('a',"b")
n2<-c('A','B','C')
n3<-c(1,2,3,4)
a<-array(1:24,c(2,3,4),dimnames = list(n1,n2,n3))
a
```
##### 访问数组的元素 a[2,3,1]表示防问第一个矩阵中的第二行第三列的元素
***
### 4) 数据框 DataFrame（类似于pandas)
##### 数据框：由不同列（可以是不同的数据类型）组成的
##### 数据框的生成 data.frame(col1,col2,col3....)
```
age<-c(22,34,45)
gender<-c('female','male','male')
grade<-c(100,80,78)
b<-data.frame(age,gender,grade)
b
```
``` age gender grade
1  22 female   100
2  34   male    80
3  45   male    78
```
##### 与pandas不同，df=DataFrame(_,index=,columns=)（写法不同）
##### 访问数据框的元素I（三种方式），通过下标，通过列名，通过美元符号,类似于pandas的.loc[数字],.iloc[字符型]，.ix[混合型]
***
### 5) 列表 list

##### 一些对象的有序集合，对象有可能是向量，矩阵，数组，数据框，其他的列表
##### 列表生成 list1<-list(obj1,obj2,obj3,..)
##### 访问列表的元素list,list[[]]/list$obj2

***
### 总结：
##### 五种数据结构（向量（一维），矩阵（二维），数组（多维），数据框（数值可以不同类型），列表（包含多种对象））
##### p中数据结构（list,dict,tuple,numpy矩阵，pandas数据框）