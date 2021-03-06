# 本周作业内容

探测目标主机是否开放了指定端口（1-1024）

**要求：编写一个基于多进程或多线程模型的主机扫描器。**

1. 使用扫描器可以基于 ping 命令快速检测一个 IP 段是否可以 ping 通，如果可以 ping 通返回主机 IP，如果无法 ping 通忽略连接。
2. 使用扫描器可以快速检测一个指定 IP 地址开放了哪些 tcp 端口，并在终端显示该主机全部开放的端口。
3. IP 地址、使用 ping 或者使用 tcp 检测功能、以及并发数量，由命令行参数传入。
4. 需考虑网络异常、超时等问题，增加必要的异常处理。
5. 因网络情况复杂，避免造成网络拥堵，需支持用户指定并发数量。

**命令行参数举例如下：**
`pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100`

`pmap.py -n 10 -f tcp -ip 192.168.0.1 -w result.json`

**说明：**

1. 因大家学习的操作系统版本不同，建立 tcp 连接的工具不限，可以使用 telnet、nc 或 Python 自带的 socket 套接字。
2. -n：指定并发数量。
3. -f ping：进行 ping 测试
4. -f tcp：进行 tcp 端口开放、关闭测试。
5. -ip：连续 IP 地址支持 192.168.0.1-192.168.0.100 写法。
6. -w：扫描结果进行保存。

**选做：**

1. 通过参数 [-m proc|thread] 指定扫描器使用多进程或多线程模型。
2. 增加 -v 参数打印扫描器运行耗时 (用于优化代码)。
3. 扫描结果显示在终端，并使用 json 格式保存至文件。

# 学习笔记

## 学习重点难点

+ 异常处理
+ concurrent.futures；
+ argparse: 命令行选项、参数和子命令解析器

### 本周踩的坑

+ 运行文件不能和引用的包文件同名：ImportError: cannot import name 'webdriver' from 'selenium'
+ webdriver驱动的存放路径，要开启权限

### 本周心得

+ 关于随机代理的视频看了2遍，作业用时比较长，主要是一开始对xpath找的定位的方面比较弱，后来经助教的指点，又查看了文档学习，终于顺利完成了作业，也对使用加深了印象；
+ 对于mysql输入语句结束要加分号完全记住了，由于自己工作中对库的创建都是可视化操作，所以在小组同学抛出问题时，只是觉得语句没问题，完全没发现是未加结束；的问题，这点对自己以后也是一个提醒；
+ scrapy过程中记录日志，是我在听分享可学到的，在实操过程中又结合文档，在项目中加入errback判断+记录错误回调并配置了生成日志的路径；
+ 举一反三，模仿中间件内获取setting文件内的配置项，将pipelines文件内用到的mysql参数，配置到了setting，并获取
+ 尽量做到面向对象的编程方式，调用类的方法本周作业内容：
  作业一：
  为scrapy 增加代理ip功能；
  将保存至csv文件的功能修改成保持到mysql，并下载部分增加异常捕获和处理机制；（代理IP可用GitHub的IP库）
  作业二：
  使用requests或selenium 模拟登录石墨文档 https://shimo.im
