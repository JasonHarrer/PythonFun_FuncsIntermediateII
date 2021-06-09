#!/usr/bin/env python

def printInfo(some_dict):
    for key in some_dict.keys():
        array = some_dict[key]
        print(f'{len(array)} {key.upper()}')
        for item in array:
            print(f'{item}')
        print()

dojo = {
           'locations': [
                            'San Jose',
                            'Seattle',
                            'Dallas',
                            'Chicago',
                            'Tulsa',
                            'DC',
                            'Burbank'
                        ],
           'instructors': [
                              'Michael',
                              'Amy',
                              'Eduardo',
                              'Josh',
                              'Graham',
                              'Patrick',
                              'Minh',
                              'Devon'
                          ]
       }

printInfo(dojo)
