### 3图形初阶

#### 3.1 使用图形

1. ``` R
   attach(mtcars)#绑定数据框
   plot(wt, mpg)#打开图形窗口生成散点图
   abline(lm(mpg-wt))#向图形添加一条最优拟合曲线
   title("Regression of MPG on Weight")#添加标题
   detach(mtcars)#解除绑定的数据框
   ```

2. 可以通过代码或图形用户界面来保存图形。

``` R
pdf("mygraph.pdf")
attach(mtcars)
plot(wt, mpg)
abline(lm(mpg~wt))
title("Regression of MPG on Weight")
detach(mtcars)
dev.off()
```

除了 *pdf*()，还可以使用函数*win.metafile*()、*png*()、*jpeg*()、*bmp*()、*tiff*()、*xfig*()和*postscript*()将图形保存为其他格式。

3. 创建多个图形且能随时查看每一个

``` R
dev.new()
statements to create graph 1
dev.new()
statements to create a graph 2
etc.
```

#### 3.2 例子

``` R
dose <- c(20, 30, 40, 45, 60)
drugA <- c(16, 20, 27, 40, 60)
drugB <- c(15, 18, 25, 31, 40)
plot(dose, drugA, type="b")#plot(x,y,type="b")绘制出药物A剂量和相应的折线图
```

![Example1](Example1.jpeg)

#### 3.3 图形参数

1. 通过修改称为图形参数的选项来自定义一幅图形的多个特征（字体、颜色、坐标轴、标签）

2. 符号&线条

| 参数 | 描述                   |
| :--- | ---------------------- |
| pch  | 指定绘制点时使用的符号 |
| lty  | 指定线条类型           |
| cex  | 指定符号大小           |
| lwd  | 指定线条宽度           |

3. 颜色

| 参数     | 描述                   |
| -------- | ---------------------- |
| col      | 默认的绘图颜色         |
| col.axis | 坐标轴刻度文字的颜色   |
| col.lab  | 坐标轴标签（名称）颜色 |
| col.main | 标题颜色               |
| col.sub  | 副标题颜色             |
| fg       | 图形前景色             |
| bg       | 图形背景色             |

4. 图形参数同样可以用来指定字号、字体和字样。在*Windows*系统中，等宽字体映射为*TT
   Courier New*，衬线字体映射为*TT Times New Roman*，无衬线字体则映射为*TT Arial*（TT代表*True
   Type*）。
5. *pin* 以英寸表示的图形尺寸（宽和高）
   *mai* 以数值向量表示的边界大小，顺序为“下、左、上、右”，单位为英寸
   *mar* 以数值向量表示的边界大小，顺序为“下、左、上、右”，单位为英分。

​       *cex* 表示相对于默认大小缩放倍数的数值。默认大小为1，1.5 表示放大为默认值的1.5 倍，0.5 表示缩小为默认值的50%。
​       *cex.axis* 坐标轴刻度文字的缩放倍数。
​       *cex.lab* 坐标轴标签（名称）的缩放倍数。
​       *cex.main* 标题的缩放倍数。
​       *cex.sub* 副标题的缩放倍数。

​       *font* 整数。用于指定绘图使用的字体样式。1=常规，2=粗体，3=斜体，4=粗斜体，5=符号字体
​       *font.axis* 坐标轴刻度文字的字体样式
​       *font.lab* 坐标轴标签（名称）的字体样式
​       *font.main* 标题的字体样式
​       *font.sub* 副标题的字体样式
​       *ps* 字体磅值（1 磅约为1/72 英寸）。文本的最终大小为ps*cex
​       *family* 绘制文本时使用的字体族。标准的取值为serif（衬线）、sans（无衬线）和mono（等宽)

6. 代码清单3-1

![Example2](Example2.jpeg)

![Example3](Example3.jpeg)

#### 3.4 添加文本、自定义坐标轴和图例

1. 可以使用*title*()函数为图形添加标题和坐标轴标签。
2. 使用函数*axis*()来创建自定义的坐标轴，而非使用R中的默认坐标轴。其格式为：
   *axis(side, at=, labels=, pos=, lty=, col=, las=, tck=, ...)*

​      *side* 一个整数，表示在图形的哪边绘制坐标轴（1=下，2=左，3=上，4=右）
​      *at*一个数值型向量，表示需要绘制刻度线的位置
​      *labels* 一个字符型向量，表示置于刻度线旁边的文字标签（如果为NULL，则将直接使用at 中的值）
​      *pos* 坐标轴线绘制位置的坐标（即与另一条坐标轴相交位置的值）
​     *lty* 线条类型
​     *col* 线条和刻度线颜色
​     *las* 标签是否平行于（=0）或垂直于（=2）坐标轴

​     *tck*刻度线长度

3. 函数*abline*()可以用来为图形添加参考线。函数*legend*()来添加图例。通过函数*text*()和*mtext*()将文本添加到图形上。*text*()可向绘图区域内部添加文本，而*mtext*()则向图形的四个边界之一添加文本。
4. 代码清单3-3  

![Example4](Example4.jpeg)

==如果图例占幅较大，可设置*cex*<1的值来进行调整==

#### 3.5图形的组合

1. 使用函数*par*()或*layout*()可以容易地组合多幅图形为一幅总括图形。
2. 函数*layout*()的调用形式为*layout(mat)*，其中的*mat*是一个矩阵，它指定了所要组合的
   多个图形的所在位置。

