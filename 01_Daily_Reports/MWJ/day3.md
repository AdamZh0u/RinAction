### 导入和导出数据(涉及的四个函数）
***
#### 1)getwd() 得到当前文件存放的工作目录
'getwd()'
'C:/Users/24322/Documents'
#### 2)setwd() 重新设置当前文件存放的工作目录
#### 3）read.csv('数据文件所在的工作目录')导入数据文件
#### 4）write.csv(数据集，’定义一个文件名称‘)导出数据文件
#### (p不一样，导入数据pd.read_csv(r''),导出数据data.to_pickle())
***
### 数据框dataframe的常用操作函数
***
#### 1）简化数据框批量操作
##### 方法一：atttach(dataframe)
##### 操作1
##### 操作2
##### 操作n
##### detach(dataframe)
```
mtcars
df1<-head(mtcars)
df1<-df1[1:3]
df1
df1$mpg
attach(df1)
mpg
disp
detach(df1)
```
```                      mpg cyl disp
Mazda RX4         21.0   6  160
Mazda RX4 Wag     21.0   6  160
Datsun 710        22.8   4  108
Hornet 4 Drive    21.4   6  258
Hornet Sportabout 18.7   8  360
Valiant           18.1   6  225
```
```
> attach(df1)
> mpg
[1] 21.0 21.0 22.8 21.4 18.7 18.1
> disp
[1] 160 160 108 258 360 225
> detach(df1)
```
##### 方法二：with(dataframe,{
##### 操作1
##### 操作2
##### 操作n
##### })
```
df1$mpg+df1$cyl+df1$disp
with(df1,{
  mpg+cyl+disp
})
```
```
> df1$mpg+df1$cyl+df1$disp
[1] 187.0 187.0 134.8 285.4 386.7 249.1
[1] 187.0 187.0 134.8 285.4 386.7 249.1
```
#### 2)增加数据框变量（列）
##### 方法一：within(dataframe,{
##### 操作1
##### 操作2
##### 操作n
##### })
```
df1<-within(df1,{
  sum=mpg+cyl+disp
  mean=(mpg+cyl+disp)/3
})
df1
```
```
> df1
                   mpg cyl disp      mean   sum
Mazda RX4         21.0   6  160  62.33333 187.0
Mazda RX4 Wag     21.0   6  160  62.33333 187.0
Datsun 710        22.8   4  108  44.93333 134.8
Hornet 4 Drive    21.4   6  258  95.13333 285.4
Hornet Sportabout 18.7   8  360 128.90000 386.7
Valiant           18.1   6  225  83.03333 249.1
```
##### 方法二：transform（dataframe,操作1，...,操作n)
```
df3<-transform(df1,s=mpg+cyl+disp,m=(mpg+cyl+disp)/3)
df3
```
```
                   mpg cyl disp      mean   sum     s
Mazda RX4         21.0   6  160  62.33333 187.0 187.0
Mazda RX4 Wag     21.0   6  160  62.33333 187.0 187.0
Datsun 710        22.8   4  108  44.93333 134.8 134.8
Hornet 4 Drive    21.4   6  258  95.13333 285.4 285.4
Hornet Sportabout 18.7   8  360 128.90000 386.7 386.7
Valiant           18.1   6  225  83.03333 249.1 249.1
                          m
Mazda RX4          62.33333
Mazda RX4 Wag      62.33333
Datsun 710         44.93333
Hornet 4 Drive     95.13333
Hornet Sportabout 128.90000
Valiant            83.03333
```
##### 方法三：dplyr包中的mute(dataframe,操作1，...,操作n)
```
install.packages('dplyr')
library(dplyr)
df2<-mute(df1,(s1=mpg+cyl+disp,m1=(mpg+cyl+disp)/3))
df2
```
```
                   mpg cyl disp      mean   sum
Mazda RX4         21.0   6  160  62.33333 187.0
Mazda RX4 Wag     21.0   6  160  62.33333 187.0
Datsun 710        22.8   4  108  44.93333 134.8
Hornet 4 Drive    21.4   6  258  95.13333 285.4
Hornet Sportabout 18.7   8  360 128.90000 386.7
Valiant           18.1   6  225  83.03333 249.1
```
##### transform新创建的变量不能调用，mute可以