#12 maths counting
def counting(l1):
    counte=0
    counto=0
    for i in l1:
        if i%2==0:
            counte +=1
        else:
            counto +=1
    print(counte)
    print(counto)

# model type 2
def main():
    n = input()
    b = int(n)
    c = []
    for i in range(0, b):
        l1 = input()
        a = int(l1)
        c.append(a)
    print(c)
    # l1 = list(input("enter the number:"))
    counting(c)
if __name__ == "__main__":
    main()
