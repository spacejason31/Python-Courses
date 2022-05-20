cubes = []
for x in [1,2,3,4,5]:
    cubes.append(x**3)                  #too wordy
cubes
cubed = [x**3 for x in [1,2,3,4,5]]     #better
cubed
cube = [x**3 for x in range(1,6)]       #pythonic (aka best)
cube
names = ['Graham Chapman', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']
print([name.upper() for name in names if name.startswith("T")])

print([x*y for x in ['spam', 'eggs', 'chips'] for y in [1,2,3]])
print([x*y for x in [1,2,3] for y in ['spam', 'eggs', 'chips']])

names = ['Magnus Carlsen', 'Fabiano Caruana', 'Yifan Hou', 'Wenjun Ju']
fixtures = [f"{x} vs. {y}" for x in names for y in names if x!= y]
fixtures

print([a+b for a in [0,1,2,3] for b in [4,3,2,1]])
print({a+b for a in [0,1,2,3] for b in [4,3,2,1]})
list({a+b for a in [0,1,2,3] for b in [4,3,2,1]})

names = ['Eric', 'Graham', 'Terry', 'John', 'Terry']
print({k:len(k) for k in names})

names = ['Vivian', 'Rachael', 'Tom', 'Adrian']
test = [70, 82, 80, 79]
scores = {names[i]:test[i] for i in range(0,4)}
scores

#Exercise 103
john = { 'first_name':'John', 'surname':'Cleese'}
john['middle_name']
from collections import defaultdict
safe_john = defaultdict(str, john)
print(safe_john['middle_name'])
courses = defaultdict(lambda: 'No!')
courses['Java'] = 'This is Java'
print(courses['Python'])
print(courses['Java'])

#Exercise 104
from collections import defaultdict
class Interrogator:
    def __init__(self, questions):
        self.questions = questions
    def __iter__(self):
        return self.questions.__iter__()

questions = ["What is your name?", "What is your quest?", "What is the average airspeed velociy of an unladen swallow?"]
awkward_person = Interrogator(questions)
for question in awkward_person:
    print(question)

#Exercise 105
class PrimesBelow:
    def __init__(self, bound):
        self.candidate_numbers = list(range(2,bound))
    def __iter__(self):
        return self
    def __next__(self):
        if len(self.candidate_numbers) == 0:
            raise StopIteration
        next_prime = self.candidate_numbers[0]
        self.candidate_numbers = [x for x in self.candidate_numbers if x % next_prime != 0]
        return next_prime
primes_to_a_hundred = [prime for prime in PrimesBelow(100)]
print(primes_to_a_hundred)
primes_hundredThousand = [prime for prime in PrimesBelow(110000)]
print(primes_hundredThousand)
primes_under_five = iter(PrimesBelow(5))
next(primes_under_five)

#Exercise 107
class Primes:
    def __init__(self):
        self.current = 2
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            current = self.current
            square_root = int(current ** 0.5)
            is_prime = True
            if square_root >=2:
                for i in range(2, square_root + 1):
                    if current % i == 0:
                        is_prime = False
                        break
            self.current += 1
            if is_prime:
                return current

[p for p in Primes() if p <= 100]
import itertools
print([p for p in itertools.takewhile(lambda x: x<100, Primes())])

#Exercise 108
import itertools
players = ['White', 'Black']
turns = itertools.cycle(players)
countdown = itertools.count(10,-1)
print([turn for turn in itertools.takewhile(lambda x: next(countdown)>0, turns)])

#Exercise 109
def primes_below(bound):
    candidates = list(range(2,bound))
    while(len(candidates) > 0):
        yield candidates[0]
        candidates = [c for c in candidates if c % candidates[0] != 0]

#Activity 20
import random
import math
import numpy
import matplotlib.pyplot as plt
def pi_finder(num_pt):
    circle_num = 0
    total_num = 0
    pi_est = []
    for i in range(num_pt):
        x = random.random()
        y = random.random()
        hyp = math.sqrt((x**2)+(y**2))
        total_num += 1
        if hyp<1:
            circle_num += 1
        if (total_num != 0) & ((total_num % 1000) == 0):
            est = 4 * circle_num / total_num
            pi_est.append(est)
    return pi_est
est = pi_finder(100000)
plt.plot(est, 'r--')
plt.plot([0,len(est)], [math.pi,math.pi])
plt.show()

#Exercise 110
import re
title = "And now for something completely different"
pattern = "(\w)\\1+"
print(re.search(pattern, title))

#Exercise 111
import re
description = "The Norwegian Blue is a wonderful parrot. This parrot is notable for its exquisite plumage"
pattern = "(parrot)"
replacement = "ex-\\1"
print(re.sub(pattern, replacement, description))

#Activity 21
import re
customers = ['Xander Harris', 'Jennifer Smith', 'Timothy Jones', 'Amy Alexandrescu', 'Peter Price', 'Weifung Xu']
winners = [name for name in customers if re.search("[Xx]", name)]