

def getSum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum

y = 0
for x in range(1,1000000):
    if x % getSum(x) == 0:
        print(x-y)
        y = x