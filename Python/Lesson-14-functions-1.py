# Функции определяют в самом начале


def napechatat_privetstvie(name):
    """Приветствие"""
    print("Приветствую " + name + " Всего хорошего")


def summa(x,y):
    # s = x+y
    # return x
    return  x+y


def factorial(x):
    """Считает факториал """
    otvet=1
    for i in range(1, x+1):
        otvet= otvet*i
    return otvet


#-----=-------------

print("--------")
napechatat_privetstvie("Denis")
napechatat_privetstvie("Ivan")

x = summa(33,22)
for i in range(1,10):
    print(str(i) + "!\t = " + str(factorial(i)))


# print(x)
# print(factorial(1))
# print(factorial(5))




