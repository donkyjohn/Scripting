#!/bin/python3

import filecmp

# filecmp() module provides functions to compare files and directories, and filecmp.cmp() is the most commonly used function.

# filecmp.cmp(path to file1, path to file2) 
# compares the files named f1 and f2, returning True if they seem equal, False otherwise. 

# filecmp.clear_cache() 
# clears the filecmp cache, which contains the results of the comparison of directory contents.

# filecmp.cmpfiles(path to dir1, path to dir2, list of filenames) 
# compares the files named in list of filenames, returning three lists of filenames: match, mismatch, and errors. match contains the list of files that match, mismatch contains the names of those that don’t, and errors lists the names of files which could not be compared.

# filecmp.dircmp(path to dir1, path to dir2, hidenames) 
# compares the directories dir1 and dir2, returning a dircmp object that represents the difference between the two directories. hidenames is a list of names to be ignored, defaults to ['RCS', 'CVS', 'tags']. 
# The dircmp object has the following methods: 
# dircmp.report()
# prints a report on the differences between the directories.
# dircmp.report_partial_closure()
# prints a report on the differences between the directories, and reports on common immediate subdirectories.
# dircmp.report_full_closure()
# prints a report on the differences between the directories, and reports on recursively found common subdirectories.
# dircmp.left_list, dircmp.right_list
# the lists of files and subdirectories in dir1 and dir2.
# dircmp.common
# the list of files and subdirectories common to both dir1 and dir2.
# dircmp.left_only, dircmp.right_only
# the lists of files and subdirectories that are in dir1 but not dir2, and vice versa.


