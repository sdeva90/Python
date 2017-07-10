# to finf teh length of last character in teh string
def findtext(sample):
    length = 0
    reset  = 0
    for i in sample:
        if i == ' ':
            reset = 1
        elif reset == 1:
            length = 1
            reset  = 0
        else:
            length = length +1
    return length

sample = " san i doing "
n = findtext(sample)
print(n)
