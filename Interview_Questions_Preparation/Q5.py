# 5 dict operations, all other opeartions tested here
a = dict()
a['san'] = 10
a['sou'] = 2
lookup = a.get('san', 0)
a['san'] = lookup + 3
delete = a.pop('sou')
numele = len(a)
a['san'] = 15
print(delete)
