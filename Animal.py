#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'


class Animal(object):
    def __init__(self):
        super(Animal, self).__init__()
        self.animal_name = None
        self.animal_color = None
        self.animal_age = None
        self.animal_sex = None

    def set_name(self, name):
        self.animal_name = name

    def set_color(self, color):
        self.animal_color = color

    def set_age(self, age):
        self.animal_age = age

    def set_sex(self, sex):
        self.animal_sex = sex

    def animal_call(self, call):
        return call

    def animal_run(self, run):
        return run
