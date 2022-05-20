from turtle import Turtle, done
turtle = Turtle()
turtle.right(180)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
done()

import dataclasses
@dataclasses.dataclass
class Point:
    x: int
    y: int
p = Point(x=10, y=20)
print(p)
p2 = Point(x=10,y=20)
p==p2
dataclasses.asdict(p)

#Date/Time handling in python
import datetime
datetime.date.today()
from dateutil import tz
d = datetime.datetime(1989, 4, 24, 10, 11, tzinfo=tz.gettz("Europe/Madrid"))
print(d)
d1 = datetime.datetime(1989, 4, 24, hour=11, tzinfo=tz.gettz("Europe/Madrid"))
d2 = datetime.datetime(1989, 4, 24, hour=8, tzinfo=tz.gettz("America/Los_Angeles"))
print(d1>d2)
print(d1, d2)
d2_madrid = d2.astimezone(tz.gettz("Europe/Madrid"))
print(d1, d2_madrid)
print(d1.hour, d2_madrid.hour)
d1_utc = d1.astimezone(tz.gettz("UTC"))
d2_utc = d2.astimezone(dt.timezone.utc)
print(d1_utc, d2_utc, "\n", d1_utc.hour, d2_utc.hour)

import datetime as dt
d3 = dt.datetime(2019, 2, 25, 10, 50, tzinfo=dt.timezone.utc)
d4 = dt.datetime(2019, 2, 26, 11, 20, tzinfo=dt.timezone.utc)
td = d4-d3
td.total_seconds()
d5 = dt.datetime.now(dt.timezone.utc)
d5.isoformat()

import datetime as dt
import time
datetime_now = dt.datetime.now(dt.timezone.utc)
time_now = time.time()
epoch = datetime_now - dt.timedelta(seconds=time_now)
print(epoch)

import calendar
c = calendar.Calendar()
list(c.itermonthdates(2019, 2))
list(d for d in c.itermonthdates(2019,2) if d.month==2)
list(d for d in c.itermonthdates(2020,2) if d.month==2)

import random
import time
t1 = time.time()
l = [random.randint(1,999) for _ in range(10*3)]
t2 = time.time()
t2-t1

#Accessing sys/os/environmental information
import platform
import os
import sys
print("Process id:", os.getpid())
print("Parent process id:", os.getppid())
print("Machine network name:", platform.node())
print("Python version:", platform.python_version())
print("System:", platform.system())
print("Python module lookup path:", sys.path)
print("Command to run python", sys.argv)
print("USERNAME environment variable:", os.environ["USERNAME"])

import pathlib
path = pathlib.Path()
print(repr(path))

p = pathlib.Path("")
txt_files = p.glob("*.txt")
print("*.txt:", list(txt_files))
print("**/*.txt", list(p.glob("**/*.txt")))
print("*/*:", list(p.glob("*/*")))
print("Files in */*:", [f for f in p.glob("*/*") if f.is_file()])

#Create a subprocess that analyzes a line of code and reports whether the code crashes (aka results in any number other than 0)
import subprocess
import sys
code = 'compile("1" + "+1" * 10 ** 6, "string", "exec)'
result = subprocess.run([
    sys.executable,
    "-c", code
])
print(result.returncode)

#Access and read a web file, deconstruct it into a list of strings, and analyze the text
import urllib.request
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = urllib.request.urlopen(url)
words = response.read().decode().split()
len(words)
import collections
word_counter = collections.Counter(words)
for word, count in word_counter.most_common(5):
    print(word, "-", count)
print("QUESTION", "-", word_counter["QUESTION"])
print("CIRCUMFLEX", "-", word_counter["CIRCUMFLEX"])
print("DIGIT", "-", word_counter["DIGIT"])
print("PYTHON", "-", word_counter["PYTHON"])

#Playing with word list & defaultdict as a counter
import urllib.request
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = urllib.request.urlopen(url)
words = response.read().decode().split()
words = [x.lower() for x in words]
        # ^- list comprehension: [\expression for \item in \list]
import collections
word_count = collections.defaultdict(int)
for word in words:
    word_count[word] += 1
word_count

# 3 ways to create a counter dictionary
d = {}
def function(x):
    if x not in d:      #Option 1
        d[x] = 1
    else:
        d[x] += 1
def function(x):
    try:                #Option 2
        d[x] += 1
    except KeyError:
        d[x] = 1
import collections
d = collections.defaultdict(int)        #initial value = 0
d = collections.defaultdict(lambda: 1)  #initial value = 1
def function(x):        #Option 3
    d[x] += 1

_audit = {}
def add_audit(area, action):
    if area in _audit:
        _audit[area].append(action)
    else:
        _audit[area] = [action]
def report_audit():
    for area, actions in _audit.items():
        print(f"{area} audit:")
        for action in actions:
            print(f"- {action}")
        print()
add_audit("HR", "Hired Sam")
add_audit("Finance", "Used 1000£")
add_audit("HR", "Hired Tom")
report_audit()
_audit = collections.defaultdict(list)
_audit = collections.defaultdict(lambda: ["Area created"])
def add_audit(area, action):
    _audit[area].append(action)

#Chain Maps
import collections
_defaults = {
    "appetisers": "Hummus",
    "main": "Pizza",
    "dessert": "Chocolate Cake",
    "drink": "Water",
}
def prepare_menu(customizations):
    return collections.ChainMap(customizations, _defaults)
def print_menu(menu):
    for key, value in menu.items():
        print(f"For {key}: {value}.")
menu1 = prepare_menu({})
print_menu(menu1)
menu2 = prepare_menu({"drink": "Red Wine"})
print_menu(menu2)
menu3 = prepare_menu({"sides": "French Fries"})
print_menu(menu3)
_defaults["main"] = "Pasta"
print_menu(menu3)

#Using functools to create a cache for functions to re-use the output from heavy operations
import time
def func(x):
    time.sleep(1)
    print(f"Heavy operation for {x}")
    return x*10
print("func returned:", func(1))
print("func returned:", func(1))
import functools
@functools.lru_cache(maxsize=2)
def func(x):
    time.sleep(1)
    print(f"Heavy operation for {x}")
    return x*10
print("func returned:", func(1))
print("func returned:", func(2))
print("func returned:", func(3))
print("func returned:", func(3))
print("func returned:", func(2))
print("func returned:", func(1))

import functools
import time
def func(x):
    time.sleep(1)
    print(f"Heavy operation for {x}")
    return x*10
cached_func = functools.lru_cache()(func)
print("Cached func returned:", cached_func(1))
print("Cached func returned:", cached_func(1))
print("func returned:", func(1))
print("func returned:", func(1))

#Using functools.partial to partially modify an existing function for repurposing
def func(x, y, z):
    print("x:", x)
    print("y:", y)
    print("z:", z)
func(1, 2, 3)
import functools
new_func = functools.partial(func, z="wops")
new_func(1,2)
new_func = functools.partial(func, "wops")
new_func(1,2)

import sys
print("hello stderr", file=sys.stderr)
import functools
print_stderr = functools.partial(print, file=sys.stderr)
print_stderr("hello stderr")