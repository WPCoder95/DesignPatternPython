# -*- coding:utf-8 -*-
'''
状态模式
'''

from abc import ABCMeta, abstractmethod
'''
class State(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def Handle(self):
        pass

class ConcreteStateB(State):
    def Handle(self):
        print "ConcreteStateB"


class ConcreteStateA(State):
    def Handle(self):
        print "ConcreteStateA"


class Context(State):
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def Handle(self):
        self.state.Handle()


def state_test():
    context = Context()
    stateA = ConcreteStateA()
    stateB = ConcreteStateB()
    context.setState(stateA)
    context.Handle()
'''


class State(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def doThis(self):
        pass


class StartState(State):
    def doThis(self):
        print "TV switching ON ..."


class StopState(State):
    def doThis(self):
        print "TV switching OFF ..."

class TVContext(State):
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def doThis(self):
        self.state.doThis()

def tv_test():
    context = TVContext()
    context.getState()
    start = StartState()
    stop = StopState()
    context.setState(stop)
    context.doThis()

########################################


class ComputerState(object):
    name = 'state'
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print "Current:", self, "=> switched to new state", state.name
            self.__class__ = state
        else:
            print "Current:", self, "=> switched to", state.name, "not possible"

    def __str__(self):
        return self.name


class Off(ComputerState):
    name = 'Off'
    allowed = ['On']


class On(ComputerState):
    name = 'On'
    allowed = ['Off', 'Suspend', 'Hibernate']


class Suspend(ComputerState):
    name = 'Suspend'
    allowed = ['On']


class Hibernate(ComputerState):
    name = 'Hibernate'
    allowed = ['On']


class Computer(object):
    def __init__(self, model='HP'):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


def computer_test():
    comp = Computer()
    comp.change(On)
    comp.change(Off)

    comp.change(On)
    comp.change(Suspend)

    comp.change(Hibernate)
    comp.change(On)
    comp.change(Off)


if __name__ == '__main__':
    # state_test()
    # tv_test()
    computer_test()