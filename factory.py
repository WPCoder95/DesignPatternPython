# -*- coding:utf-8 -*-
'''
三种工厂示例:
      1.简单工厂模式
      2.工厂模式
      3.抽象工厂模式
'''

#####################################################
# 简单工厂
from abc import ABCMeta, abstractmethod

# 动物的基类
class Animal(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def do_say(self):
        pass


class Cat(Animal):
    def do_say(self):
        print 'Meow, Meow'


class Dog(Animal):
    def do_say(self):
        print 'Won, Won'


# 简单工厂类, 根据传入的字符串来生成不同的对象, 并调用对象的方法
class ForestFactory(object):

    def make_sound(self, object_type):
        # 使用eval 根据字符串object_type生成具体的对象
        return eval(object_type)().do_say()


def simple_factory_test():
    ff = ForestFactory()
    # input在python2中如果要输入字符串,需使用'',如输入Cat,则为'Cat'
    animal = input('Which animal you want to create, Cat or Dog :')
    print animal
    ff.make_sound(animal)


###########################################################
# 工厂模式
class Section:
    __metaclass__ = ABCMeta

    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print 'PersonalSection'


class AlbumSection(Section):
    def describe(self):
        print 'AlbumSection'


class PatentSection(Section):
    def describe(self):
        print 'PatentSection'


class PublicSection(Section):
    def describe(self):
        print 'PublicSection'


class Profile:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSection(self):
        return self.sections

    def addSection(self, section):
        self.sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(PatentSection())
        self.addSection(PublicSection())


class facebook(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(AlbumSection())


def factory_test():
    profile_type = input("Which profile you'd like to create? [Lindedin or Facebook]")
    profile = eval(profile_type.lower())()
    print ('Create Profile ..', type(profile).__name__)
    print ('profile has section --', profile.getSection())

####################################################
# 抽象工厂方法示例
class VegPizza:
    __metaclass__ = ABCMeta

    @abstractmethod
    def prepare(self):
        pass


class NonVegPizza:
    __metaclass__ = ABCMeta

    @abstractmethod
    def serve(self, VegPizza):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print(' Prepare ', type(self).__name__)


class ChickenPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Chicken on ", type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Perpare ", type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Ham on", type(VegPizza).__name__)


class PizzaFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


class IndiaPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()


class PizzaStore:
    def __init__(self):
        pass

    def makePizzas(self):
        for factory in [IndiaPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


def abs_factory_test():
    pizza = PizzaStore()
    pizza.makePizzas()


if __name__ == '__main__':
    # simple_factory_test()
    # factory_test()
    abs_factory_test()
