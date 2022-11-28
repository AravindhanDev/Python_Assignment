from array import *

def getArraySum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

arr = array('i', [12, 23, 34, 45, 56])
sumResult = getArraySum(arr)
print(f'sum {sumResult}')