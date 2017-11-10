studentcijfers = [[95, 92, 86], [66, 75, 54],  [89, 72, 100], [34, 0, 0]]

def gemiddelde_per_student(studentcijfers):
    global lst
    lst = []
    for student in studentcijfers:
        antwoord = sum(student)/len(student)
        lst.append(antwoord)
        print(lst)
    return lst


def gemiddelde_van_alle_studenten():
    gemiddeld = sum(lst)/len(lst)
    print(gemiddeld)
gemiddelde_per_student(studentcijfers)
gemiddelde_van_alle_studenten()