#!/bin/python3

import MySQLdb as my
print("="*80)
print("\nThis script will look for Pfam hits of interest in the mouse genome")
print("="*80)





result = [] 
while input("Enter a Pfam search term or type 0 to stop: ") != "0":
      result.append(input("Enter a Pfam search term or type 0 to stop: "))
print(result)

'''

db = my.connect(host="genome-mysql.soe.ucsc.edu",
                user="genomep",
                passwd="password",
                db="mm39")
c = db.cursor()
var = c.execute("""SELECT * FROM ucscGenePfam """)
print(c.fetchall())

'''