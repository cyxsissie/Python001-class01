# 转换器 用于自定义匹配规则

class IntConverter:
    regex = '[0-9]+'  # 匹配的正则方式

    # 化成数字，给python 处理
    # 再转成字符串，给网址进行合并

    def to_python(self,value):
        return int(value)

    def to_url(self,value):
        return str(value)

class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self,value):
        return int(value)

    def to_url(self,value):
        return '%04d' %value