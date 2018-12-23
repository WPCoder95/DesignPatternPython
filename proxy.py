# -*- coding:utf-8 -*-
'''
代理模式
'''
from abc import ABCMeta, abstractmethod

class Actor(object):
    def __init__(self):
        self.isBusy = False

    def occupied(self):
        self.isBusy = True
        print(type(self).__name__, 'is occupied with current movie.')

    def available(self):
        self.isBusy = False
        print(type(self).__name__, 'is free for the movie.')

    def getStatus(self):
        return self.isBusy


class Agent(object):
    def __init__(self):
        self.principle = None

    def work(self):
        self.actor = Actor()
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.available()


def agent_actor_test():
    r = Agent()
    r.work()

##########################################
# 银行卡消费代理模式示例


class Payment(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def doPay(self):
        pass


class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        # assume card number is account number
        self.account = self.card
        return self.account

    def __hasFunds(self):
        print 'Bank:: Checking if Account', self.__getAccount(), 'has enough funds'
        return True

    def setCard(self, card):
        self.card = card

    def doPay(self):
        if self.__hasFunds():
            print("Band:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds!")
            return False


class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def doPay(self):
        card = input("Proxy:: Punch in Card Number: ")
        self.bank.setCard(card)
        return self.bank.doPay()


class Consumer(object):
    def __init__(self):
        print "Consumer:: Let's buy the Demin shirt"
        self.debitCard = DebitCard()
        self.isPurchased = None

    def makePayment(self):
        self.isPurchased = self.debitCard.doPay()

    def __del__(self):
        if self.isPurchased:
            print "Consumer:: Wow! Denim shirt is Mine :-)"
        else:
            print "Consumer:: I should earn more :("


def consumer_bank_test():
    you = Consumer()
    you.makePayment()


if __name__ == '__main__':
    # agent_actor_test()
    consumer_bank_test()