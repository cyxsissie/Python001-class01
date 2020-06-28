# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_time = item['movie_time']

        movie2 = pd.DataFrame(data = [movie_name,movie_type,movie_time], columns=['电影名称','电影类型','上映时间'])
        movie2.to_csv('./movie2.csv',mode = 'a', encoding='utf8',index=False)
        return item
