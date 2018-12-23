# -*- coding:utf-8 -*-

class Hotelier(object):
    def __init__(self):
        print "Arrange the Hotel for Marriage? --"

    def __isAvailable(self):
        print "Is the Hotel free for the event on given day?"
        return True

    def bookHotel(self):
        if self.__isAvailable():
            print "Registered the Booking\n"


class Florist(object):
    def __init__(self):
        print "Flower Decorations for the Event? --"

    def setFlowerRequirements(self):
        print "Carnations, Rose and Lilies would be used to for Decorations\n"


class Caterer(object):
    def __init__(self):
        print "Food Arrangements for the Event --"

    def setCuisine(self):
        print "Chinese & Continental Cuisine to be served\n"


class Musincian(object):
    def __init__(self):
        print "Musical Arrangements for the Marriage --"

    def setMusicType(self):
        print "Jazz and Classical will be played\n"




class EventManager(object):
    def __init__(self):
        print "Event Manager:: Let me talk to the folks"

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musincian()
        self.musician.setMusicType()


class You(object):
    def __init__(self):
        print "You:: Woa! Marriage Arrangement??!!"

    def askEventManager(self):
        print "you:: Let's Contact the Event Manager\n"
        em = EventManager()
        em.arrange()

    def __del__(self):
        print "You:: Thanks to Event Manager, all perparation done! Phew!"


def facade_example_test():
    you = You()
    you.askEventManager()


if __name__ == '__main__':
    facade_example_test()