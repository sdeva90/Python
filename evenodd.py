# for num in range(2, 10):
#      if num % 2 == 0:
#          print("Found an even number", num)
#          continue
#      print("Found a number", num)


import sys
def Factorial(n): # return factorial
    result = 1
    for i in range (1,n):
        result = result * i
    print "factorial is ",result
    return result
print Factorial(10)
