def dogs_age(age):
    if age <= 2:
        return age * 10.5
    else:
        return 21 + (age - 2) * 4


print(dogs_age(5))
