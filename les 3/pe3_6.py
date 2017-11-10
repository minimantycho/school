s = 'Guido van Rossum heeft programmeertaal Python bedacht.'
klinkers = ['a','e','i','o','u']
for char in s:
    if klinkers.count(char) == 1:
        print(char)