for tafel in range(1,11):
    for vermenigvuldiging in range(1,11):
        antwoord = tafel * vermenigvuldiging
        print('{:2} {:2} {:2} {:2} {:2}'.format(tafel,'*',vermenigvuldiging, '=', antwoord), end=', ')
    print()