# to find the subset using dict
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3]
d = dict()
count = 0
for i in l1:
    d[i] = 1
for j in l2:
    lookup = d.get(j,0)
    if lookup == 0 or lookup != 1:
        print('not a subset')
        break
    elif lookup == 1:
        count = count + 1
if count == len(l2):
    print("subset")
