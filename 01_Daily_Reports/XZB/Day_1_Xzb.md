By Xuz

---

# Day 1

## 词云的生成

```R
library(wordcloud2)
wordcloud2(data=demoFreq, size=1.6)
write.table(demoFreq,"Demo1.csv",sep=",")
demo<-read.table("Demo1.csv",sep=',')
wordcloud2(data=demo,size=1.6)
```

使用的包：wordcloud2

词云结果：

![image-20191029172637983](Day_1_Xzb.assets/image-20191029172637983.png)



## 第二章小结

主要数据结构

1. 向量
2. 矩阵
3. 数组
4. 数据框
5. 因子
6. 列表

数据的输入方式

1. 键盘
2. 带分隔符的文本文件
3. Excel文件
4. XML文件
5. 网页抓取
6. SPSS导入
7. SAS数据集
8. Stata数据
9. NetCDF数据
10. HDF5数据
11. 数据库的访问
12. Stat/Transfer

数据集的标注

+ 变量标注
+ 值标签



