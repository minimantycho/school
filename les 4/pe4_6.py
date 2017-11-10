# def wijzig(letterlijst):
#     print(letterlijst)
#     letterlijst.pop(['a','b','c'])
#     letterlijst.append('d','e','f')
#     print(letterlijst)
#     letterlijst = ['a','b','c']
# wijzig(['a','b','c'])

# def wijzig(lijst):
#     print(lijst)
#     wijzig = ['d','e','f']
#     lijst = wijzig
#     print(lijst)
# wijzig(['a','b','c','f'])

def wijzig(lijst):
    print(lijst)
    nieuw = lijst
    nieuw[nieuw.index('a')] = 'd'
    nieuw[nieuw.index('b')] = 'e'
    nieuw[nieuw.index('c')] = 'f'
    print(lijst)


wijzig(['a','b','c','f'])