personen = eval(input('met hoeveel personen gaan jullie? '))
def geld(personen):
    # for error in geld(personen = input('met hoeveel personen gaan jullie? ')):
    try:
        hoeveel_pp = 4328/personen
        print(hoeveel_pp)
    except NameError:
        print('geef het getal in cijfer')
    except ZeroDivisionError:
        print('kan niet delen door 0')
    except personen < 0:
        print('Negatieve getallen niet toegestaan')
geld(personen)

