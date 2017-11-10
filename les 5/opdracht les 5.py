dag = 11
maand = 'mei'
weekdag = 'zaterdag'
jaar = 2017
uur = 17
minuut = 54
seconden = 32
print('{} {}, {}, {} at {}:{}:{}'.format(dag,maand,weekdag,jaar,uur,minuut,seconden))

lst = ['Tycho Werff', 'Ties Sluijs', 'lars tuijl']
for name in lst:
    fl = name.split()
    print('{:8}{:1}'.format(fl[0],fl[1]))

n = 87
print('{:b}'.format(n))
print('{:c}'.format(n))
print('{:d}'.format(n))
print('{:x}'.format(n))
print('{:e}'.format(n))
print('{:3:f}'.format(n))