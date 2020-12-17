cars = ['bmw', 'vw', 'seat', 'shkoda', 'lada']

# Печать индекса из массива

for x in cars:
    print(x.upper())

for x in range(1,6):
    print(x)
# Создаем массив
mynumber_list = list(range(0, 100 +1))
print(mynumber_list)
print("======================")

# Каждое число из массива умножить на 2
for x in mynumber_list:
    x=x*2
    print(x)
mynumber_list.sort(reverse=True)
print(mynumber_list)

# Поиск максимальных чисел
print("Max number is " + str(max(mynumber_list)))

# Поиск минимального числа
print("Max number is " + str(min(mynumber_list)))

print("Summa of list is " + str(sum(mynumber_list)))
#         0     1     2        3         4
cars = ['bmw', 'vw', 'seat', 'shkoda', 'lada']
# Выборка машин
mycars = cars[1:4]  # 4 - по какого значения НЕ ВЫКЛЮЧАЯ
print(mycars)
mycars=cars[:4]
print(mycars)

mycars =cars[-3:-1]
print(mycars)


# Копирования массива
cars = ['bmw', 'vw', 'seat', 'shkoda', 'lada']
mycars = cars[:]