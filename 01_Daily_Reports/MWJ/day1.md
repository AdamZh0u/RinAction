开始学习R语言:
## 使用R语言和R的语法：
开始学习R语言:
## 使用R语言和R的语法：
### 1.包的管理：
* 什么是包？（能实现某方面需求的功能集合）
* 安装包：
       'install.packages("ggplot2")'
* 加载包：
       ‘library()'
* 查看当前已经安装的包：
        'installed.packages()'
### 2.R的语法
* （1)变量赋值
    ' a<-10'' b<-'good'' ' f<-c(1,2,3')
    c()函数能把多个元素组合在一起
* （2）运算
        + - * / 加减乘除
        ^ 求幂 （python**）
        %%求余数（pyhon %)
        %/% 整除 （python //)
        & 和
        |  或
        ！=非
    
* （3）控制结构
        >if else {if(条件1）
                     xxx
                   elseif(条件2）
                     yyy
                   else
                   zzz
                   }  (python elif,and if...))
                   
        > while while(条件）{
                     xxx
                     }
        >for   for(i in x){
                   xxx
                   }
                   '''for (i in 1:10)print("hi")'''
* （4）访问数据
                 a<-c(10,20,30,40)
                 a[1]  10
                 a[2]  20
                 a[c(1,4)] 10,40
                 (python 中index从0开始
                 a=[10,20,30,40]
                 a[0] 10
                 a[1] 20
                 a[0,3] 10,40
                 a[0:3] 10,20,30,40