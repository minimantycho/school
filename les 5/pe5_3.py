bestand = open('kaartnummer.txt', 'r')
zinnen = sum(1 for line in open('kaartnummer.txt'))
print('Deze file telt',zinnen,'regels')

max_num = 0
line_count = 0
with open('kaartnummer.txt','r') as bestand:
    for line in bestand:
        number = int(line.split(',')[0])
        if number > max_num:
            max_num = number
            line_num = line_count
        line_count += 1
print('het grootste kaartnummer is', max_num, 'en staat op regel', line_num)




# count = 0
# # grootste kaartnummer, naam, welke lijn
# biggest_count = [0,' ',0]
# for zinnen in bestand:
#     count += 1
#     zinnen = zinnen.split(", ")
#     print(zinnen[1].rstrip('\n') + 'heeft kaartnummer: ' + zinnen[0])
#     if (int(zinnen[1]) > int(biggest_count[0])):
#         biggest_count[0] = zinnen[0]
#         biggest_count[1] = zinnen[1]
#         biggest_count[2] = count
#     print('het grootste kaartnummer is: ' + str(biggest_count[0]) + ' and belongs to' + str(biggest_count[1]) )
# #print niks

