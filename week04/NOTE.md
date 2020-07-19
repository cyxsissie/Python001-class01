# 学习笔记

## 本周作业

掌握基本的 SQL 语句和 pandas 等价的语句，利用 Python 的函数高效地做聚合等操作。

请将 SQL 语句翻译成 pandas 语句

## 本周重点

+ NumPy 拥有线性代数和随机数生成的内置函数（可用于生成测试数据）
+ Series 是 Pandas 提供的一种数据类型，可以把它想象成 Excel 的一行或一列

  ````
  import numpy as np
  import pandas as pd

  # 创建 Series，pandas 自动创建 index
  s = pd.Series([1, 3, 5, np.nan, 6, 8])
  print(s)
  ````
+ DataFrame 是 Pandas 提供的另一种数据类型，可以把它想象成 Excel 的表格

  ```
  import numpy as np
  import pandas as pd

  # 创建数据集
  data = np.random.randn(6, 4)

  # 创建 DataFrame
  df = pd.DataFrame(data)
  print(df)
  ```
+ Python中xlrd和xlwt模块使用方法

  + xlrd模块实现对excel文件内容读取，xlwt模块实现对excel文件的写入
    + 相关拓展文章：https://www.cnblogs.com/xiao-apple36/p/9603499.html
+ pandas中map() 和apply() 的区别

  + map()：针对pandas 中的DataFrame中列进行迭代操作
  + apply(): 针对pandas中DataFrame中行进行迭代操作
+ 数据绘图

  + plot 学习文档：[https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)
  + **seaborn 学习文档：**
    [http://seaborn.pydata.org/tutorial.html](http://seaborn.pydata.org/tutorial.html)
+ 数据分词/情感分析

  + jieba 学习文档：[https://github.com/fxsjy/jieba/blob/master/README.md](https://github.com/fxsjy/jieba/blob/master/README.md)
  + snowNLP 参考学习地址：[https://github.com/isnowfy/snownlp/blob/master/README.md](https://github.com/isnowfy/snownlp/blob/master/README.md)
