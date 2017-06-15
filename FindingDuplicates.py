a = [1, 2, 3, 1,]
uniq = []
d = []
for x in a:
    if x not in uniq:
        uniq.append(x)
    else:
        d.append(x)
print(d)
