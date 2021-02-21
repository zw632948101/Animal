#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
import random

__author__ = 'wei.zhang'
from Cat import Cat


class CatWold(Cat):
    def __init__(self, name='', age='', color='', sex='', hair='', verietise='', call='',
                 cathingMice='', value_=''):
        super(CatWold, self).__init__()
        self.name = name
        self.age = age
        self.color = color
        self.sex = sex
        self.hair = hair
        self.verietise = verietise
        self.call = call
        self.cathingMice = cathingMice
        self.value = value_
        self.init_attribute()

    def init_attribute(self):
        name = ['果冻', '布丁', '雪球', '奶搪', '双双', '布什', '白虎', '威风', '帅哥', '玛雅', '壮壮', '多多', '阿虎', '小凡', '小宝', '小雪', '逗逗',
                '笑笑', '佳佳', '点点', '安安', '苹果', '玫瑰', '百合', '草莓', '绿茶', '橙子', '果汁', '小小', '小银', '小卒', '小刺猬', '小芸', '天狼']
        age = [i for i in range(1, 15)]
        color = ['黄', '黑', '白', '灰', '蓝']
        sex = ['公猫', '母猫']
        hair = ['长毛', '短毛']
        verietise = ['布偶猫', '金吉拉', '山东狮子猫', '缅因猫', '挪威纳猫', '波斯猫']
        self.verietise = self.verietise if self.verietise else random.choice(verietise)
        self.name = self.name if self.name else random.choice(name)
        self.age = self.age if self.age else random.choice(age)
        self.color = self.color if self.color else random.choice(color)
        self.sex = self.sex if self.sex else random.choice(sex)
        self.hair = self.hair if self.hair else random.choice(hair)

        self.set_name(self.name)
        self.set_age(self.age)
        self.set_color(self.color)
        self.set_sex(self.sex)
        self.set_hair(self.hair)
        self.set_varieties(self.verietise)
        print(self.cat_introduce())
        print(self.animal_call(self.call))
        print(self.cat_catching_mice(cathingMice=self.cathingMice, value_=self.value))


if __name__ == '__main__':
    cat = CatWold()
