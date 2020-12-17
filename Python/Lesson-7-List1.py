



cities = ['New York', 'Moscow', 'new dehli', 'Simferopol', 'Toronto']

print(cities)

# Колличество в массиве
print(len(cities))
# Выбор из массива
print(cities[0])
# Первый с канца
print(cities[-1])
print(cities[2].upper())
# замена в массиве
cities[2] = 'Tula'
print(cities)
# Добавление в массив
cities.append('Kursk')
cities.append('Yalta')
print(cities)
# Добавление в  нужное место
cities.insert(1, 'Feodosiya')
print(cities)

# Стирание из массива
del cities[-1]
print(cities)
# Стирание из массива по названию
# cities.remove('Tule')
# print(cities)
# Обрезает последний символ
deleted_city = cities.pop()
print("Deleted city is: " + deleted_city)
print(cities)

# Сортировка
cities.sort()
print(cities)

# Сортировка наоборот
cities.sort(reverse=True)
print(cities)
cities.reverse()
print(cities)
