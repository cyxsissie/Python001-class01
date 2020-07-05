# 本周作业内容：
作业一：
    为scrapy 增加代理ip功能；
    将保存至csv文件的功能修改成保持到mysql，并下载部分增加异常捕获和处理机制；（代理IP可用GitHub的IP库）
作业二：
    使用requests或selenium 模拟登录石墨文档 https://shimo.im

 # 学习笔记   
 ## 补上周的为掌握好的知识点
 根据本周四群分享的内容，加深对scrapy的创建和运行命令，找到了上周为何运行项目失败的原因
    搭建步骤：
    scrapy startproject movies work1
    cd work1 
    scrapy genspider maoyan maoyan.com
    运行：
    cd work1/movies/spiders
    scrapy crawl maoyan
## 本周笔记
###  学习重点难点
+ 异常处理
+ 中间件内设置代理IP的流程；在github上找到一个提供IP库的地址；也有通过接口获取IP地址，感觉工作中通过接口获取比较常见；
+ 熟悉了webdriver的便捷

### 本周踩的坑
+ 运行文件不能和引用的包文件同名：ImportError: cannot import name 'webdriver' from 'selenium'
+ webdriver驱动的存放路径，要开启权限
### 本周心得
+ 关于随机代理的视频看了2遍，作业用时比较长，主要是一开始对xpath找的定位的方面比较弱，后来经助教的指点，又查看了文档学习，终于顺利完成了作业，也对使用加深了印象；
+ 对于mysql输入语句结束要加分号完全记住了，由于自己工作中对库的创建都是可视化操作，所以在小组同学抛出问题时，只是觉得语句没问题，完全没发现是未加结束；的问题，这点对自己以后也是一个提醒；
+ scrapy过程中记录日志，是我在听分享可学到的，在实操过程中又结合文档，在项目中加入errback判断+记录错误回调并配置了生成日志的路径；
+ 举一反三，模仿中间件内获取setting文件内的配置项，将pipelines文件内用到的mysql参数，配置到了setting，并获取
+ 尽量做到面向对象的编程方式，调用类的方法

