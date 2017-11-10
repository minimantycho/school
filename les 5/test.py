s = 'a','b','c','d','e','f','g','h'
#opdracht a
print(s[0:4])
#opdracht b
print(s[3:6])
#opdracht c
print(s[3:4])
#opdracht d
print(s[-3:-1])
link = "https://www.nu.nl/wetenschap/4927634/meteorietinslag-zorgde-38-miljoen-jaar-geleden-recordtemperatuur-aarde.html"
print(link[:5].upper())
print(link.replace('wetenschap', 'economie'))
print(link)
new = link.replace('nu','nos')
print(new)
nieuw = link.replace('zorgde','kwam') and link.replace('nu','nos')
print(nieuw)
lst = ['tycho','sam','floris','lars']
for namen in lst:
    print(namen, end=', ')
for namen in lst:
    print (namen, end=' is een mooie man en ')
