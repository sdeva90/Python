#1
#company = ['apple', 'google', 'drastin', 'linkedin', 'google', 'drastin']
#mynewlist = list(company)
#print(mynewlist)

#2
#company = ['apple', 'google', 'drastin', 'linkedin', 'google', 'drastin']
#if company[1] == company[4]:
#del company[4]
#else:
#    print(company)

#3
# company = ['apple', 'google', 'drastin', 'linkedin', 'google', 'drastin']
# b = []
# for i in company:
#   if i not in b:
#         b.append(i)
# print ("unique list is :", b)

# company = ['apple', 'google', 'drastin', 'linkedin', 'google', 'drastin', 'None']
# # b = []
# # for i in company:
# #     if i not in b:
# #         b.append(i)
# # print ("unique list is :", b)
# previous = None
# count = 1
# for j in company:
#     if j == previous:
#         count +=1
#     else:
#         count = 1
#         previous = j
# # return count
# print (count)
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
