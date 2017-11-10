def read():
    global ticker
    with open('tickerFile.txt', 'r') as bestand:
        ticker = dict()
        for regels in bestand:
            regels = bestand.readlines()
            for lijn in regels:
                lijn = lijn.strip().split(';')
                ticker[lijn[0]] = lijn[1]
    bestand.close()
    return(ticker)

lijst = read()
print(lijst)
def bedrijf():
    bedrijf = input('Geef het bedrijf zijn naam: ')
    ticker = print('Ticker: ', lijst[bedrijf])
    return ticker

def tick():
    tick = input('Geef de ticker van het bedrijf: ')
    organisatie = print('hele naam: ', list(lijst.keys())[list(lijst.values()).index(tick)])
    return organisatie


read()
bedrijf()
tick()