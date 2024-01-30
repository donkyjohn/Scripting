#!/bin/python3

import MySQLdb as my
import MySQLdb as my
print("="*80)
print("\nThis script will look for Pfam hits of interest in the mouse genome")
print("="*80)





result = [] 
while True:
      search_term = input("Enter a Pfam search term or type 0 to stop: ")
      if search_term == "0":
            break
      result.append(search_term)
print(result)

db = my.connect(host="genome-mysql.soe.ucsc.edu",
                        user="genomep",
                        passwd="password",
                        db="mm39")

c = db.cursor()
c.execute("SELECT * FROM ucscGenePfam")
result2 = c.fetchall()
print(result2)

# Check for matches
matches = []
for item in result:
      for row in result2:
            if item in row:
                  matches.append(row)
                  break

print(matches)

