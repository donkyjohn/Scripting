#!/usr/bin/python3

import sqlite3 as sq
var = sq.connect('taxonomy.db')
c = var.cursor()

try:
    c.execute('''CREATE TABLE ORGANISMS \
              (org_id, latin_name, common_name, tax_id, kingdom, phylum, ordr)''')
except sq.OperationalError:
    print("\nTable organisms already exists\n")

c.execute("INSERT INTO organisms \
          VALUES (1,'Homo sapiens','human', \
          9606,'Metazoa','Chordata','Primates')")
c.execute("INSERT INTO organisms \
           VALUES (2,'Danio rerio','zebrafish', \
           7955,'Metazoa','Chordata','Cypriniformes')")
c.execute("INSERT INTO organisms \
           VALUES (3,'Monosiga brevicollis','choanoflagellate', \
           81824,'','','Choanoflagellida')")
c.execute('''INSERT INTO organisms \
             VALUES(?,?,?,?,?,?,?)''', \
            (4,'Gallus gallus','chicken', 9031,'Metazoa','Chordata','Galliformes'))

insert_id = c.lastrowid
print('last row insert id {}'.format(insert_id))
species = [(5,'Anopheles gambiae','malaria mosquito', 7165,'Metazoa','Arthropoda','Diptera'),
           (6,'Tribolium castaneum','red flour beetle', 7070,'Metazoa','Arthropoda','Coleoptera')
          ]
c.executemany('INSERT INTO organisms VALUES (?,?,?,?,?,?,?)', species)

# Update record
c.execute('''UPDATE organisms SET common_name = ? WHERE tax_id = ? ''', \
         ('African malaria mosquito', 7165))
################################################################################
# Save (commit) changes
conn.commit()
# Close connection when done with it
conn.close()

 