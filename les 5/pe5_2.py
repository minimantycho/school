bestand = open('kaartnummer.txt', 'r')
zinnen = bestand.readlines()
bestand.close()
print(zinnen)

for zin in zinnen:
    kaartinfo = zin.split(',')
    print(kaartinfo[1].strip() + 'heeft kaart nummer: ' + kaartinfo[0].strip())
