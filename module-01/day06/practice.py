from abc import ABC, abstractmethod

# 1. Spot the SRP violation

class Report:
    def build(self):
        print("Building report")


class ReportSaver:
    def save(self):
        print("Saving report")


class ReportEmailer:
    def email(self):
        print("Emailing report")


report = Report()
report.build()

saver = ReportSaver()
saver.save()

emailer = ReportEmailer()
emailer.email()


# 2. Refactor to OCP

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        print("Circle area")


class Square(Shape):
    def area(self):
        print("Square area")


class Triangle(Shape):
    def area(self):
        print("Triangle area")


shapes = [
    Circle(),
    Square(),
    Triangle()
]

for shape in shapes:
    shape.area()


# 3. Write a Singleton

class AppSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.currency = "ETB"
        return cls._instance


settings1 = AppSettings()
settings2 = AppSettings()

print(settings1 is settings2)


# 4. Write a Factory

class ShapeFactory:
    @staticmethod
    def create(kind):
        if kind == "circle":
            return Circle()
        elif kind == "square":
            return Square()
        elif kind == "triangle":
            return Triangle()
        else:
            raise ValueError("Unknown shape")


shape = ShapeFactory.create("circle")
shape.area()


# 5. Write an Observer pair

class NewsAgency:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update()


class SubscriberOne:
    def update(self):
        print("Subscriber One received news")


class SubscriberTwo:
    def update(self):
        print("Subscriber Two received news")


agency = NewsAgency()

agency.subscribe(SubscriberOne())
agency.subscribe(SubscriberTwo())

agency.notify()