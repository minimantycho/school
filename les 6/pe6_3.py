invoer = ('5-9-7-1-7-8-3-2-4-8-7-9')

nieuw = invoer.split('-')
nieuw.sort()
grootste = max(nieuw)
kleinste = min(nieuw)
aantal = len(nieuw)
plus = int()
for y in nieuw:
    plus += int(y)
int(aantal)
gemiddelde = plus/aantal
print('De gesoorteerde list van ints:', nieuw)
print('het grootste getal is:', grootste,'en het kleinste getal is:',kleinste)
print('Aantal getallen:',aantal,'en Som van de getallen:',plus)
print('Het gemiddelde is:',gemiddelde)