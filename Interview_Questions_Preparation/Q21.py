# to return the list from interger number
import math
def solution(input):
    # method1
    n = input
    l = [int(i) for i in str(n)]
    # return(l)
    # method 2
    l2 = []
    while n>0:
        m = math.floor(n%10)
        l2.append(m)
        n = math.floor(n/10)
    l2.reverse()
    # print(l2)
    return l2

assert solution(123) == [1,2,3]
