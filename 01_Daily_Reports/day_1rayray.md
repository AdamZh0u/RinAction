- ### 词云

  instal..packages(wordcloud2)首先要安装词云的包（==R的packages很强大==，学习之余一定要多挖掘R有趣的包功能，这样才能让科研与生活变得多娇:happy:)
  
  - data：words % freq
  
  - size：字体大小，默认为1，一般来说该值越小，生成的形状轮廓越明显；
  
  - color：‘random-dark’ or "random-light’
  
  - backgroundColor：grey or black
  
  - minRontation, maxRontation 
  
  - rotationRation
  
  - shape: circle ...
  
    :thinking:为了让图变得好看，还得多试几次。

----

（==这个分界面太不明显了====狗头)

- #### R in action Section 1&2

  - packages 包的安装有两种，一个右下packages界面，点Install; 二是install.packages("rjava")  :high_brightness: =="==不能忘"

    个人认为第一种方法更好用，在packages界面还可以勾选已安装的包，可直接代替library( )操作

  - 数据结构

    - 向量：一般就是自己赋值，c( )进行创建

    - 数组:和矩阵类似，但维度可>2。由array( )创建  

      - 三个参数vector, dimensions, dimnames。

    - ==数据框==:dataframe

      先建一个dataframe，一般是将里面的要素设定为1；而后再新建一个data.frame将分析结果放入，再用rbind命令将两个data.frame合并，就可以导出了

    - 矩阵：mymatrix(data,nrow= ,nclo= )

      - 可对矩阵行列命名rnames( ); cnames( )                                                 :call_me_hand:6666
      - 可用下标及方括号选择行列：x[i,]表示x中的i行，[,j]表示j列。 

  - 导出导入数据

    - read.csv( )
    - write.csv( )

  - 绘图 

    plot( )               :call_me_hand:加强学习强大ggplot画图功能

    ----

    thinking:thinking:

    R还有很多很强大的空间分析与画图功能等待挖掘！

    词云这个任务，真是太为难我这个（伪）强迫症了--

    :star:

    

