# -*-coding:utf-8 -*-
'''
桥接模式
'''

from abc import ABCMeta, abstractmethod


class AbstractClass(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def operation(self):
        pass


class AbstractImp(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def operation_imp(self):
        pass


class ATestImplementor(AbstractClass):
    def __init__(self, name):
        AbstractClass.__init__()
        self._name = name

    def operation(self, name, data):
        self._name = name
        print '{} operate {}'.format(self._name, data)


class BTestImplementor(AbstractClass):
    def __init__(self, name):
        AbstractClass.__init__()
        self._name = name

    def operation(self, name, data):
        self._name = name
        print '{} operate {}'.format(self._name, data)


class Implementor(AbstractImp):
    pass





