#!/usr/bin/env python


def changeValue(array, old_value, new_value):
    if isinstance(array, list):
        for counter in range(len(array)):
            if isinstance(array[counter], list) or isinstance(array[counter], dict):
                changeValue(array[counter], old_value, new_value)
            elif array[counter] == old_value:
                array[counter] = new_value
    elif isinstance(array, dict):
        for counter, value in array.items():
            if isinstance(value, list) or isinstance(value, dict):
                changeValue(value, old_value, new_value)
            elif value == old_value:
                array[counter] = new_value
    elif array == old_value:
        array = new_value


x = [ [5,2,3], [10,8,9] ]
students = [
             { 'first_name': 'Michael', 'last_name': 'Jordan' },
             { 'first_name': 'John',    'last_name': 'Rosales' }
           ]
sports_directory = {
    'basketball': [ 'Kobe', 'Jordan', 'James', 'Curry'],
    'soccer':     [ 'Messi', 'Ronaldo', 'Rooney' ]
}
z = [ { 'x': 10, 'y': 20 } ]

print(f'Before changeValue: {x}')
changeValue(x, 10, 15)
print(f'After changeValue: {x}')

print(f'Before changeValue: {students}')
changeValue(students, 'Jordan', 'Bryant')
print(f'After changeValue: {students}')

print(f'Before changeValue: {sports_directory}')
changeValue(sports_directory, 'Messi', 'Andres')
print(f'After changeValue: {sports_directory}')

print(f'Before changeValue: {z}')
changeValue(z, 20, 30)
print(f'After changeValue: {z}')
