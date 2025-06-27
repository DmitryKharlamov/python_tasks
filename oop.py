#Задание 1. Инкапсуляция
# Создайте класс BankAccount, который инкапсулирует данные о балансе.
#  Реализуйте методы:
# deposit(amount) — пополнение счёта;
# withdraw(amount) — снятие средств (не должно позволять уйти в минус);
# get_balance() — получить текущий баланс.
#
#
# Баланс должен быть защищён от прямого изменения (например, self.__balance).
from abc import ABC, abstractmethod


class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.__balance = amount

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Недостаточно средств")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount('Dmitry', 100)

account.deposit(50)
account.withdraw(30)
account.withdraw(200)
print("Баланс:", account.get_balance())
# Создайте базовый класс Employee с атрибутами name, position, salary и методом get_info().
# Создайте подклассы:
# Developer, у которого есть доп. атрибут programming_language;
# Manager, у которого есть список подчинённых (employees).
#
#
# Каждый подкласс должен переопределять метод get_info().
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return self.name, self.position, self.salary

class Developer(Employee):
    def __init__(self, name, position, salary, programming_language):
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    def get_info(self):
        return self.name, self.position, self.salary, self.programming_language

class Manager(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position, salary)
    employees = []

    def get_info(self):
        return self.name, self.position, self.salary, self.employees

dev1 = Developer("Алиса", 'Разработчик Питон', 10000, 'Python')
dev2 = Developer("Алексей", 'Frontend', 10000, 'JavaScript')
manager = Manager("Елена", 'PM', 10000000)
manager.employees.append(dev1)
print(dev1.get_info())
print(dev2.get_info())
print(manager.employees[0].get_info())

# Создайте базовый класс Shape с методом area() и perimeter() (возвращает 0 по умолчанию).
# Создайте подклассы:
# Rectangle (по width, height);
# Circle (по radius).
# Продемонстрируйте работу полиморфизма: создайте список фигур и выведите площадь и периметр каждой из них с помощью одного и того же кода.
class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

shapes = [
    Rectangle(3, 4),
    Circle(5),
    Rectangle(6, 2),
    Circle(1.5)
]

for shape in shapes:
    print(f"{shape.__class__.__name__}:")
    print(f"  Площадь: {shape.area():.2f}")
    print(f"  Периметр: {shape.perimeter():.2f}")


# Используйте модуль abc.
# Создайте абстрактный класс Transport с абстрактными методами:
# start_engine(),
# stop_engine(),
# move().
# Создайте классы Car и Boat, реализующие интерфейс Transport.
class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def start_engine(self):
        print('start engine')

    def stop_engine(self):
        print('stop engine')

    def move(self):
        print('move')

class Boat(Transport):
    def start_engine(self):
        print('start engine')
    def stop_engine(self):
        print('stop engine')
    def move(self):
        print('move')


# Создайте два класса:
# Flyable, с методом fly() (выводит I'm flying!);
# Swimmable, с методом swim() (выводит I'm swimming!).
#
#
# Создайте класс Duck, наследующий оба класса. Добавьте метод make_sound() (выводит Quack!).
# Создайте экземпляр Duck и вызовите все три метода.
class Flyable:
    def fly(self):
        print("i'm flying")

class Swimable:
    def swim(self):
        print("i'm swiming")

class Duck(Flyable, Swimable):
    def make_sound(self):
        print("Quack")

# duck = Duck()
# duck.swim()
# duck.fly()
# duck.make_sound()

# Создайте абстрактный класс Animal с методами speak() и move().
# Создайте классы Dog, Bird, Fish. Пусть:
# Dog говорит "Woof!" и бегает,
# Bird говорит "Tweet!" и летает (наследует Flyable),
# Fish молчит и плавает (наследует Swimmable).
#
#
# Положите всех животных в один список и вызовите методы speak() и move() в цикле.
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    @abstractmethod
    def move(self):
        pass
class Dog(Animal):
    def speak(self):
        print("Woof")
    def move(self):
        print("бегает")

class Bird(Animal, Flyable):
    def speak(self):
        print("Tweet")

    def move(self):
        self.fly()

