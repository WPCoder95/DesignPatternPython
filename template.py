# -*- coding:utf-8 -*-
'''
模板模式
'''

from abc import ABCMeta, abstractmethod


class Compiler(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()


class iOSCompiler(Compiler):
    def collectSource(self):
        print "Collecting Swift Source Code"

    def compileToObject(self):
        print "Compile Swift code to LVM bitCode"

    def run(self):
        print "Program runing on runtime environment"


def compiler_test():
    iOS = iOSCompiler()
    iOS.compileAndRun()

#######################################################


class AbstractClass(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def template_methon(self):
        print "Defining the Algorithm, Operation 1 follows Operation2"
        self.operation2()
        self.operation1()

class ConcreteClass(AbstractClass):
    def operation1(self):
        print "My Concrete Operation"

    def operation2(self):
        print "Operation 2 remains same"


class Client(object):
    def main(self):
        self.concreate = ConcreteClass()
        self.concreate.template_methon()


def client_test():
    client = Client()
    client.main()


#############################################


from abc import abstractmethod, ABCMeta


class Trip(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def setTransport(self):
        pass

    @abstractmethod
    def day1(self):
        pass

    @abstractmethod
    def day2(self):
        pass

    @abstractmethod
    def day3(self):
        pass

    @abstractmethod
    def returnHome(self):
        pass

    def itinerary(self):
        self.setTransport()
        self.day1()
        self.day2()
        self.day3()
        self.returnHome()


class VeniceTrip(Trip):
    def setTransport(self):
        print "Take a boat and find you way in the Grand Canal"

    def day1(self):
        print "Visit St Mark's Basilica in St Mark's Square"

    def day2(self):
        print "Appreciate Doge's Palace"

    def day3(self):
        print "Enjoy the food near the Rialto Bridge"

    def returnHome(self):
        print "Got souvenirs for friends and get back"


class MaldivesTrip(Trip):
    def setTransport(self):
        print "On foot, on any island, Wow!"

    def day1(self):
        print "Enjoy the marine life of Banana Reef"

    def day2(self):
        print "Relax on the beach and enjoy the sun"

    def day3(self):
        print "Relax for the water sport and snorkelling"

    def returnHome(self):
        print "Don't feel like leaving the beach..."


class TravelAgency(object):
    def arrange_trip(self):
        choice = input("What kind of place you'd like to go historical or to a beach?")
        if choice == 'historical':
            self.trip = VeniceTrip()
            self.trip.itinerary()
        if choice == 'beach':
            self.trip = MaldivesTrip()
            self.trip.itinerary()


def travel_test():
    TravelAgency().arrange_trip()

if __name__ == '__main__':
    # compiler_test()
    # client_test()
    travel_test()