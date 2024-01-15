#!/bin/python3

import csv

with open('/home/guest/_repos/Scripting/S5_Filesystem_reading_writing_files/urine.csv') as csv.file:
    csv_reader = csv.reader(csv.file, delimiter=',')
    count = 0
    for row in csv_reader:
        if count == 0:
            print("Column names are:")
            print("{0:5s} | {1:5s} | {2:10s}".format(row[0], row[1], row[2]))
            count += 1
        elif(count <= 20):
            print("{0:5s} | {1:5s} | {2:10s}".format(row[0], row[1], row[2]))
            count += 1
    print("Processed {} lines.".format(count))
    csv.file.close()      

with open('/home/guest/_repos/Scripting/S5_Filesystem_reading_writing_files/urine.csv', mode='r') as csvfile2:
    csvreader = csv.DictReader(csvfile2)
    count2 = 0  
    for row in csvreader:
        if(count<=5):
            print("{0:5s} | {1:5s} | {2:10s}".format(row[""], row["r"], row["gravity"]))
            count2 += 1
    print("Processed {} lines.".format(count2))
csvfile2.close()

with open('/home/guest/_repos/Scripting/Own_attempts/S5/pers.csv', mode='w') as pers_file:
    pers_writer = csv.writer(pers_file, 
    delimiter=';', # default is ',' this is the character used to separate fields.
    quotechar='"', # default is '"' this is the character used to quote fields containing special characters.
    quoting=csv.QUOTE_MINIMAL) # default is QUOTE_MINIMAL this specifies the character used to escape the delimiter if quoting is set to QUOTE_NONE.
    pers_writer.writerow(['John Snow', '1,73', '32'])
    pers_writer.writerow(['Arya Stark', '1,55', '21'])
    pers_writer.writerow(['Daenerys Targaryen', '1,57', '32'])
pers_file.close()


