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

# options
# csv.QUOTE_MINIMAL # default value, quotes fields containing special characters.
# csv.QUOTE_ALL # quotes all fields.
# csv.QUOTE_NONNUMERIC # quotes all non-numeric fields.
# csv.QUOTE_NONE # does not quote fields containing special characters.

csv.register_dialect('myDialect',
                    delimiter = '|', # this is the character used to separate fields.
                    quoting = csv.QUOTE_ALL, # this specifies the character used to escape the delimiter if quoting is set to QUOTE_NONE.
                    skipinitialspace = True) # this specifies how to interpret whitespace which immediately follows a delimiter.
# this last piece of code registers a dialect with the name 'myDialect' and the specified parameters.