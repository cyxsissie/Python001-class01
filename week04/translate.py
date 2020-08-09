# -*- coding:utf-8 -*-
import pandas as pd 

'''
这里的df_data 就是data表所有数据，保存在一个Dataframe中

例如：df_data = pd.DataFrame({'id': [1, 2, 3, 4, 5],
                     'name': ['lili', 'xixi', 'xiao', 'yun','fang'],
                     'age': [20, 25, 30, 35, 40]})

这里的df_table1 就是table1表所有数据，保存在一个Dataframe中

这里的df_table2 就是table2表所有数据，保存在一个Dataframe中
'''

# SELECT * FROM data;
df_data

# SELECT * FROM data LIMIT 10;
df_data.head(10)

# SELECT id FROM data;
# 两种写法                      
df_data[['id']]
# 或者
df_data.id # 会输出 Name: id, dtype: int64

# SELECT COUNT(id) FROM data;
len(df_data.id)

# SELECT * FROM data WHERE id<1000 AND age>30;
df_data[(df_data['id'] < 1000) & (df_data['age'] > 30)]

# SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
# 两种写法
df_table1.groupby('id').aggregate({'order_id': 'nunique'})
# 或者
df_table1.groupby('id')['order_id'].nunique()

# SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
pd.merge(df_table1, df_table2, on='id')

# SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat([df_table1, df_table2]).drop_duplicates()

# DELETE FROM table1 WHERE id=10;
# 两种写法 
df_table1[[df_table1.id != 10]
# 或者
df_table1.drop(df_table1[df_table1.id != 10].index)

# ALTER TABLE table1 DROP COLUMN column_name;
df_table1.drop(['column_name'], axis=1)
