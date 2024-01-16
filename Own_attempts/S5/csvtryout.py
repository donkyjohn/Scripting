#!/bin/python3

import csv

print("\n Writing to csv files")
with open('/home/guest/_repos/Scripting/Own_attempts/S5/tryout.csv', mode='w') as tryoutfile:
    tryoutwriter = csv.writer(tryoutfile,
    delimiter=';',
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL)
    tryoutwriter.writerow(['Name','Height','Age'])
    tryoutwriter.writerow(['Benjamin','2,03','23'])
    tryoutwriter.writerow(['Potter','1,83','25'])
tryoutfile.close()
with open('/home/guest/_repos/Scripting/Own_attempts/S5/tryout.csv') as csv_file:
    reader = csv.reader(csv_file)
    line = 0
    for row in reader:
        if line == 0:
            print("Collumn names: ")
            print("{0:5s}".format(row[0]))
            line += 1
        elif(line <= 20):
            print("{0:5s}".format(row[0]))
            line += 1
    print("Processed {} lines.".format(line))
csv_file.close()