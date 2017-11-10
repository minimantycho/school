def code(invoerstring):
    resultaat = ''

    for letter in invoerstring:
        resultaat += chr(ord(letter)+3)


    return resultaat

print(code(input('Geef een zin: ')))
