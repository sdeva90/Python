import csv
from random import randint
# import numpy as np
process_name = ["sshd",
"atd",
"crond",
"dbus-daemon",
"udevd",
"hald",
"init",
"System",
"svchost",
"lsm",
"hashdeep",
"logon",
"java",
"hald-runner",
"xinetd"
]
process_status = ["Running",
"zombie",
"IO",
"Waiting",
"Stopped"]

output = []
f = open('process.csv', 'w', newline='')
writer = csv.writer(f)
for machine_id in range(1, 10000):
    maxRand = randint(10, 20)
    for process_id in range(1, maxRand):
        outputLine = []
        outputLine.append(str(machine_id))
        outputLine.append(process_name[randint(0,14)])
        outputLine.append(process_status[randint(0,4)])
        outputLine.append(str(randint(0,99)))
        outputLine.append(str(randint(0,99)))
        outputLine.append(str(randint(2000,4194304)))
        #outputLine.append(randint[0,1])
        printrow = ', '.join(outputLine)
        output.append(outputLine)
        writer.writerow(outputLine)
