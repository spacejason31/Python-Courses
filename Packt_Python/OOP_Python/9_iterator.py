#Comparing for loops to object-oriented iterations
class CapitalIterable:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return CapitalIterator(self.string)

class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()

        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self

iterable = CapitalIterable('the quick brown fox jumps over the lazy dog')
iterator = iter(iterable)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

for i in iterable:
    print(i)

#List comprehensions
input_strings = ['1', '5', '28', '131', '3']
output_integers = []                            #traditional way
for num in input_strings:
    output_integers.append(int(num))

input_strings = ['1', '5', '28', '131', '3']    #using list comprehension
output_integers = [int(num) for num in input_strings]

output_integers = [int(num) for num in input_strings if len(num) < 3]
        #note: len(num) looks at the length of each element not the list

#Example of when a list comprehension could work, but a for loop is a better solution:
import sys
filename = sys.argv[1]

with open(filename) as file:
    header = file.readline().strip().split("\t")
contacts = [
dict(
zip(header, line.strip.split("\t")))
for line in file
]
for contact in contacts:
    print("email: {email} -- {last}, {first}".format(**contact))

from collections import namedtuple
Book = namedtuple("Book", "author title genre")
books = [
    Book("Pratchett", "Nightwatch", "fantasy"),
    Book("Pratchett", "Thief Of Time", "fantasy"),
    Book("Le Guin", "The Dispossessed", "scifi"),
    Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
    Book("Turner", "The Thief", "fantasy"),
    Book("Phillips", "Preston Diamond", "western"),
    Book("Phillips", "Twice Upon A Time", "scifi"),]
fantasy_authors = {b.author for b in books if b.genre == "fantasy"}
fantasy_titles = {b.title: b for b in books if b.genre == "fantasy"}

#Generator expressions
#parses a log file and outputs a new log file that containes only WARNING lines
import sys
inname = sys.argv[1]
outname = sys.argv[2]

with open(inname) as infile:
    with open(outname, "w") as outfile:
        warnings = (l for l in infile if 'WARNING' in l)
        for l in warnings:
            outfile.write(l)

#large object-oriented code that reads WARNING lines & deletes the WARNING column from the output file
#not recommended; only shows what is happening in the next generator
class WarningFilter:
    def __init__(self, insequence):
        self.insequence = insequence

    def __iter__(self):
        return self

    def __next__(self):
        l = self.insequence.readline()
        while l and "WARNING" not in l:
            l = self.insequence.readline()
            if not l:
                raise StopIteration
                return l.replace("\tWARNING", "")

with open(inname) as infile:
    with open(outname, "w") as outfile:
        filter = WarningFilter(infile)
        for l in filter:
            outfile.write(l)

def warnings_filter(insequence):
    for l in insequence:
        if "WARNING" in l:
            yield l.replace("\tWARNING", "")

with open(inname) as infile:
    with open(outname, "w") as outfile:
        filter = warnings_filter(infile)
        for l in filter:
            outfile.write(l)

#Modeling a computer's filesystem
class File:
    def __init__(self, name):
        self.name = name

class Folder(File):

    def __init__(self, name):
        super().__init__(name)
        self.children = []

root = Folder("")
etc = Folder("etc")
root.children.append(etc)
etc.children.append(File("passwd"))
etc.children.append(File("groups"))
httpd = Folder("httpd")
etc.children.append(httpd)
httpd.children.append(File("http.conf"))
var = Folder("var")
root.children.append(var)
log = Folder("log")
var.children.append(log)
log.children.append(File("messages"))
log.children.append(File("kernel"))

#The previous is a rather involved way of structuring a filesystem into a tree

#The following does the same thing, but much more easily

#takes a directory, recursively asks walk() to generate a list of all files subordinate to each of its children, and then yields all that data plus its own filename
def walk(file):
    if isinstance(file, Folder):
        yield file.name + "/"
        for f in file.children:
            yield from walk(f)
    else:
        yield file.name

file = "C:/Users/space/Desktop/Packt_Python"
walk(file)

#Coroutines
def tally():
    score = 0
    while True:
        increment = yield score
        score += increment

white_sox = tally()
blue_jays = tally()
next(white_sox)
next(blue_jays)
white_sox.send(3)
blue_jays.send(2)
white_sox.send(2)
blue_jays.send(4)