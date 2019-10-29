# Day1 R笔记

## Chapter 1 R语言介绍

1. R是一种**区分大小写**的解释型语言。

2. R语句由函数和赋值构成。R使用<-作为**赋值符号**。

3. 帮助函数

   <img src="C:%5CUsers%5Cshirl%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20191029154428059.png" alt="image-20191029154428059" style="zoom: 67%;" />

   函数help.start()会打开一个浏览器窗口，可在其中查看入门和高级的帮助手册、常 见问题集，以及参考材料。函数RSiteSearch()可在在线帮助手册和R-Help邮件列表的讨论存 档中搜索指定主题，并在浏览器中返回结果。由函数vignette()函数返回的vignette文档一般是 PDF格式的实用介绍性文章。

4. 用于管理R工作空间的函数

   <img src="C:%5CUsers%5Cshirl%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20191029154947498.png" alt="image-20191029154947498" style="zoom: 67%;" />

   注：

   * 之前输入过的命令可进行修改，并重新执行。
   * setwd()命令的路径中需使用正斜杠/。且需使用引号闭合目录名和文件名。
   * 可以使用函数dir.create()来创建新目录，然后使用setwd() 将工作目录指向这个新目录。

5. 输入及输出

   * 输入：

     函数source("*filename*")可在当前会话中执行一个脚本。如果文件名中不包含路径，R将 假设此脚本在当前工作目录中。

   * 文本输出：

     函数sink("*filename*")将输出重定向到文件filename中。默认情况下，如果文件已经存在， 则它的内容将被覆盖。使用参数append=TRUE可以将文本追加到文件后，而不是覆盖它。参数 split=TRUE可将输出同时发送到屏幕和输出文件中。不加参数调用命令sink()将仅向屏幕返回 输出结果。

   * 图像输出：

     <img src="C:%5CUsers%5Cshirl%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20191029160620104.png" alt="image-20191029160620104" style="zoom:67%;" />

     最后使用dev.off()将输出返回到终端。

6. 包

   下载包的地址：http://cran.r-project.org/web/packages

   * 包的安装及更新

     第一次安装一个包，使用命令install.packages()即可。

     使用命令update.packages()可以更新已经安装的包。

   * 要在R会话中使用它， 还需要使用library()命令载入这个包。在一个会话中，包只需载入一次。可以自定义启动环境以自动载入会频繁使用的那些包。

7. 

8. 

9. 批处理

   对于Windows，需在终端窗口使用： 

   "C:\Program Files\R\R-3.1.0\bin\R.exe" CMD BATCH  

   ➥ --vanilla --slave "c:\my projects\myscript.R"  

   将路径调整为R.exe所在的相应位置和脚本文件所在位置。

