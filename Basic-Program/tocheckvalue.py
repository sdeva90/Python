# Program to check the given value is there in the List or not.
value = ['apple', 'orange', 'guava', 'pine' ]
givevalue = input(" Please Enter your value: ")
a = str(givevalue)
if a in value:
    print("found")
else:
    print("not found")
