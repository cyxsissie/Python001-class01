# 学习笔记

作业地址：http://127.0.0.1:8000/index

## 本周作业

使用 Django 展示豆瓣电影中某个电影的短评和星级等相关信息：

1. 要求使用 MySQL 存储短评内容（至少 20 条）以及短评所对应的星级；
2. 展示高于 3 星级（不包括 3 星级）的短评内容和它对应的星级；
3. （选做）在 Web 界面增加搜索框，根据搜索的关键字展示相关的短评。

## 本周主要学习内容如下：

### 一、Django：python编写的开源web框架

MTV框架：模型models，模板template，视图views

Django特点：
使用MTV框架，可快速开发和代码复用，有丰富组件：包括ORM，url正则，可继承模板，权限模块，admin管理，表单模型，缓存，国际化等
**安装Django：
pip install --upgrade django==版本号**
django使用：

1. 创建项目和目录结构
   django-admin startproject 项目名
   目录结构如下：

```
项目名/
项目名/manage.py               命令行工具，管理工程
项目名/项目名/
项目名/项目名/__init__.py
项目名/项目名/settings.py      工程配置文件（数据库配置等）
项目名/项目名/urls.py
项目名/项目名/wsgi.py
```

2. 创建django应用程序

```
python manage.py help          查看该工具的具体功能
python manage.py startapp index
index/migrations               数据库迁移文件夹
index/models.py                模型
index/apps.py                  当前app配置文件
index/admin.py                 管理后台
index/tests.py                 自动化测试
index/views.py                 视图
```

3. ###### 编写代码启动服务


   运行：python manage.py runserver
   ip:端口(默认127.0.0.1:8000)
4. django配置文件 -- settings.py
5. 结构说明
   配置包括：项目路径、秘钥、域名访问权限、App列表、静态资源(css,js,图片)、静态模板、数据库配置、缓存、中间件等

### 二、url调度器（urlconf）：django如何处理一个请求~~~~

当一个用户请求django站点的一个页面：

1. 如果传入HttpRequest对象拥有urlconf属性(通过中间件设置)，它的值将被用来代替ROOT_URLCONF设置；
2. django加载URLconf模块并寻找可用的urlpatterns，django依次匹配每个URL模式，在与请求的URL匹配的第一个模式停下来；
3. 一旦有URL匹配成功，django导入并调用相关视图，视图会获得如下参数：

* 一个HttpRequest实例
* 一个或多个位置参数提供

4. 如果没有URL被匹配，或者匹配过程中出现异常，django会调用一个适当的错误处理视图；
   逻辑代码在项目下urls.py：

```python
from django.contrib import admin
from django.urls import path,include
# include可以引入其他urls.py文件进行匹配，如下，如果访问的url是''，就继续进入引入名为index的app下的urls.py进行进一步匹配
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls'))
]
```

找到index项目下的urls.py，继续根据urlpatterns做匹配，其中匹配的路径为views.index，说明是匹配views.py中index函数

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]
```

index项目下的views.py文件

```python
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello Django!")
```

5. url支持变量：
   django支持对url设置变量，url变量类型包括：
   str、int、slug、uuid、path path('int:year',views.myyear) 例：

```python
from django.urls import path, register_converter
from . import views, converters

urlpatterns = [
    path('', views.index),

    ### 带变量的URL
    # path('<int:year>', views.year),  # 只接收整数，其他类型返回404
    path('<int:year>/<str:name>', views.name),

    ### 自定义过滤器
    path('<yyyy:year>', views.year), 

]

views.py:

from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Django!")

# path('<int:year>', views.year), 
def year(request, year):
    # return HttpResponse(year)
    return redirect('/2020.html')

# path('<int:year>/<str:name>', views.name),
def name(request, **kwargs):
    return HttpResponse(kwargs['name'])
```

6. url正则和自定义过滤器
   可以用正则表达式对传入参数判断：
   原来的path改为re_path

```python
urls.py:
from django.urls import path, re_path, register_converter
from . import views, converters

