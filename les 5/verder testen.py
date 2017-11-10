def BMI(weight, height):
    bmi = weight*703/height**2
    if bmi < 18.5:
        return str(bmi) + ' underweight'
    elif bmi < 25:
        return str(bmi) + ' normal'
    else:
        return 'overweight'

height = eval(input('Hoe veel inch lang ben je? '))
weight = eval(input('Hoeveel weeg je in pounds? '))
print(BMI(height, weight))