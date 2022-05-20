#Big O notation:
#O(1) Constant time
def getFirst(myList):
    return myList[0]
#O(n) Linear time
def getSum(myList):
    sum = 0
    for item in myList:
        sum += item
    return sum
#O(n^2) Quadratic time
def getSum(myList):
    sum = 0
    for row in myList:
        for item in row:
            sum += item
    return sum
#O(log(n)) Logarithmic time
def searchBinary(myList, item):
    first = 0
    last = len(myList) - 1
    foundFlag = False
    while(first<=last and not foundFlag):
        mid = (first + last)//2
        if myList[mid] == item:
            foundFlag = True
        else:
            if item <= myList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return foundFlag
