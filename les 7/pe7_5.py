dict = {}
def namen():
    while True:
        naam = str(input('geef een voornaam: '))
        if len(naam) == 0:
            print(dict)
            for naam,vaak in dict.items():
                if (vaak == 1):
                    print('Er is 1 student met de naam {}'.format(naam))
                else:
                    print('{} studenten hebben de naam: {}'.format(vaak,naam))

        elif len(naam) > 0:
            if naam in dict:
                dict[naam] += 1
            else:
                dict[naam] = 1

        else:
            print('Er is iets misgegaan')
namen()
