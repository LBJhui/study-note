# _*_ coding: utf-8 _*_
# @Time: 2024/5/29 15:51
# @Author: LBJ辉
# @File: code11-8-多态
# @Project: nxops-01

class Animal(object):

    def speak(self):
        print('动物的叫声')
        pass


class Cat(Animal):

    def speak(self):
        print('喵喵')


class Dog(Animal):

    def speak(self):
        print('汪汪')


class Test(object):
    def speak(self):
        print('test')


def speak(object):  # animal
    object.speak()


animal = Animal()
kitty = Cat()
puppy = Dog()
t = Test()
speak(animal)
speak(kitty)
speak(puppy)
speak(t)