urlpatterns = [
    path('', views.index),

    ### 正则匹配
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),

]

views.py:
# path('<myint:year>', views.year), 
# re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),
def myyear(request, year):
    return render(request, 'yearview.html')
```

自定义匹配规则：

```python
from django.urls import path, register_converter
from . import views, converters

register_converter(converters.IntConverter,'myint')
register_converter(converters.FourDigitYearConverter, 'yyyy')

### 自定义过滤器
    path('<yyyy:year>', views.year), 

class IntConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)

class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value
```

##### 三、view视图：

响应分为两种：response，render，render是response的进一步封装；


| 响应类型 | 说明 |
| - | - |
| HttpResponse('') | http状态200，请求已经成功被服务器接收 |
| HttpResponseRedirect('/admin/') | http状态302，重定向到Admin站点 |
| HttpResponsePermanentRedirect('/admin/') | http状态301，永久定向到Admin站点 |
| HttpResponseBadRequest('BadRequest') | http状态400，访问的页面不存在或者请求出问题 |
| HttpResponseNotFound('NotFound') | http状态400，访问的页面不存在或者网页url失效 |
| HttpResponseForbidden('NotFound') | http状态403，没有权限访问 |
| HttpResponseNotAllowed('NotAllowedGet') | http状态405，不允许使用该请求方式 |
| HttpResponseSeverError('SeverError') | http状态500，服务器异常 |

django快捷函数：

* render():将给定模板与给定上下文字典组合在一起，并以渲染的文本返回一个HttpResponse对象；
* redirect():将一个HttpResponseRedirect返回到传递的参数的适当url；
* get_object_or_404():在给定的模型管理器上调用get(),但它会引发404错误，而不是模板类型的DoesNotExist异常；

##### 四、ORM相关：

模型：
每个模型都是一个python类，都继承自django.db.models.Model 模型类每个属性相当于数据库中对应表中对应字段

将python实体转换为一张表
python manage.py makemigrations
会转化为中间python脚本
python manage.py migrate
再将中间python脚本转化为sql

创建model：

```python
from django.db import models

# 图书or电影
class Type(models.Model):
    # id = models.AutoField(primary_key=True) #django会自动创建主键
    typename = models.CharField(max_length=20)

# 作品名称和作者、主演
class Name(models.Model):
    # id自动创建
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    stars = models.CharField(max_length=10)
```

配置mysql客户端：
在项目同名目录下的__init__.py中添加配置：

```python
import pymysql
pymysql.install_as MySQLdb()

#如果仍然找不到mysql客户端，则需要linux配置mysql搜索路径：export PATH=$PATH:mysql客户端目录
```

ORM的API：
使用django的manage.py的shell命令可以对表进行CRUD操作：

```python
数据表的读写
$ python manage.py  shell
>>> from index.models import *
>>> n = Name()
>>> n.name='红楼梦'
>>> n.author='曹雪芹'
>>> n.stars=9.6
>>> n.save()

使用ORM框架api实现
增
>>> from index.models import *
>>> Name.objects.create(name='红楼梦', author='曹雪芹', stars='9.6')
>>> Name.objects.create(name='活着', author='余华', stars='9.4')

查
>>> Name.objects.get(id=2).name

改
>>> Name.objects.filter(name='红楼梦').update(name='石头记')

删 
单条数据
>>> Name.objects.filter(name='红楼梦').delete()
全部数据
>>> Name.objects.all().delete()

其他常用查询
>>> Name.objects.create(name='红楼梦', author='曹雪芹', stars='9.6')
>>> Name.objects.create(name='活着', author='余华', stars='9.4')
>>> Name.objects.all()[0].name
>>> n = Name.objects.all()
>>> n[0].name
>>> n[1].name

