#!/bin/python3

import time

print("\nMonth of year: ", time.strftime("%B"))
print("Week number of year: ", time.strftime("%W"))
print("Day of year: ", time.strftime("%j"))
print("Day of month : ", time.strftime("%d"))
print("Day of week: ", time.strftime("%A")) 


import locale
locale.setlocale(locale.LC_ALL, 'nl_NL') # set locale to Dutch
print("\nMaand van jaar: ", time.strftime("%B"))    # Month of year
print("Dag van week: ", time.strftime("%A"))        # Day of week
print("Weeknummer van jaar: ", time.strftime("%W")) # Week number of year
print("Dag van jaar: ", time.strftime("%j"))        # Day of year
print("Dag van maand: ", time.strftime("%d"))       # Day of month
print("Dag van week: ", time.strftime("%A"))        # Day of week
print("Tijd: ", time.strftime("%X"))                # Time
print("Datum: ", time.strftime("%x"))               # Date
print("Datum en tijd: ", time.strftime("%c"))       # Date and time
print("Tijdzone: ", time.strftime("%Z"))            # Timezone

from datetime import date, timedelta
date_nextweek = date.today() + timedelta(days = 7)
date_min5 = date.today() - timedelta(5)
print('\nCurrent date :', date.today())
print('Date next week :', date_nextweek)
print('Five days before :', date_min5)