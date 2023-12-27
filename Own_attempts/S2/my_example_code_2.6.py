#!/bin/python3

dnt = {
    "A": "adenine",
    "C": "cytosine",
    "G": "guanine",
    "T": "thymine"
}

print("key c has value", dnt["C"])
print("key A has value {}".format(dnt["A"]))

#####################################

list = {}
list["A"] = "adenine"
list["C"] = "cytosine"
list["G"] = "guanine"
my_list = {}
my_list["T"] = "thymine"
print("list", my_list)

#####################################

my_dict = dict(zip(["A", "C", "G", "T"], ["adenine", "cytosine", "guanine", "thymine"]))
print("dict", my_dict)

#####################################

var1 = dict(zip(["name", "job", "age"], ["Benjamin", "student", 23]))
var2 = dict(zip(["name", "job", "age"], ["Iris", "student", 21]))
print("The name of the first person is {} and the name of the other person is {}. They are both {} but {} is {} years old and {} is {} years old.".format(var1['name'], var2['name'], var1['job'], var1['name'], var1['age'], var2['name'], var2['age']))

#####################################

nested = {'name' : { 
    'firstname' : 'Benjamin', 
    'lastname' : 'Hoerée' 
    }, 'jobs' : ['student', 'dj'],
    'age' : 23
    } 

# 'name' is a dictionary
# 'jobs' is a list

jobs_str = ' and '.join(nested['jobs'])
print("{}'s jobs are {} and he is {} years old".format(nested['name']['firstname'], jobs_str, nested['age']))

nested['name']['firstname'] = 'Benjamin'
nested['name']['lastname'] = 'Hoeree'
nested['jobs'] = ['student', 'dj']  
nested['age'] = 23

print("Benjamin's last name is {}".format(nested['name']['lastname']))
Keys = list(nested.keys())