>>> Name.objects.values_list('name')
<QuerySet [('红楼梦',), ('活着',)]>
>>> Name.objects.values_list('name')[0]
('红楼梦’,)
filter支持更多查询条件
filter(name=xxx, id=yyy)

可以引入python的函数
>>> Name.objects.values_list('name').count()
2
```

##### 五、Django模板：

模板可以将前端相关文件，如html，js，css整合在一起成为网页内容作为响应；
常用：
模板变量 {{variables}}
从url获取模板变量 {% url 'urlyear' 2020 %}:会找到urls.py中匹配urlyear的路径
如：

```python
urls.py:
urlpatterns = [
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),
    ...
]
```

读取静态资源 {% static "css/XXX.css" %}
for 遍历标签 {% for type in type_list %}{% endfor %}
if 判断标签{% if name.type==type.type %}{% endif %}

##### 六、urlconf与models

针对不同业务，有时候为了避免无关联业务功能耦合在一起，这时候需要对urlconf设置，对业务解耦，需要新建不同app；
比如douban项目中有两个功能的url：

```
http://ip/xxx
http://ip/yyy
通过设置可以改为：
http://ip/douban/xxx
http://ip/douban/yyy
```

需要设置如下
settings.py：

```python
INSTALLED_APPS = [
    ####  内置的后台管理系统
    'django.contrib.admin',
    ####  内置的用户认证系统
    'django.contrib.auth',
    #### 所有model元数据
    'django.contrib.contenttypes',
    #### 会话，表示当前访问网站的用户身份
    'django.contrib.sessions',
    #### 消息提示
    'django.contrib.messages',
    #### 静态资源路径
    'django.contrib.staticfiles',
    #### 注册自己的APP
    'index',
    'douban'
]
```

启动:python manage.py startproject douban
项目MyDjango根目录下urls.py:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('index.urls')),
    path('douban/',include('Douban.urls')),
]
```

app下urls.py:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.books_short),
]
```

如果表已存在，并且有数据，只需要做查找数据可以反向创建model
根据db反向创建model命令：
python manage.py inspectdb > models.py
生成的models:

```python
from django.db import models

class T1(models.Model):
    id = models.BigAutoField(primary_key=True)
    n_star = models.IntegerField()
    short = models.CharField(max_length=400)
    sentiment = models.FloatField()

    # 元数据，不属于任何一个字段的数据
    class Meta:
        managed = False
        db_table = 't1'
```

path('index', views.books_short)中对应视图views.books_short配置:
根据from . import views，会在当前目录下的views.py查找
views.py 通过已经创建的model，利用ORM查找对应表数据用来响应：

```python
from django.shortcuts import render

# Create your views here.
from .models import T1
from django.db.models import Avg

def books_short(request):
    ###  从models取数据传给template QuerySet对象 ###
    shorts = T1.objects.all()
    # 评论数量
    counter = T1.objects.all().count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg =f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "
    # 情感倾向
    sent_avg =f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    # 正向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())
```

##### 七、其他：模块和包，以及django源码相关：

模块：.py结尾的python程序
包：存放多个模块的目录
**init**.py:包运行初始化文件，可以使空文件
常见几种方式导入：

```
import
from import
from import as
```

包运行初始化文件__init__.py，在包被引入时，会优先执行；
如果同一个包内，py文件引入，可以使用from . import 被引入py文件，from . 表示从当前目录开始查找；

django源码：

1. 针对功能;2、针对某个元素;
   需要习惯使用if '**name**' == '**main**'
   使用python manage.py runserver 8080时，底层manage.py做了5件事：

* 1、解析runserver以及后面参数
* 2、加载runserver文件
* 3、检查配置项，settings，INSTALL_APPS，ip端口是否占用，ORM框架
* 4、实例化WSGIserver接收http请求
* 5、动态创建一些类

manage.py:

```python
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    # 加载环境变量和配置
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyDjango.settings')
    # 导入命令行
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```

django.core.management：

```python
def execute_from_command_line(argv=None):
    """Run a ManagementUtility."""
    utility = ManagementUtility(argv)
    utility.execute()
```

初始化，解析传来的命令字符串，读取django配置，执行命令行，导入模块，实例化服务（执行ORM相关，加载WSGI配置等）
