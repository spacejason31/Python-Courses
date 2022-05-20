import random
rand = list(i for i in range(100))
random.shuffle(rand)

def BubbleSort(list):
    lastElementIndex = len(list) - 1
    for passNo in range(lastElementIndex, 0, -1):
        for idx in range(passNo):
            if list[idx] > list[idx+1]:
                list[idx], list[idx+1] = list[idx+1], list[idx]
    return list

def InsertionSort(list):
    for i in range(1, len(list)):
        j = i-1
        element_next = list[i]

        while (list[j] > element_next) and (j >= 0):
            list[j+1] = list[j]
            j=j-1
        list[j+1] = element_next
        print(list)
    return list

list1 = [25, 26, 22, 24, 27, 23, 21]
list_sort = InsertionSort(list1)
print(list1)    #note: despite assigning the sort function to a variable, the original list is still sorted as well
print(list_sort)

def MergeSort(list):
    if len(list)>1:
        mid = len(list)//2  #splits list in half
        left = list[:mid]
        right = list[mid:]

        MergeSort(left)     #repeats until length of list is 1
        MergeSort(right)

        a = 0
        b = 0
        c = 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c]=left[a]
                a += 1
            else:
                list[c]=right[b]
                b += 1
            c += 1
        while a < len(left):
            list[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            list[c] = right[b]
            b += 1
            c += 1
    return list

list3 = [44, 16, 83, 7, 67, 2, 34, 45, 10]
MergeSort(list3)

def ShellSort(list):
    distance = len(list) // 2
    while distance > 0:
        for i in range(distance, len(list)):
            temp = list[i]
            j = i
        # Sort the sub list for this distance
            while j >= distance and list[j - distance] > temp:
               list[j] = list[j - distance]
               j = j-distance
            list[j] = temp
        # Reduce the distance for the next element
        distance = distance//2
    return list

list4 = [26, 17, 20, 11, 23, 21, 13, 18, 24, 14, 12, 22, 16, 15, 19, 25]
ShellSort(list4)

def SelectionSort(list):
    for fill_slot in range(len(list) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if list[location] > list[max_index]:
                max_index = location
        list[fill_slot],list[max_index] = list[max_index],list[fill_slot]
    return list

list5 = [70, 15, 25, 19, 34, 44]
SelectionSort(list5)