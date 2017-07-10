# elemnet avialble or not in Tuple
# to check teh element avilable in tuple
def elementin_tuple(a):
    t = ('1', '2', '3', '4', '5')
    if a in t:
        print("It is there already")
    else:
        print("It is a new number")

a = input("enter the number:")
elementin_tuple(a)
