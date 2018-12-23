# -*-coding:utf-8 -*-
'''
观察者模式
'''

from abc import ABCMeta, abstractmethod


class Subject(object):
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer1(object):
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)


class Observer2(object):
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)


def subject_test():
    subject = Subject()
    observer1 = Observer1(subject)
    observer2 = Observer2(subject)
    subject.notifyAll('notification')

###############################################


class Subscriber:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self):
        pass


class NewPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, new):
        self.__latestNews = new

    def getNews(self):
        return "Got News: ", self.__latestNews


class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class AnyOtherSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


def subscriber_test():
    news_publisher = NewPublisher()
    # 观察者进行注册以订阅消息
    for subscriber in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        subscriber(news_publisher)
    print('Subscribers: ', news_publisher.subscribers())
    # 订阅中心发布消息
    news_publisher.addNews('Hello, World')
    news_publisher.notifySubscribers()
    # 某对象取消订阅
    print('Detached:', type(news_publisher.detach()).__name__)
    print('Subscribers:', news_publisher.subscribers())
    # 新消息发布并通知所有订阅者
    news_publisher.addNews('My second news!')
    news_publisher.notifySubscribers()


'''
# 观察者抽象类
class Observer(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def update(self, data):
        pass


# 主题抽象类
class Subject(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self._observers = []

    def attach(self, obj):
        self._observers.append(obj)

    def detach(self, obj):
        try:
            self._observers.remove(obj)
        except ValueError:
            pass

    def notify_all(self, data):
        for obs in self._observers:
            obs.update(data)

    # def notify(self, obj, data):
    #     for obs in self._observers:
    #         if obj == obs:
    #             obs.updata(data)


class DataCenter(Subject):
    def __init__(self, name='', data=None):
        Subject.__init__(self)
        self.__name = name
        self.__data = data

    def data(self, value):
        self.__data = value
        # information change, notice the observers to update
        # self.notify(self.__data)
        self.notify_all(self.__data)


class TestAObserver(Observer):
    def update(self, data):
        print 'TestA Update : {}'.format(data)


class TestBObserver(Observer):
    def update(self, data):
        print 'TestB Update : {}'.format(data)


def data_center_test():
    obs_a = TestAObserver()
    obs_b = TestBObserver()
    data_center = DataCenter(name='DataCenter')
    data_center.attach(obs_a)
    data_center.attach(obs_b)
    data_center.data('test')

'''

if __name__ == '__main__':
    subject_test()
    subscriber_test()
