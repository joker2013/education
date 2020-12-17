enemy = {
#     key     value
    'loc_x': 70,   # 'loe_x': 70, - item
    'loc_y': 50,   #  loe_x - key    50 - value
    'color': 'green',
    'health': 100,
    'name': 'Mudilo',
}
print(enemy)
print("location x = " + str(enemy['loc_x']))
print("location y = " + str(enemy['loc_y']))
print("name = " + str(enemy['name']))

# Добавление в словарь
enemy['rank'] = 'Admiral'
print(enemy)

# Стиране
del enemy['rank']
print(enemy)

 # Изменение параметров в словаре
enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] - 30

if enemy['health'] < 80:
    enemy['color'] = 'yellow'
print(enemy)


print(enemy.keys())
print(enemy.values())