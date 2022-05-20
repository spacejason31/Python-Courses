#Class: Australian
class Australian():
    is_human = True
    enjoys_sport = True

    @classmethod
    def is_sporty_human(cls):
        return cls.is_human and cls.enjoys_sport

john = Australian()
type(john)
john.is_human
john.enjoys_sport
Australian.is_sporty_human()
aussie = Australian()
aussie.is_sporty_human()

#Class Pet
import random
class Pet():
    def __init__(self, height, name = None):
        self.height = height
        self.name = name

    is_human = False
    owner = 'Michael Smith'

    def is_tall(self, tall_if_at_least):
        return self.height>=tall_if_at_least

    def __str__(self):
        return '%s (height: %s cm)' % (self.name, self.height)

    @classmethod
    def owned_by_smith_family(cls):
        return 'Smith' in cls.owner

    @classmethod
    def create_random_height_pet(cls):
        height = random.randrange(0,100)
        return cls(height)

for i in range(5):
    pet = Pet.create_random_height_pet()
    print(pet.height)
bowser = Pet(60)
bowser.height = 40
bowser.is_tall(30)
my_pet = Pet(30, 'chubster')
print(my_pet)
my_other_pet = Pet(40, 'Rudolf')
print(my_other_pet)

class Cat(Pet):
    is_feline = True
    def make_sound(self):
        print('Woof!')
class Dog(Pet):
    is_feline = False
    def make_sound(self):
        print('Meow!')

my_cat = Cat('Kibbles', 8)
my_cat.is_feline
my_dog = Dog("Rover", 15)
my_dog.is_feline

class Cat():
    def make_sound(self):
        print('Meow!')
class Dog():
    def make_sound(self):
        print('Woof!')
class CatDog(Cat, Dog):
    def make_sound(self):
        for i in range(3):
            super().make_sound()
my_pet = CatDog()
my_pet.make_sound()

#Class: Country
class Country():
    def __init__(self, name = 'Unspecified', population = None, size_kmsq = None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

    def size_miles_sq(self, conversion_rate = 0.621371):
        return self.size_kmsq * conversion_rate ** 2

    def __str__(self):
        label = self.name
        if self.population:
            label = '%s, population: %s' % (label, self.population)
        if self.size_kmsq:
            label = '%s, size_kmsq: %s' % (label, self.size_kmsq)
        return label

    @classmethod
    def create_with_msq(cls, name, population, size_msq):
        size_kmsq = size_msq / 0.621371 ** 2
        return cls(name, population, size_kmsq)

algeria = Country(name = 'Algeria', size_kmsq = 2.382e6)
algeria.size_miles_sq(conversion_rate=0.6)
chad = Country(name = 'Chad', population = 100)
print(chad)
ukraine = Country(name = 'Ukraine', size_kmsq = 245e6)
print(ukraine)
mexico = Country.create_with_msq('Mexico', 150e6, 76e4)
mexico.size_kmsq

#Class: Diary
import datetime
class Diary():
    def __init__(self, birthday, christmas):
        self.birthday = birthday
        self.christmas = christmas
    def show_birthday(self):
        return self.format_date(self.birthday)
    def show_christmas(self):
        return self.format_date(self.christmas)

    @staticmethod # allows a method within the class to be accessed by other methods in the class
    def format_date(date):
        return date.strftime('%d-%b-%y')

my_diary = Diary(datetime.date(2020, 5, 14), datetime.date(2020, 12, 25))
my_diary.show_birthday()

class CustomDiary(Diary):
    def __init__(self, birthday, christmas, date_format):
        self.date_format = date_format
        super().__init__(birthday, christmas)
    def format_date(self, date):
        return date.strftime(self.date_format)

first_diary = CustomDiary(datetime.date(2018, 1, 1), datetime.date(2018, 3, 3), '%d-%b-%Y')
second_diary = CustomDiary(datetime.date(2018, 1, 1), datetime.date(2018, 3, 3), '%d/%m/%Y')
print(first_diary.show_birthday())
print(second_diary.show_birthday())

#Class: Temperature
class Temperature():
    def __init__(self, celsius):
        self.celsius = celsius
    @property
    def fahrenheit(self):
        return self.celsius * 9/5 + 32
    @fahrenheit.setter
    def fahrenheit(self, value):
        if value < -460:
            raise ValueError("Temperatures less than -460 are not possible")
        self.celsius = (value-32)*5/9

my_temp = Temperature(0)
print(my_temp.fahrenheit())
my_temp.celsius = -10
print(my_temp.fahrenheit())

freezing = Temperature(100)
freezing.fahrenheit

temp = Temperature(5)
temp.fahrenheit
temp.fahrenheit = 32
temp.fahrenheit
temp = Temperature(50)
temp.fahrenheit = -500

#Class: Person
class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

customer = Person('Mary', 'Lou')
customer.full_name
customer.full_name = 'Mary Schmidt'
customer.last_name
customer.full_name = 'Mary Ann Schmidt'

class BetterPerson(Person):
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    @full_name.setter
    def full_name(self, name):
        names = name.split(' ')
        self.last_name = names[-1]
        if len(names) > 2:
            self.first_name = ' '.join(names[:-1])
        elif len(names) <= 2:
            self.first_name = names[-1]

my_person = BetterPerson('Mary', 'Smith')
my_person.full_name = 'Mary Ann Smith'
print(my_person.first_name)
print(my_person.last_name)

class TalkativePerson(Adult):
    def speak(self):
        super().speak()
        print("It is a pleasure to meet you!")
john = TalkativePerson('John', 'Tonic')
john.speak()

class Baby(Person):
    def speak(self):
        print("Blah "*3, "feed me")
class Adult(Person):
    def speak(self):
        print('Hello, my name is %s' % self.first_name)

jess = Baby('Jessie', 'Mcdonald')
tom = Adult('Thomas', 'Smith')
jess.speak()
tom.speak()

class MyInt(int):
    def is_divisible_by(self, x):
        return self % x == 0

a = MyInt(8)
a.is_divisible_by(3)

import datetime
class MyDate(datetime.date):
    def add_days(self, n):
        return self + datetime.timedelta(n)

d = MyDate(2019, 12, 1)
print(d.add_days(40))
print(d.add_days(400))

#Organized People Classes
class Calendar():
    def book_appointment(self, date):
        print('Booking appointment for date %s' % date)

class OrganizedBaby(Baby, Calendar):
    def book_appointment(self, date):
        print('Note: you are booking an appointment with an infant.')
        super().book_appointment(date)
class OrganizedAdult(Adult, Calendar):
    pass
andres = OrganizedBaby('Andres', 'Gomez')
boris = OrganizedAdult('Boris', 'Bumblebutton')
andres.speak()
boris.speak()
boris.book_appointment(datetime.date(2018,1,1))
andres.book_appointment(datetime.date(2018,1,1))