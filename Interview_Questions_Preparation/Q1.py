# 1 order sequence
# Arranging the given set of numbers in an order
list1 = [-1, 0, 15]
start = l[0]
end = l[len(l)-1]
result = []
for i in range(start,end+1):
    if start <= end:
        result.append(start)
        start = start+1
print(result)
