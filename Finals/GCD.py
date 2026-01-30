from math import gcd

c = int(input())  # Task number
n = int(input())  # Number of integers
numbers = []

for _ in range(n):
    num = int(input())
    numbers.append(num)

if c == 1:
    greatestCD = 1
    for x in range(n):
        if x == 0:
            greatestCD = gcd(numbers[x], numbers[x + 1])
        elif x > 0 and x < n - 1:
            greatestCD = gcd(greatestCD, numbers[x + 1])
    print(greatestCD)        
        
elif c == 2:
    greatestCD = 1
    for y in range(n):
        maxgcd = 1
        elementRemoved = numbers[y]
        numbers.remove(elementRemoved)
        for z in range(n - 1):
            if z == 0:
                greatestCD = gcd(numbers[z], numbers[z + 1])
            elif z > 0 and z < n - 2:
                greatestCD = gcd(greatestCD, numbers[z + 1])
            
            if greatestCD > maxgcd:
                maxgcd = greatestCD
        numbers.insert(y, elementRemoved)
    print(maxgcd)    

