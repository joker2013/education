class Hero():
    """Класс лучших героев"""

    def __init__(self, name, level, race):
        """sadasdasd"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """Печатает параметры героев"""
        discription = (self.name + " Уровень " + str(self.level) + " Раса " + self.race + " Здоровье " + str(
            self.health)).title()
        print(discription)

    def level_up(self):
        """Upgrade level of hero"""
        self.level += 1

    def move(self):
        """Старт """
        print("Hero " + self.name + "Старт")

    def set_health(self, new_health):
        self.health = new_health


# наследование класса
class SuperHero(Hero):
    """Class to Create Super"""

    def __init__(self, name, lavel, race, magiclevel):
        """blablabla"""
        super().__init__(name, lavel, race)
        self.magiclevel = magiclevel
        self.__magic = 100     # __ Запрещает доступ к magic из вне класса

    def makemagic(self):
        self.magic -= 10

    # Рассширение функции
    def show_hero(self):
        discription = (self.name + " Уровень " + str(self.level) + " Раса " + self.race + " Здоровье " + str(
            self.health) + " Магия " + str(self.magic)).title()
        print(discription)
