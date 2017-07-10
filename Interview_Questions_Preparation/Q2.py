# 2 between sequence
# to create anew list based on teh condition
year = [1945, 1977, 1990, 2001, 2015]
start = 1945
end = 2003
c = []
for i in year:
    if i > start and i < end:
        c.append(i)
print(c)
