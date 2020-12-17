

# Цикл работает от 0 до 100
for x in range(0,100):
    print("***")
    print("-------")
# Печатаем каждое второе число. Меняем шаг в 2
for x in range(-100, 10, 2):
    print(x)
# Прерывание цикла
for x in range(100, 10, -2):
    print("Number x = " + str(x))
    if x== 50:
        break

print("---EOF---")
# До тех пор
x=0
while True:
    print(x)
    x=x+1    # x++ означает x+1
    if x ==100:
        break
