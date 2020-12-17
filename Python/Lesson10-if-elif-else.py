x =25

# Сравнение
if x == 25:
    print("Yes you Right")
# else Иначе
else:
    print("No you are wrong")
print("=====================")

# Сравнение возвраста
age = 31

if age <= 4:
    print("You are baby")
elif age > 4 and age < 12:
    print("You are kid")
elif age>= 12 and age < 19:
    print("You are teenager")
else:
    print("You are old")

print("=++++++++++++++++++==")


all_cars = ['Acura', 'Ford', 'GEO', 'GM', 'GMC']
german_cars = ['Audi', 'Bentley', 'BMW', 'Buick', 'Lexus']
print(all_cars)
if 'Acura' in all_cars:
    print("Есть в листе")
else:
    print("Нет в листе")
# Условие
for xxx in all_cars:
    if xxx in german_cars:
        print(xxx + " Тачки из германии")
    else:
        print(xxx + " Тачка не из германии")





