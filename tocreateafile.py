import csv
from random import randint
from math import integer
# import numpy as np
F_name = ["san",
"sou",
"ing",
"asg",
"sand",
"dev",
"tam",
"ven",
"then",
"sar",
"prad",
"vel",
"sam",
"bala",
"haru"
]
F_status = ["Running",
"Jogging",
"vetti",
"Waiting",
"Stopped",
"watching"
]

output = []
f = open('exal.csv', 'w', newline='')
writer = csv.writer(f)
# for id in range(1, 100):
# maxRand = randint(10, 20)
for F_id in range(1, 500):
        outputLine = []
        outputLine.append(str(F_id))
        outputLine.append(F_name[randint(0,14)])
        outputLine.append(F_status[randint(0,5)])
        outputLine.append(str(randint(1, 9)))
        outputLine.append(str(randint(0,99)))
        outputLine.append(str(randint(2000,41943)))
        #outputLine.append(randint[0,1])
        printrow = ', '.join(outputLine)
        output.append(outputLine)
        writer.writerow(outputLine)
