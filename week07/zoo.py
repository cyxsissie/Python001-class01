# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

#  使用抽象基类
class Animal(metaclass=ABCMeta):
    # 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性
    @abstractmethod
    def __init__(self, name, types, size, is_fierce):
        self.name = name
        self.types = types
        self.size = size
        self.is_fierce = is_fierce

    # 控制属性
    # 是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
    @property
    def is_fierce_animal(self):
        return True if self.size != '小型' and self.types == '食肉' and self.is_fierce == '凶猛' else False

class Cat(Animal):
    # 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，猫类继承自动物类
    as_pet = True
    def __init__(self, name, types, size, is_fierce):
        self.name = name
        super().__init__(name, types, size, is_fierce)
        
    @classmethod
    def sound(cls):
        sounds = '喵～～～'
        return f"{cls.__name__} 的叫声是 {sounds}."
    
    def fit_for_pet(self):     
        if super().is_fierce_animal:
            return "不适合作为宠物"
        else:
            return "适合作为宠物"
    
class Zoo:
    # 动物园类要求有“名字”属性和“添加动物”的方法，
    # “添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
    def __init__(self, name):
        self.name = name
        # 将动物园的动物作为似有属性统计
        self.__animals = set()

    def add_animal(self, animal):
        if animal not in self.__animals:
            self.__animals.add(animal)
            return True
        return False

    def __getattr__(self, item):
        return any(i.__class__.__name__ == item for i in self.__animals)


if __name__ == '__main__':
    # 动物类不允许被实例化
    try:
        Animal('猫', '食肉', '小型', '温顺')
    except TypeError as e:
        print(f"Animal不能被实例化")
    # 猫的叫声，是否可以作为宠物
    cat = Cat('老虎', '食肉', '大型', '凶猛')
    print(f"\n{cat.sound()}")
    print(f"\n{cat.name} {cat.fit_for_pet()}")
    cat = Cat('英短猫', '食肉', '小型', '温顺')
    print(f"\n{cat.sound()}")
    print(f"\n{cat.name} {cat.fit_for_pet()}")
    # 添加动物   
    z = Zoo('时间动物园')
    z.add_animal(cat)
    print(f"\n动物园是否有猫这类动物: {getattr(z, 'Cat')}")
    print(f"动物园是否有狗这类动物: {getattr(z, 'Dog')}")