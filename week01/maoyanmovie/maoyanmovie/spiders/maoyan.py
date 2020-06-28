# -*- coding: utf-8 -*-
import scrapy
from maoyanmovie.items import MaoyanmovieItem
from scrapy.selector import Selector

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url = url, callable = self.parse, dont_filter=False)

    def parse(self,response):
        #基准的xpath
        movies = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd')                                                 
        #for循环依次遍历
        for rank in range(10):
            #创建对象'
            item = MaoyanmovieItem()
            # 电影名称
            item['movie_name'] = movies[rank].xpath("./div[1]/div[2]/a/div/div[1]/span[1]/text()").extract_first().strip()   
            # 电影类型
            item['movie_type'] = movies[rank].xpath("./div[1]/div[2]/a/div/div[2]/text()").extract_first().strip()
            #上映时间
            item['movie_time'] = movies[rank].xpath('./div[1]/div[2]/a/div/div[4]/text()').extract_first().strip()
            #把爬取的数据交给管道文件pipeline处理
            yield item    