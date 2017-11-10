def convert(celsius):
    antwoord = celsius*1.8+32
    return antwoord

def table():
    for x in range(-30,41,10):
        # tabel = print(str(x) + ' '  + str(convert(x)))
        print('{:5},{:5}'.format(str(x), (convert(x))))


table()



