import csv

with open('gamers.csv', 'r', newline='') as csv_file:
    csv_writer = csv.reader(csv_file, delimiter=';')
    lst = []
    for row in csv_writer:
        print(row[0], 'heeft', row[2], 'punten gehaald op', row[1])
        lst.append(row[2])
    grootste = max(lst)
print('de hoogst gehaalde score is:', grootste)