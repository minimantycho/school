def som():
    lst = []
    while True:
        nextInt = eval(input('Geef een getal: '))
        lst.append(nextInt)
        if nextInt == 0:
            break
    aantal = len(lst)
    lst = sum(lst)
    print('Er zijn ' + str(aantal -1) + ' getallen ingevoerd, de som is: ' + str(lst))
som()

