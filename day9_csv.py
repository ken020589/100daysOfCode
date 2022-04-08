##!/usr/bin/env python
#day9 csv

from unicodedata import name
import csv
import keyboard

name = input('your name: ')
height = float(input('your height: '))
weight = float(input('your weight: '))
with open('test.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'height', 'weight']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({'name': name, 'height': height, 'weight': weight})
        
        