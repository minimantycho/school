kinderen = {'Kees':6, 'Jan':5, 'Kevin':7, 'Ties':8, 'Sam':9, 'Tycho':9.5, 'Maarten':9}
# waarde = kinderen.values()
# print(waarde)
# for slim in kinderen:
#     if waarde >= 9:
#         print(kinderen.keys())

for slim in kinderen.items():
    if (slim[1] >= 9):
        print(slim)

