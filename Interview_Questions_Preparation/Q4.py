# 4 dictionaries counting using get function
l1 = [1, 2, 3, 3, 5]
l2 = [3, 3, 4, 9]
l = l1 + l2
a = {}
for i in l:
    a[i] = a.get(i,0) + 1
for key, value in a.items():
    print(key, value)
