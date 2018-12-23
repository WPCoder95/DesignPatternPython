# -*-coding:utf-8 -*-


# python Singleton的经典实现方式
# 返回固定的类
class Singleton(object):
    # python内部用于实例化对象的方法
    # 通过重写__new__方法来控制队形的生成
    def __new__(cls):
        # python对象的特殊方法,用来了解对象是否具有某个属性
        # 若类已有实例对象,则instance属性就会存在
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


def singleton_test():
    s = Singleton()
    print s
    s1 = Singleton()
    print s1


# python Singleton的懒汉实现方式
class Singleton2(object):
    __instance = None

    def __init__(self):
        if not Singleton2.__instance:
            print ' __init__ method called.'
        else:
            print 'instance already created: ', self.getInstance()

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton2()
        return cls.__instance


def singleton2_test():
    # class initialized
    sa = Singleton2()
    # object created here
    print ('Object created :', sa.getInstance())
    print sa
    sb = Singleton2()
    print sb


# Monostate模式
class Borg1:
    __share_state = {'1': '4'}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__share_state
        pass


def borg1_test():
    a = Borg1()
    b = Borg1()
    a.x = 5
    print ('Borg1 object "a": ', a)
    print ('Borg1 object "b": ', b)
    print ('Object state "a": ', a.__dict__)
    print ('Object state "b": ', b.__dict__)


class Borg(object):
    __share_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__share_state
        return obj


def borg_test():
    a = Borg()
    b = Borg()
    a.x = 5
    print ('Borg1 object "a": ', a)
    print ('Borg1 object "b": ', b)
    print ('Object state "a": ', a.__dict__)
    print ('Object state "b": ', b.__dict__)


# 使用元类生成单例
# python类的定义由它的元类来决定
# A = type(name, base, dict)
# name: 类的名字
# base: 基类
# dict: 创建类所用的字典
# 如果一个类有一个预定义的元类 python会通过元类来创建类
# 本实例定义了元单例类,只要在要生成的单例类中声明__metaclass__为MetaSingleton类,即可生成单例类
class MetaSingleton(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__( *args, **kwargs)
        return cls._instance[cls]


class Logger:
    # 使用元类生成单例
    __metaclass__ = MetaSingleton
    pass

def metaclass_test():
    a = Logger()
    b = Logger()
    # a和b的地址相同
    print a, b, a==b


# 使用单例进行数据库连接示例
# 保证数据库操作的一致性，以提高内存和cpu的使用率
import sqlite3
class Database:
    __metaclass__ = MetaSingleton
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db.sqlite3')
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

def database_test():
    db1 = Database().connect()
    db2 = Database().connect()
    print db1, db2, db1 == db2


# 单例的另外一个实例
class HealthCheck(object):
    # 此处为单例的经典写法
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        self.servers = []

    def addServer(self):
        for i in range(1, 4):
            print 'add server[{}] ... '.format(i)
            self.servers.append('server[{}]'.format(i))

    def changeServer(self):
        print 'changing health list ...'
        print 'delete last element.'
        print 'append X element.'
        self.servers.pop()
        self.servers.append('server[X]')

# HealthCheck类的测试函数
def health_check_test():
    hc1 = HealthCheck()
    hc2 = HealthCheck()
    print hc1, hc2, hc1 == hc2
    hc1.addServer()
    hc2.changeServer()
    print hc1.servers, hc2.servers
    print hc1, hc2, hc1 == hc2

if __name__ == '__main__':
    borg1_test()
    borg_test()
    metaclass_test()
    database_test()
    health_check_test()