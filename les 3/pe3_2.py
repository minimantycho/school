#opdracht 3
leeftijd = int(input('Hoe oud ben je? '))
paspoort = str(input('Heb je een nederlands paspoort? '))

if leeftijd > 18 and paspoort == 'ja':
    print('Dan mag je stemmen!')

else:
    print('Helaas, je mag niet stemmen')

