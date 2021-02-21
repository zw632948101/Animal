#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'

from Animal import Animal


class Cat(Animal):
    def __init__(self):
        super(Cat, self).__init__()
        self.cat_varieties = None
        self.cat_hair = None

    def set_varieties(self, verietise):
        self.cat_varieties = verietise

    def set_hair(self, hair):
        self.cat_hair = hair

    def animal_call(self, call=None):
        return f'{self.cat_varieties}{self.animal_name}{call}喵喵叫;'

    def catching_mice(self, cathingMice=None, value=None):
        return f'捉{cathingMice}老鼠{value}'

    def cat_introduce(self):
        introduce = f'猫的属性：\n品种：{self.cat_varieties}\n名字：{self.animal_name}\n' \
                    f'毛发：{self.cat_hair}\n颜色：{self.animal_color}\n年龄:{self.animal_age}岁\n' \
                    f'性别：{self.animal_sex}'
        return introduce

    def cat_catching_mice(self, cathingMice=None, value_=None):
        catching = f'{self.cat_hair}{self.cat_varieties}{self.animal_name}{self.catching_mice(cathingMice,value_)};'
        return catching
