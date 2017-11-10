# def hello2():
#     while True:
#         name = input('What is your name?: ')
#         print('Hallo {}'.format(name))
# hello2()

# def befor0(table):
#     for row in table:
#         for num in row:
#             if num == 0:
#                 break
#             print(num,end=' ')
#         print()
# table = [[2,3,0,6],[0,3,4,5],[4,5,6,0]]
# # befor0(table)
#
# def ignore0(table):
#     for row in table:
#         for num in row:
#             if num == 0:
#                 continue
#             print(num,end=' ')
#         print()
# ignore0(table)

# employee = {'272-82-9319':['Tycho','Aster'],'321-42-5353':['miel', 'Evy'],'312-65-2523':['Gjalt','Mies']}
# employee['272-82-9319'] = 'Holden Catfield'
# employee['272-82-9319'] = 'Holden Cautfield'
# print(employee)

phonebook = {('Anna','Karenina'):'(123)456-78-90',('Yu','Tsun'):'(901)234-56-78',('Hans', 'Castorp'):'(321)908-76-54'}
def lookup(phonebook):
    while True:
        naam = input('Enter the first name: ')
        achternaam = input('Enter the last name: ')
        person = (naam,achternaam)
        if person in phonebook:
            print(phonebook[person])
lookup(phonebook)