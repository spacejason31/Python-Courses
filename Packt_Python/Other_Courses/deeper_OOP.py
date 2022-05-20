#Multiple inheritance, duck-typing, & mixins

from datetime import datetime
from time import sleep

class Mixin():
    def log_critical(self, extra = None):
        print(datetime.now(), extra)
        sleep(0.2)
        start = datetime.now()
        print(start, '... processing ...')
        sleep(0.5)
        finish = datetime.now()
        print(finish, "... completed ...")
        print(f"Runtime: {finish - start} \n")

class PythonClass(Mixin, object):
    def color(self):
        print("i am blue")

    def critical_task(self, extra = None):
        Mixin().log_critical(f'... Critical task started in: ' + self.__class__.__qualname__)
        # note: b/c this is multiple-inheritance, you have to call the class with 'Mixin()' instead of just 'Mixin'

class SomeClass(PythonClass):
    def color(self):
        print("i am red")

class SomeOtherClass(PythonClass):
    def color(self):
        print("i am orange")

class NotFromPythonClass(Mixin, object):
    def color(self):
        print('i am yellow')

class NotFromPythonNoMethod(object):
    def color_1(self):
        print('i am black')

    def critical_task(self, extra = None):
        Mixin().log_critical(f'... Critical task started in: ' + self.__class__.__qualname__)
        # note: b/c this is multiple-inheritance, you have to call the class with 'Mixin()' instead of just 'Mixin'

a = PythonClass()
b = SomeClass()
c = SomeOtherClass()
d = NotFromPythonClass()
e = NotFromPythonNoMethod()

some_object = [a, b, c, d]
more_objects = [a, b, c, d, e, a]
for obj in some_object:
    obj.color()
for obj in more_objects:
    try:
        obj.color()
    except Exception as ex:
        print("object threw exception:", ex)

for obj in more_objects:
    if hasattr(obj, 'color'):
        obj.color()
    else:
        print(f'Object {obj} does not have the required attribute')

for obj in more_objects:
    if hasattr(obj, 'color'):
        obj.color()
    if hasattr(obj, 'critical_task'):
        obj.critical_task()

for obj in more_objects:
    if hasattr(obj, 'critical_task'):
        obj.critical_task()


# Constructors & class methods
class Colors():
    def __init__(self):
        self.colors = []

    @classmethod
    def generate_data(cls):             # cls instead of self
        return ['blue', 'red', 'orange', 'yellow', 'black']

class PythonClass(object):
    def __init__(self, data = None):
        self.data = data                # data attribute

    @classmethod
    def create_data(cls, data_class):
        print('*' * 20)
        print('cls: ', cls.__qualname__)
        print('data_class: ', data_class.__qualname__)
        print('*' * 20)

        data_list = []                              # cls = PythonClass
        for data_item in data_class.generate_data():# local list to hold data
            data_list.append(cls(data_item))        # call classmethod of: Colors class
        return data_list                            # create instance of: PythonClass to hold data

color_objects = PythonClass.create_data(Colors)     # parentheses after 'PythonClass' creates an instance of that class, here we don't want to

color_objects
color_objects[1].data

color_objects = PythonClass.create_data(Colors)
for obj in color_objects:
    print(obj.data)