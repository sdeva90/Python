# 15alphanumeric counting
def tofind(x):
    alpha = 0
    num = 0
    for i in x:
        if i.isalpha():
            alpha +=1
        elif i.isnumeric():
                num += 1
        else:
            print("invalid")
            return
    print("number of letter:", alpha)
    print("Count of number:", num)
x = input()
tofind(x)
