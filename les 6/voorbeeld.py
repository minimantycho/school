def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    kluizen =  infile.readlines()
    return 12 - len(kluizen)

def nieuwe_kluis():
    kluisjes = [1,2,3,4,5,6,7,8,9,10,11,12]
    infile = open('kluizen.txt', 'r')
    kluizen = infile.readlines()
    infile.close()
    for kluis in kluizen:
        kluis = kluis.split(';')
        if(eval(kluis[0]) in kluisjes):
            kluisjes.remove(eval(kluis[0]))

    if(len(kluisjes) != 0):
        code = input('Voor je code in: ')
        outfile = open('kluizen.txt', 'a')
        outfile.write('{};{}\n'.format(kluisjes[0],code))
        outfile.close()
        return 'Je kluisje is nummer: {}'.format(kluisjes[0])
    else:
        return 'Sorry er zijn geen kluisjes beschikbaar!'

def kluis_openen():
    infile = open('kluizen.txt', 'r')
    lines = infile.readlines()
    infile.close()
    nmr = input('Wat is je kluis nummer: ')
    code = input('Wat is je code: ')
    for line in lines:
        line = line.split(';')
        if(nmr == line[0] and code == line[1].strip()):
            return 'Open'
    return 'Wrong credentials!'

def kluis_teruggeven():
    infile = open('kluizen.txt', 'r')
    lines = infile.readlines()
    infile.close()
    nmr = input('Wat is je kluis nummer: ')
    code = input('Wat is je code: ')
    for t in range(len(lines)):
        line = lines[t].split(';')
        if(nmr == line[0] and code == line[1].strip()):
            lines.pop(t)
            outfile = open('kluizen.txt', 'w')
            outfile.writelines(lines)
            outfile.close()
            return 'Kluis {} is weer vrij'.format(line[0])
    return 'Wrong credentials!'

gekozenWaarde = 0

while (gekozenWaarde != 5):
    menu = ('1: Ik wil weten hoeveel kluizen nog vrij zijn','2: Ik wil een nieuwe kluis','3: Ik wil even iets uit mijn kluis halen','4: Ik geef mijn kluis terug','5: Ik wil stoppen')

    for optie in menu:
        print(optie)
    gekozenWaarde = eval(input('Geef een nummer: '))
    if(gekozenWaarde == 1):
        print(toon_aantal_kluizen_vrij())
    elif(gekozenWaarde == 2):
        print(nieuwe_kluis())
    elif(gekozenWaarde == 3):
        print(kluis_openen())
    elif(gekozenWaarde == 4):
        print(kluis_teruggeven())

    print('----------')
