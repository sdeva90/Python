import csv
# import numpy as np
colvalues = ["Home to Work",
"Work to Home",
"Origin - Home",
"Origin - Work",
"Origin - Shop",
"Origin - Education",
"Origin - Tourist",
"Origin - Hotel",
"Origin - Other",
"Origin - Not Given",
"Destination - Home",
"Destination - Work",
"Destination - Shop",
"Destination - Education",
"Destination - Tourist",
"Destination - Hotel",
"Destination - Other",
"Destination - Not Given"]

output = []
f = open('output.csv', 'w', newline='')
writer = csv.writer(f)
with open('inputfile.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        for x in range(0, 18):
            # print(x)
            outputLine = []
            outputLine.append(row[0]);
            outputLine.append(row[1]);
            outputLine.append(row[2]);
            outputLine.append(row[3]);
            outputLine.append(colvalues[x])
            # print(colvalues[x])
            outputLine.append(row[5 + x])

            # printrow = ', '.join(outputLine)
            output.append(outputLine)
            writer.writerow(outputLine)

print(len(output))
