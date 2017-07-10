# dict diff checker
# 1. create dict
# 2. insert values(i) in dict
# 3. get diff b\w sum and each element in list1
# 4. lookup teh diff in dict
# 5. if yes, print diff, i
# 6
l1 = [1, 2, 3, 5, 9, 9, 11]
ans = 5
a = dict()
c = dict((i, 1) for i in l1)
for i in l1:
    diff = ans-i
    lookup = c.get((diff), 0)
    if lookup ==1 and diff > i:
        print(diff, i)
