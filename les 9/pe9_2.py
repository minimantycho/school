import datetime
import csv

with open('inloggers.csv','w', newline='') as MyCVSFile:
    writer = csv.writer(MyCVSFile, delimiter=';')
    # for gegevens in writer:
    while True:
        naam = input('wat is je naam? ')
        if naam == 'einde':
            break
        voorl = input('wat zijn je voorletters? ')
        gbdatum = input('wat is je geboortedatum? ')
        email = input('wat is je e-mail adres? ')

        writer.writerow((voorl,naam,gbdatum,email))