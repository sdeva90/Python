# the_world_is_flat = False
# if the_world_is_flat:
#     print("Be careful not to fall off!")
# else:
#     print("done")
# print(2 % 9)
# s = 'ha;oshfasfo;sanlvckahdfckas'
# print (len(s))
# a = 0
# b = 1
# while a+b <= 1:
#     print (b, end=',')
# a, b = b, a+b
# def fib(n):
#  a,b = 1,1
#  for i in range(n-1):
#   a,b = b,a+b
#  return a
# print(a)
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))
#        nterms = 10
#        if nterms <= 0:
#            print("Plese enter a positive integer")
#        else:
#            print("Fibonacci sequence:")
#        for i in range(nterms):
#            print(recur_fibo(i))
# Python program to display the Fibonacci sequence up to n-th term using recursive functions
# for i in range(5, 10):
#     print(i)
# a = ['i',' have' , 'a question', 'yet' , 'to' , 'overcome']
# for i in range(len(a)):
#     print(i, a[i])
# list (range(5))
# print(list)
# def fib(n):    # write Fibonacci series up to n
#      """Print a Fibonacci series up to n."""
#      a, b = 0, 1
#      while a < n:
#          print(a, end=', ')
#          a, b = b, a+b
#      print()
# fib(2000)
import sys
import os

things_todo = ['clean', 'play', 'hike', 'movie', 'eat']
things_todo1 = ['clean', 'play', 'hike', 'movie', 'eat']

# things_todo.append('cleanall')
# things_todo.remove('clean')
# things_todo.sort()
# things_todo.reverse()
things_todo.extend('clean')
# del things_todo[2]
print ("things_todo", things_todo)
#
# things_todo2 = things_todo + things_todo1
# print(things_todo2)
