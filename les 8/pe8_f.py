stations = ['Schagen','Heerhugowaard','Alkmaar','Castricum','Zaandam','Amsterdam Sloterdijk','Amsterdam Centraal','Amsterdam Amstel',
            'Utrecht Centraal','\'s-Hertogenbosch','Eindhoven','Weert','Roermond','Sittard','Maastricht']


def inlezen_beginstation(stations):
    while True:
        global beginstation
        beginstation = str(input('Wat is je beginstation?: '))
        global start_nummer
        start_nummer = stations.index(beginstation)
        print(beginstation, ' is nummer ', start_nummer + 1, ' en is goedgekeurd')
        return start_nummer

def inlezen_eindstation(station):
    while True:
        global eind_station
        eind_station = str(input('Wat is je eindstation?: '))
        global eind_nummer
        eind_nummer = stations.index(eind_station)
        if start_nummer > eind_nummer:
            print('Kies een begin station die voor het eindstation is')
        else:
            print(eind_station, ' is nummer ', eind_nummer + 1, 'en is goedgekeurd')
            omroepen_reis()
            break

        return eind_nummer

def omroepen_reis():
    print('Het beginstation is: ', beginstation,'dit is het ', start_nummer,'e station in het traject.')
    print('Het eindstation is: ',eind_station,'dit is het ', eind_nummer,'e station in het traject')
    afstand = eind_nummer - start_nummer
    prijs = afstand*5
    print('De afstand bedraagt ', afstand, 'station(s)')
    print('De prijs van het kaartje is: ',prijs)



inlezen_beginstation(stations)
inlezen_eindstation(stations)
