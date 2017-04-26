import sys
import os

things_todo = ['clean', 'play', 'hike', 'movie', 'eat']
things_todo1 = ['clean', 'play', 'hike', 'movie', 'eat']

things_todo.append('cleanall')
things_todo.remove('clean')
things_todo.sort()
things_todo.reverse()
things_todo.extend('eat')
del things_todo[2]
print ("things_todo", things_todo)

things_todo2 = things_todo + things_todo1
print(things_todo2)
