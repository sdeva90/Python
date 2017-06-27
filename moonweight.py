#  Your Weight on the Moon
# If you were standing on the moon right now, your weight would be
# 16.5 percent of what it is on Earth. You can calculate that by multiplying
# your Earth weight by 0.165.
# If you gained a kilo in weight every year for the next 15 years,
# what would your weight be when you visited the moon each year
# and at the end of the 15 years? Write a program using a for loop
# that prints your moon weight for each year.
# 1.withoutusing function
ew = 60
for year in range(1,15):
    ew = ew + 1
    mw = ew * 0.165
    print('year %s = %s' %(year, mw))
# 2. with using function
def weight(ew, inc):
    for year in range(1,16):
        ew = ew + 1
        we = ew + inc
        mw = we * 0.165
        print('year %s = %s' %(year, mw))
#3. using stdin readline
import sys
def weight():
    print("enter your earth weight")
    ew = float(sys.stdin.readline())
    print("enter the weight you increase yearly")
    inc = float(sys.stdin.readline())
    print("please enter the number of years")
    y = int(sys.stdin.readline())
    y = y + 1
    for year in range(1, y):
        ew = ew + inc
        weight = ew * 0.165
        print('year %s = %s ' %(year, weight))