10. 输出结果的进一步分析

    lmfit <- lm(  ) 

    以上赋值语句创建了一个名为lmfit的列表对象，其中包含了分析的大量信息（包括预测值、 残差、回归系数等）。

    键入summary(lmfit)将显示分析结果的统计概要，plot(lmfit)将生成回归诊断图形， 而语句cook<-cooks.distance(lmfit)将计算和保存影响度量统计量，plot(cook)对其绘 图。

    ## Chapter 2 创建数据集

    1. 数据结构

       * 向量

         向量是用于存储数值型、字符型或逻辑型数据的一维数组。执行组合功能的函数c()可用来创建向量。

         注：单个向量中的数据必须 拥有相同的类型或模式（数值型、字符型或逻辑型）。同一向量中无法混杂不同模式的数据。

         通过在方括号中给定元素所处位置的数值，可以访问向量中的元素。例如，a[c(2, 4)] 用于访问向量a中的第二个和第四个元素。

         最后一个语句中使用的冒号用于生成一个数值序列。例如，a <- c(2:6)等价于a <- c(2,  3, 4, 5, 6)。

       * 矩阵

         可通过函数matrix()创建矩阵。一般使用格式为： 

         *myymatrix*<-matrix(*vector*,nrow=*number_of_rows*,ncol=*number_of_columns*,byrow=*logical_value*,dimnames=list(char_vector_rownames*,char_vector_colnames*))  

         其中*vector*包含了矩阵的元素，nrow和ncol用以指定行和列的维数，dimnames包含了可选 的、以字符型向量表示的行名和列名。选项byrow则表明矩阵应当按行填充（byrow=TRUE）还是按列填充（byrow=FALSE），默认情况下按列填充。

         注：单个矩阵中的数据必须 拥有相同的类型或模式（数值型、字符型或逻辑型）。

         X[i,]指矩阵X中的第*i*行，X[,j] 指第*j*列，X[i, j]指第*i*行第*j* 个元素。选择多行或多列时，下标*i*和*j*可为数值型向量。

       * 数组

         数组（array）与矩阵类似，但是维度可以大于2。数组可通过array函数创建，形式如下： 

         myarray <- array(*vector*, *dimensions*, *dimnames*)  

         其中*vector*包含了数组中的数据，*dimensions*是一个数值型向量，给出了各个维度下标的最大 值，而*dimnames*是可选的、各维度名称标签的列表。

       * 数据框

         数据框中不同的列可以包含不同模式（数值型、字符型等）的数据。但**每一列数据的模式必须唯一**。

         数据框可通过函数data.frame()创建： 

         mydata <- data.frame(*col1*, *col2*, *col3*,...)  

         其中的列向量*col1*、*col2*、*col3*等可为任何类型（如字符型、数值型或逻辑型）。每一列的名称可由函数names指定。

         可以联合使用函数attach()和detach()或单独使用函数with()来简化代码。[详见教材]

       * 因子

         变量可归结为名义型、有序型或连续型变量。名义型变量是没有顺序之分的类别 变量。有序型变量表示一种顺序关系，而非数量关系。连续型变量可以呈现为某个范围内的任意值，并同时表示了顺序和数量。

         **类别（名义型）变量**和**有序类别（有序型）变量**在R中称为因子（factor）。因子在R中非 常重要，因为它决定了数据的分析方式以及如何进行视觉呈现。

         函数factor()以一个整数向量的形式存储类别值，整数的取值范围是[1...*k*]（其中*k*是名义 型变量中唯一值的个数），同时一个由字符串（原始值）组成的内部向量将映射到这些整数上。

         要表示有序型变量，需要为函数factor()指定参数ordered=TRUE。

       * 列表

         列表就是一些对象（或成分，component）的有序集合。列表允许你整合若干（可能无关的）对象到单个对象名下。

    2. 数据输入

       * 使用键盘输入数据 

         有两种常见的方式：用R内置的文本编辑器和 直接在代码中嵌入数据。 

         R中的函数edit()会自动调用一个允许手动输入数据的文本编辑器。具体步骤如下： 

         (1) 创建一个空数据框（或矩阵），其中变量名和变量的模式需与理想中的最终数据集一致； 

         (2) 针对这个数据对象调用文本编辑器，输入你的数据，并将结果保存回此数据对象中。

         也可以直接在你的程序中嵌入数据集。比如说，参见以下代码： 

         mydatatxt <- "  

         age gender weight  

         25 m 166  

         30 f 115  

         18 f 120  

         "  

         mydata <- read.table(header=TRUE, text=mydatatxt)  

         一个字符型变量被创建于存 储原始数据，然后read.table()函数被用于处理字符串并返回数据框。

       * 从带分隔符的文本文件导入数据 

         可以使用read.table()从**带分隔符**的文本文件中导入数据。此函数可读入一个表格格式 的文件并将其保存为一个数据框。表格的每一行分别出现在文件中每一行。其语法如下： *mydataframe* <- read.table(*file*, *options*)  

         其中，*file*是一个带分隔符的ASCII文本文件，*options*是控制如何处理数据的选项。

       * 导入 Excel 数据 

         在Excel中将其导出为一个逗号分隔文件（csv），并使用前文描述的方式将其导入R中。

         此外，可以用xlsx包直接地导入Excel工作表。同时也需要xlsxjars和rJava包，以及一个正常工作的Java 安装（http://java.com）

       * 导入 XML 数据

       * 从网页抓取数据

       * 导入 SPSS 数据 

         IBM SPSS数据集可以通过foreign包中的函数read.spss()导入到R中，也可以使用Hmisc 包中的spss.get()函数。

       * 导入 SAS 数据 

         R中设计了若干用来导入SAS数据集的函数，包括foreign包中的read.ssd()，Hmisc包中 的sas.get()，以及sas7bdat包中的 read.sas7bdat()。如果安装了SAS，sas.get()是 一个好的选择。

       * 导入 Stata 数据

       * 导入 NetCDF 数据
       * 导入 HDF5 数据
       * 访问数据库管理系统
       * 通过 Stat/Transfer 导入数据

    3. 数据集的标注

       * 变量标签 

         一种方法是将变量标签作为变量名，然后通过位置下标来访问这个变量。

       * 值标签

         函数factor()可为类别型变量创建值标签。这里levels代表变量的实际值，而labels表示包含了理想值标签的字符型向量。

    4. 处理数据对象的实用函数

       <img src="C:/Users/shirl/AppData/Roaming/Typora/typora-user-images/image-20191029170346391.png" alt="image-20191029170346391" style="zoom:67%;" />

       <img src="C:/Users/shirl/AppData/Roaming/Typora/typora-user-images/image-20191029170549922.png" alt="image-20191029170549922" style="zoom:67%;" />

    

    

    

    



