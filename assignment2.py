#!/usr/bin/env python


def iterateDictionary(array):

    for row in array:
        a = []
        s = ''
        for key in row.keys():
            if s == '':
                s = ''.join([key, ' - ', row[key]])
            else:
                s = ''.join([s, ', ', key, ' - ', row[key]])
        print(s)

students = [
               {'first_name': 'Michael', 'last_name': 'Jordan'},
               {'first_name': 'John', 'last_name': 'Rosales'},
               {'first_name': 'Mark', 'last_name': 'Guillen'},
               {'first_name': 'KB', 'last_name': 'Tonel'}
           ]

iterateDictionary(students)
