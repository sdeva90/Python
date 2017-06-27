# program to understand stdin.readline() function and module system
import sys
def sillyage():
    print("how old are you")
    age = int(sys.stdin.readline())
    if age == 3:
        print("i'm child")
    elif age == 40:
        print("I'm adult")
    else:
        print("I'm none")
