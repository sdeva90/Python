# 16 month and days calculation
month = input("Please enter a month:")
a = dict()
a = {'jan':'31', 'feb':'na', 'mar':'31', 'apr':'30', 'may':'31', 'jun':'30', 'jul':'31', 'aug':'30', 'sep':'30', 'oct':'31', 'nov':'30', 'dec':'31'}
if month == 'feb':
    year = int(input("enter the year"))
    if year % 4 == 0:
        print("28 days")
    else:
        print("29 days")
else:
    print("# of days is",a['%s' % month])

# same problem using get
month = input("Please enter a month:")
a = dict()
a = {'jan':'31', 'feb':'na', 'mar':'31', 'apr':'30', 'may':'31', 'jun':'30', 'jul':'31', 'aug':'30', 'sep':'30', 'oct':'31', 'nov':'30', 'dec':'31'}
for i in a:
    lookup = a.get(month, 0)
    if lookup == 0:
        print("enter a 3 letter month")
        break
    if month == 'feb':
        year = int(input("enter the year"))
        if year % 4 == 0:
            print("28 days")
            break
        else:
            print("29 days")
            break
    else:
        print("the # of days is",lookup)
        break
