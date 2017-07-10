# tuples removing duplicates string/integer
def dupintup(x):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    t1 = tuple(b)
    print(t1)

a = [1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 9]
dupintup(a)

# example 2
def dupintup(x):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    t1 = tuple(b)
    print(t1)

a = ['temple', 'run', 'temple', 'run']
dupintup(a)
