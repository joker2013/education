enemy = {
#   key     value
    'loc_x': 70,   # 'loe_x': 70, - item
    'loc_y': 50,   #  loe_x - key    50 - value
    'color': 'green',
    'health': 100,
    'name': 'Mudilo',
    'image': ['image1.jpg', 'image2.jpg', 'image3.jpg']

}
# Создаем массив
all_enemies = []

# Добавляем обьекты в массив
for x in range (0, 10):
#    all_enemies.append(enemy)
    all_enemies.append(enemy.copy())
# Изменение здоровья у одного из обьектов
all_enemies[5]['health'] = 30
all_enemies[8]['name'] = "Kozel"
#all_enemies[2]['loc_x'] = all_enemies[2]['loc_x'] +10
# Можно написать по другому
all_enemies[2]['loc_x'] += 10
print('=====================')

for ene in all_enemies:
    print(ene)

















