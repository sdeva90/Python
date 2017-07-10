#11 string listing - playing with string
l1 = ['john', 'joe', 'mary']
l2 = ['Asian', 'mexican','italian']
l3 = ['briyani', 'idly', 'dosa']
l4 = ['quesdila', 'gucamoley', 'taquila']
l5 = ['pasta', 'pizza', 'sasuage']
l6 = [l3, l4, l5]
if len(l1) != len(l2):
    print("list unordered")

for n in range(0, len(l1)):
    l7 = l6[n]
