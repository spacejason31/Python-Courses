class MyFirstClass:
    pass
class Point:
    pass
p1 = Point()
p2 = Point()
p1.x = 5
p1.y = 4
p2.x = 3
p2.y = 6
print(p1.x, p1.y)

l1 = list([1,2,3,4])
for i in reversed(l1):
    print(i)

l2 = [1,2,1,4,7,12,9]
for i in enumerate(l2):
    print(i)

l3 = zip(l1, l2)
for i in l3:
    print(i)

hasattr(p1, "x")
t = getattr(p1, "x")
type(t)
type(p1.x)
t == p1.x

contents = "Some file content"
file = open("filename", "w")
file.write(contents)
file.close()

file = open("filename", "a")
file.write("\na little bit more")
file.close()

with open('filename') as file:
    for line in file:
        print(line, end='')

class StringJoiner(list):
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        self.result = "".join(self)

import random, string
with StringJoiner() as joiner:
    for i in range(15):
        joiner.append(random.choice(string.ascii_letters))
print(joiner.result)

def no_args():
    pass
def mandatory_args(x,y,z):
    pass
a_variable = l2
mandatory_args("a string", a_variable, 5)
def default_args(x,y,z, a="Some String", b=False):
    print(x, y, z, a, b)
default_args("a string", a_variable, 8, "", True)
default_args(y=1, z=2, x=3, a="hi")
