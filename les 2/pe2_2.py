# opdracht 2.2
cijferICOR = 8
cijferPROG = 6
cijferCSN = 6
cijfers = [cijferICOR, cijferPROG, cijferCSN]
gemiddelde = sum(cijfers) / len(cijfers)
beloning = sum(cijfers) * 3
overzicht = "Jij krijgt €" + str(beloning) + "\nJij hebt totaal " + str(sum(cijfers)) + " cijferpunten hebt gehaald over " + str(len(cijfers)) + " vakken.\nJouw gemiddelde voor al deze vakken is: " + str(gemiddelde)
print(overzicht)
