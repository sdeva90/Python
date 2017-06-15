# To get the distinct list
c = ['apple', 'google', 'drastin', 'linkedin', 'google', 'drastin', 'jo', 'jo', 'jo']
uniq = []
for x in c:
    if x not in uniq:
        uniq.append(x)
print(uniq)
