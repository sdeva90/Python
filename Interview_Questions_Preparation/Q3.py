# To convert teh list to dict and printing teh key value pair
# 3 dictionaries
l1 = [1, 2, 3, 3, 5]
l2 = [3, 3, 4, 9]
l = l1 + l2
a = {}
for i in l:
    a[i] = 0
for key, value in a.items():
    print(key)
