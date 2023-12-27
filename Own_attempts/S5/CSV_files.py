#!/bin/python3

import csv

# CSV files stands for comma separated values files.
# CSV files are text files that store tabular data.
# CSV files are used to transfer data between programs.

csv.reader('source') # returns a reader object which iterates over lines in the given source.
# options
# delimiter = 'char' # specifies the character used to separate fields.
# quotechar = 'char' # specifies the character used to quote fields containing special characters.
# escapechar = 'char' # specifies the character used to escape the delimiter if quoting is set to QUOTE_NONE.
# dialect = 'dialect' # specifies the dialect of the source.

csv.writer('destination') # returns a writer object which converts the user's data into delimited strings on the given destination.