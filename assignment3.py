#!/usr/bin/env python


def iterateDictionary2(key, array):
    for row in array:
        if key in row:
            print(f'{row[key]}')


students = [
               {'first_name': 'Michael', 'last_name': 'Jordan'},
               {'first_name': 'John', 'last_name': 'Rosales'},
               {'first_name': 'Mark', 'last_name': 'Guillen'},
               {'first_name': 'KB', 'last_name': 'Tonel'}
           ]


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
