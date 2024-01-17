#!/bin/python3

import os
import time
from openpyxl import worksheet as ws
import re
import glob
from docx import Document



#write python code to find the genomic.gff file in each subfolder and parse this file line by line. 
#if a match is found with the gene name from input, print the result as output in the terminal
#found gene_name on location where feature=gene | start=XXXX | end=XXXX
print("="*80)
print("This script will parse info for your gene of interest from GFF annotation files.")
gene_name = str(input("Enter gene name: ")) #e.g. gyrB
print("="*80)
print("Getting list of folders in main folder ncbi_datasets...")
time.sleep(1)
location = ("/home/guest/_repos/Scripting/Exam")
location_dir = location + "/ncbi_datasets/"
location_list = os.listdir(location_dir)
emptylist = ""
c = 0
for file in location_list:
  emptylist = emptylist + " " + file
  c += 1
print("Found {} folders: ['{}']".format(c,emptylist))
print("-"*80)
x = 1
d =("-"*80)
counter = 0
document = Document()
iternames = glob.iglob("/home/guest/_repos/Scripting/Exam/**/*.gff",recursive=True)
for filename in iternames:
  print("Parsing GFF file {}: {}".format(x,filename))
  x = x+1
  file = open(filename)
  for i in file.readlines():
    if gene_name in i:
      print(i)
  print(d)
document.save()



    


