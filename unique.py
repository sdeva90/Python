
c = ['apple', 'google', 'drastin', 'linkedin', 'google', 'drastin', 'jo', 'jo', 'jo']
repeated = []
previous = None
count = 0
for item in c:
    if item == previous and item not in repeated:
        count += 1
        repeated.append(item)
    else:
        repeated = []
    previous = item
print (count)
print (item)
print (repeated)
