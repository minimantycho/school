#deel 1
# for standaardtarief in kilometer:
def standaardtarief(afstandKM):
    if afstandKM >0 :
        if afstandKM >= 50:
            standaardtarief = afstandKM * 0.6 + 15
        else:
            standaardtarief = afstandKM*0.8
    return standaardtarief



#deel 2
def ritprijs(leeftijd,weekendrit,afstandKM):
    if weekendrit == True and ((leeftijd <120 and leeftijd >=65) or (leeftijd >0 and leeftijd <12)):
        print(standaardtarief(afstandKM)/1.35)
    elif weekendrit == False and ((leeftijd >=65 and leeftijd <120) or (leeftijd > 0 and leeftijd <12)):
        print(standaardtarief(afstandKM)/1.30)
    elif weekendrit == True and (leeftijd <65 and leeftijd >12):
        print(standaardtarief(afstandKM)/1.40)
    elif weekendrit == False and (leeftijd <65 and leeftijd >12):
        print(standaardtarief(afstandKM))
    else:
        print('Error')
    return

ritprijs(30,True,52)