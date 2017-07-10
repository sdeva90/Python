#7 value increment if teh key is repeating in a list
l1 = [1, 2, 3, 5, 9, 9, 11]
ans = 5
a = dict()
for i in l1:
    lookup = a.get(i, 0)
    lookup +=1
    a[i] = lookup
print(a)

# Model 2 of same type
string = ['sa', 're', 'ga', 'ma', 'pa', 'tha', 'ne', 'sa', 'sa', 're']
# ans = 5
a = dict()
for i in string:
    lookup = a.get(i, 0)
    lookup +=1
    a[i] = lookup
print(a)
