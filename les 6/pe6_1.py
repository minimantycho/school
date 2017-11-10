def maand(nummer):
    if nummer == 12 or nummer == 1 or nummer == 2:
        print('winter')
    elif nummer == 3 or nummer == 4 or nummer == 5:
        print('lente')
    elif nummer == 6 or nummer == 7 or nummer == 8:
        print('zomer')
    elif nummer == 9 or nummer == 10 or nummer == 11:
        print('Herfst')
    else:
        print('Geef een getal binnen de 1 en 12')
maand(eval(input('geef het nummer van de maand: ')))

