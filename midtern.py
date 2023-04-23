import random
def linear_Search(array, n, x):
    countline = 0
    for i in range(0, n):
        countline += 1
        if (array[i] == x):
            return countline
    return countline
def binary_search(array, x):
    countbinary = 0
    low = 0
    upper = len(array) - 1
    while low <= upper:
        countbinary += 1
        mid = (low + upper) // 2  
        if array[mid] < x:    
            low = mid + 1
        elif array[mid] > x:  
            upper = mid - 1
        else:                    
            return countbinary
    return countbinary

def fibonacci_search(array,x):
    size = len(array)
    countfibo = 0
    start = -1
    f0 = 0
    f1 = 1
    f2 = 1
    while(f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
    while(f2 > 1):
        countfibo += 1
        index = min(start + f0, size - 1)
        if array[index] < x:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif array[index] > x:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (array[size - 1] == x):
        return countfibo
    return countfibo
countbinary = 0
countline = 0
countfibo = 0
num = int(input("給我一個數(n)決定陣列大小:"))
for i in range(100):
    x = random.randint(1,10000)
    array=[]
    for i in range(num):
        b = random.randint(1,10000)
        array.append(b)
    n = len(array)
    countline += linear_Search(array, n, x)
    countbinary += binary_search(array, x)
    countfibo += fibonacci_search(array,x)
meancountline = countline/100
meancountbinary = countbinary/100
meancountfibo = countfibo/100
#print(array)
#print(x)
print("mean execution time for linear_Search : ", meancountline) # O(n)
print("mean execution time for binary_Search : ", meancountbinary) #O(logn)
print("mean execution time for fibonacci_Search : ", meancountfibo) #O(logn)