# two sum using dict and get
l1 = [1, 3, 4, 5, 7, 9]
ans = 10
a = dict()
c = dict((i,1) for i in l1)
count = 0
for i in l1:
    diff = ans-i
    lookup = c.get((diff), 0)
    if lookup ==1 and diff > i:
        count = count +1
print(count)
