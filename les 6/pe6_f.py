def toon_aantal_kluizen_vrij():
    bestand = open('kluizen.txt', 'r')
    kluizen =  bestand.readlines()
    return 12 - len(kluizen)

def kluis_open():
    bestand = open('kluizen.txt', 'r')
    lines = bestand.readlines()
    bestand.close()
    nmr = input('Wat is je kluis nummer: ')
    code = input('Wat is je code: ')
    for line in lines:
        line = line.split(';')
        if(nmr == line[0] and code == line[1].strip()):
            return 'je kluis is open'
    return 'Verkeerde wachtwoord gegeven'

def nieuwe_kluis():
    kluisjes = [1,2,3,4,5,6,7,8,9,10,11,12]
    bestand = open('kluizen.txt', 'r')
    kluizen = bestand.readlines()
    bestand.close()
    for kluis in kluizen:
        kluis = kluis.split(';')
        if(eval(kluis[0]) in kluisjes):
            kluisjes.remove(eval(kluis[0]))

    if(len(kluisjes) != 0):
        code = input('Voor een wachtwoord in: ')
        schrijven = open('kluizen.txt', 'a')
        schrijven.write('{};{}\n'.format(kluisjes[0],code))
        schrijven.close()
        return 'Je krijgt kluisje: {}'.format(kluisjes[0])
    else:
        return 'Alle kluisjes zijn bezet'

def kluis_terug():
    bestand = open('kluizen.txt', 'r')
    lines = bestand.readlines()
    bestand.close()
    nummer = input('Welk nummer heeft je kluisje?: ')
    code = input('Wat is het wachtwoord?: ')
    for x in range(len(lines)):
        line = lines[x].split(';')
        if(nummer == line[0] and code == line[1].strip()):
            lines.pop(x)
            outfile = open('kluizen.txt', 'w')
            outfile.writelines(lines)
            outfile.close()
            return 'Kluisje {} is weer vrij'.format(line[0])
    return 'verkeerde wachtwoord!'

gekozen_Waarde = 0

while (gekozen_Waarde != 5):
    menu = ('1: Ik wil weten hoeveel kluizen nog vrij zijn','2: Ik wil een nieuwe kluis','3: Ik wil even iets uit mijn kluis halen','4: Ik geef mijn kluis terug','5: Ik wil stoppen')

    for optie in menu:
        print(optie)
    gekozen_Waarde = eval(input('Geef een nummer: '))
    if(gekozen_Waarde == 1):
        print(toon_aantal_kluizen_vrij())
    elif(gekozen_Waarde == 2):
        print(nieuwe_kluis())
    elif(gekozen_Waarde == 3):
        print(kluis_open())
    elif(gekozen_Waarde == 4):
        print(kluis_terug())

    print('----------')




