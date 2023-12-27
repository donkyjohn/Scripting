#!/bin/python3
import kladblok

x = kladblok.greet("Benjamin")
print(x)

bobber = kladblok.list["name"]
bobber2 = kladblok.list["alias"]
bobber3 = kladblok.list["organism"]
bobber4 = kladblok.list["symbol"]

print("The name is {}, the alias is {}, the organism is {}, and the symbol is {}.".format(bobber, bobber2, bobber3, bobber4))

import time

time.time()
print(time.time())

x = time.strftime("%d/%m/%Y\t%Hh%Mm%Ss")
print(x)

time.localtime()
print(time.localtime())

timetuple = time.localtime(time.time())
print("It's been {} hours since it was midnight.".format(timetuple.tm_hour))

hoursmin = str(timetuple.tm_hour) + "h" + str(timetuple.tm_min) + "m"
print(hoursmin)

#print("sleeping for 5 seconds...")
#time.sleep(5)
#print("done sleeping")  

for i in zip((1,4,7), (2,5,8), (3,6,9)):
    print(i)
