# ] Обьединет словари и добавляет функции с помощью
# которых берутся данные из словарей или изменяются

# Имя класса С БОЛЬШОЙ БУКВЫ
# В функции называются методы и первый метд всегда называется
# self - этот обьект
# import hero
from hero import *

myhero1 = Hero("Vurdalak", 5, "Orc")
myhero2 = Hero("Lexa", 4, "Human")

myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()
myhero1.set_health(60)
myhero1.show_hero()
