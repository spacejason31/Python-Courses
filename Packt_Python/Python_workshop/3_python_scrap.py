l = [5,8,1,3,2,0]
search_for = 8

result = -1
for i in range(len(l)):
    if search_for == l[i]:
        result = i
        print(search_for, "found at position", result)
        break

l = [2, 3, 5, 8, 11, 12, 18]
search_for = 11

slice_start = 0
slice_end = len(l)-1
found = False
while slice_start<= slice_end and not found:
    location = (slice_start + slice_end) // 2
    print(slice_start, location, slice_end)
    if l[location] == search_for:
        found = True
    else:
        if search_for < l[location]:
            slice_end = location - 1
        else:
            slice_start = location + 1
print(found, location)

names = ['Magda', 'Jose', 'Anne']
lengths = list(map(len, names))

from math import exp
nums = [-3, -5, 1, 4]

list(map(lambda x: 1/(1+exp(-x)), nums))

nums = list(range(1000))
filtered = filter(lambda x: x%3 == 0 or x%7 == 0, nums)

