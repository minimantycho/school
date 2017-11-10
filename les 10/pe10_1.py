import xmltodict

file = open("artikelen.xml", 'r')
xml = file.read()
file.close()

xml_dict = xmltodict.parse(xml)
for xml_item in xml_dict['artikelen']['artikel']:
    print(xml_item['naam'])
