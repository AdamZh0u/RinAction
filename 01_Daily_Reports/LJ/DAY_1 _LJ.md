# DAY_1 第一二章

## 第一章 R语言介绍

### 1.1 R语句的赋值

使用==<-==,而不是传统的=，例如x<-rnorm(5)，意为创建了一个名为x的向量对象，包含5个来自标准正态分布的随机偏差

注释由==符号#==开头，在#之后出现的任何文字都会被R解释器忽略

### 1.2 获取帮助

|        函数        |               功能                |
| :----------------: | :-------------------------------: |
|    help.start()    |         打开帮助文档首页          |
| help("foo")或？foo | 查看函数foo的帮助（引号可以省略） |

等等，具体可见教材1.3.2（p10）

### 1.3 管理R工作空间

可以运用一系列函数显示或调用工作空间，具体函数及功能可见教材1.3.3（p11）

### 1.4 输入和输出

R可以灵活规定文本、图像的输入和输出，以及其需要保存的内容

### 1.5 包

很多功能可以通过包来实现。先安装后载入，==安装仅需一次==，载入在==一个会话==中需要一次

### 1.6 R语言编程中的常见错误

1. 大小写
2. 必要的引号
3. 函数调用时的括号
4. windows中的路径名误用\
5. 使用尚未载入包的函数

## 第二章 创建数据集

### 2.1 数据集的概念

行称为观测，列称为变量

标量、向量、数组、数据框和列表都可以用来==存储数据==

R可以处理数值型、字符型、逻辑型、复数型和原生型数据

### 2.2 数据结构

#### 2.2.1 向量

  同一向量中无法混杂不同模式的数据  

#### 2.2.2 矩阵

可通过函数matrix()创建矩阵  

#### 2.2.3 数组（array）

与矩阵类似，但是维度可以大于2

#### 2.2.4 数据框

  数据框可通过函数data.frame()创建 

   数据框可以将不同模式（数值型、字符型等）的数据放入一个矩阵

  每一列数据的模式必须唯一，但可以将多个模式的不同列放到一起组成数据框。  

\$可用作生成两个数据的连列表

  函数attach()和detach()多在分析一个单独的数据框，并且没有多个同名对象时使用；如果有多个==同名数据==，可以考虑使用==函数with()==

  函数with()的局限性在于，赋值仅在==此函数的括号内==生效。  

#### 2.2.5 因子

  要表示**有序型变量**，需要为函数factor()指定参数==ordered=TRUE==

  对于**字符型向量**，因子的水平默认依字母顺序创建，可以通过指定==levels选项==来覆盖默认排序  

**数值型变量**可以用==levels和labels==参数来编码成因子

**后面的例子需要再看一下**

#### 2.2.6 列表

列表中可以是若干向量、矩阵、数据框，甚至其他列表的组合，使用函数list()创建列表  

### 2.3 数据的输入

#### 2.3.3 导入excel文件

可以用xlsx包直接导入Excel工作表(注意需要下载和安装)

###  2.6 小结

有关函数导入、导出以及结构的问题需要再仔细阅读

