# 基本数据管理

- leadership数据库
  - 组合，生成平均得分：创建新变量-组合transform( )

  - 不完整数据：赋值为NA   选择dataframe里面的某个变量中的不完整值指定为NA ，即

    variable[condition] <- expression

    i.e. `leadership$$age[leadership$age == 99] <- NA`

    ==先处理缺失值，即先将所有值赋值为NA，再进行重编码==

    使用na.omit( )删除包含NA的行

  - 挑选部分变量

    - 指定列：i.e. `newdata <- leadership[, c(6:10)]`

    - 指定变量名称：`subdata <- mydata[tablename]``

      i.e. `tabl`ename <- c("City","Pop","BuiltUpArea")

    - 剔除变量：i.e. `myvars <- names(leadership) %in% c("q3", "q4")`
      `newdata <- leadership[!myvars]`  

  - 重编码:   可用within( )函数将需重编码的多个变量放在一块进行处理

    - 重命名：

    `names(leadership)[2] <- "testDate"`

    ``names(leadership)[6:10] <- c("item1", "item2", "item3", "item4", "item5")`

    可用plyr包里的rename( )函数：

    `rename(dataframe, c(oldname="newname", oldname="newname",...))`

  - 限定某一特定时间段（日期值）：as.Date(x, "input_format")

    i.e.

    `leadership$date <- as.Date(leadership$date, "%m/%d/%y")`
    `startdate <- as.Date("2009-01-01")`
    `enddate <- as.Date("2009-10-31")`
    `newdata <- leadership[which(leadership$data>=startdata&`

    `leadership$date <= enddate),]`

    ----

    

  - 类型转换
    - 判断 `is. numeric/character/vector/matrix/data. frame/factor/logical( )`
    - 转换 `as. numeric/character/vector/matrix/data. frame/factor/logical( )`

  - 数据排序：order ( )

  ​        i.e. `Mainfactor <- Mainfactor[order(Mainfactor$exponent),]#按照某列数据升序排列`

  - 合并
    - 按照ID进行合并：`total <- merge(dataframeA, dataframeB, by="ID")`
    - 横向合并`cbind( )`
    - 添加行：`rbind( )`

  - subset( )函数

    `newdata <- subset(leadership, age >= 35 | age < 24,`
    `select=c(q1, q2, q3, q4))`  #选择所有age值大于等于35或age值小于24的行，保留了变量q1到q4

    ``newdata <- subset(leadership, gender=="M" & age > 25,select=gender:q4)`#选择所有25岁以上的男性，并保留了变量gender到q4（gender、q4和其间所有列）

