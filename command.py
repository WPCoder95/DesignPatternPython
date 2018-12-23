# -*- coding:utf-8 -*-
'''
命令模式
'''

from abc import ABCMeta, abstractmethod


class Wizard(object):
    def __init__(self, src, rootdir):
        self.choice = []
        self.rootdir = rootdir
        self.src = src

    def preferences(self, command):
        self.choice.append(command)

    def execute(self):
        for choice in self.choice:
            if list(choice.values())[0]:
                print "Copy binaries --", self.src, " to", self.rootdir
            else:
                print "No Operation"


def wizard_test():
    wizard = Wizard('Python2.7.gzip', '/usr/bin/')
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})
    wizard.execute()

###########################################


class Command(object):
    __metaclass__ = ABCMeta

    def __init__(self, recv):
        self.recv = recv

    def execute(self):
        pass


class ConcreteCommand(Command):
    def __init__(self, recv):
        self.recv = recv

    def execute(self):
        self.recv.action()


class Receiver(object):
    def action(self):
        print "Receiver Action"


class Invoker(object):
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


def command_test():
    recv = Receiver()
    cmd = ConcreteCommand(recv)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()

##############################################


class Order(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass


class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


class StockTrade(object):
    def buy(self):
        print "You will buy stocks"

    def sell(self):
        print "You will sell stocks"


class Agent(object):
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()


def order_test():
    # client
    stock = StockTrade()
    buyStock= BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)

    # invoker
    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)


if __name__ == '__main__':
    # wizard_test()
    # command_test()
    order_test()