class Fish(Animal, Swimable):
    def speak(self):
        print("молчит")
    def move(self):
        self.swim()

animals = [Dog(), Bird(), Fish()]
for animal in animals:
    animal.speak()
    animal.move()



# Условия:
# Реализуйте класс Logger с использованием паттерна Singleton, чтобы гарантировать, что в программе существует только один экземпляр логгера.
# Класс должен:
# Иметь метод log(self, message: str), который добавляет сообщение в список логов.
# Иметь метод get_logs(self), который возвращает список всех сообщений.
# Покажите, что два экземпляра Logger — это один и тот же объект.
# Технические требования:
# Реализация должна быть написана вручную, не использовать сторонние библиотеки.
# Singleton можно реализовать через __new__, декоратор или метакласс (на выбор).
#
# Пример использования
#
# logger1 = Logger()
# logger2 = Logger()
#
# logger1.log("First message")
# logger2.log("Second message")
#
# assert logger1 is logger2, "Logger is not a singleton!"
# assert logger1.get_logs() == ["First message", "Second message"]
class Singleton:
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

class Logger:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    logs = []
    def log(self, message: str):
        self.logs.append(message)


    def get_logs(self):
        return self.logs



# У вас есть класс Report, который:
# хранит данные отчета,
# генерирует его в PDF,
# сохраняет на диск.
# Разделите этот класс на части, каждая из которых будет отвечать только за одну ответственность.

class ReportData:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class PDFGenerator:
    def generate_pdf(self):
        print("PDF generated")

class FileSaver:
    def save_to_file(self, filename):
        print(f"Saved {filename}")
# Реализуйте систему оплаты: базовый класс PaymentProcessor, у которого есть метод pay().
# Добавьте поддержку разных способов оплаты (PayPal, CreditCard, Crypto) без изменения базового кода.
# Цель:
# Использовать полиморфизм или абстракции (например, через ABC).
class PaymentProcessor(ABC):
     @abstractmethod
     def pay(self):
         pass

class PayPalProcessor(PaymentProcessor):
    def pay(self):
        print("pay PayPal")

class CreditCardProcessor(PaymentProcessor):
    def pay(self):
        print("pay credit card")

# Реализуйте класс Bird и подклассы Sparrow и Penguin.
# Убедитесь, что замена Bird на любой его подкласс не ломает код.
class Bird:
    def make_sound(self):
        print("bird make sound")

    def move(self):
        print("bird move")

class Sparrow(Bird):
    def make_sound(self):
        print("sparrow make sound")

    def move(self):
        print("sparrow flying")

class Penguin(Bird):
    def make_sound(self):
        print("penguin make sound")
    def move(self):
        print("penguin swiming")

def describe_bird(bird: Bird):
    bird.make_sound()
    bird.move()

birds = [Sparrow(), Penguin()]

for bird in birds:
    describe_bird(bird)

# Представьте интерфейс Animal с методами: fly(), run(), swim().
# Реализуйте Lion(), которая умеет только бегать, не заставляя её реализовывать ненужные методы.
class Runnable(ABC):
    @abstractmethod
    def run(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass

class Lion(Runnable):
    def run(self):
        print("Lion runs")

# Создайте класс Temperature, который хранит температуру в градусах Цельсия, но:
# умеет создавать объект из градусов Фаренгейта (@classmethod),
# вычисляет температуру в Кельвинах как свойство (@property),
# предоставляет статический метод для проверки, является ли температура точкой замерзания воды (0°C или ниже).
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_farenheit(cls, farenheit):

        celsius = (farenheit - 32) * 5 / 9
        return cls(celsius)

    @property
    def kelvin(self):
        return self.celsius + 273.15

    @staticmethod
    def zero_tempreture(celsius):
        if celsius <= 0:
            return 'Температура являктся точкой замерзания воды'


t1 = Temperature(25)  # 25°C
print(f"t1 в Кельвинах: {t1.kelvin}")  # 298.15

t2 = Temperature.from_farenheit(32)  # 32°F == 0°C
print(f"t2 в Кельвинах: {t2.kelvin}")  # 273.15

print(f"Температура t2 — замерзает ли вода? {Temperature.zero_tempreture(t2.celsius)}")
