# star display
def printstar(n):
    for i in range(1, n):
        print('*' * i)
    for j in range(n, 0, -1):
        print('*' * j)
printstar(10)

# model type 2 - nested if 
def printstar(n):
    for i in range(1, n):
        for m in range(1, i):
            print('*', end = '')
        print()
    for j in range(n, 0, -1):
        print('*' * j)
printstar(10)
