# Для ввода используется input()
# input() принимает ТОЛЬКО STR
# name = input("Ваше имя: ")
#
# print("Привет " + name)
#
# num1 = input("Enter x: ")
# num2 = input("Enter Y: ")
#
# sum = int(num1) + int(num2) # Для конвертации используется int()
# print(sum)

# message = ""
# while True:
#     message = input("Enter Password ")
#     if message == 'secret':
#         break
#     print(message + "Password not correct")
#
# print("Password " + message)


mylist = []
msg=""

while msg != 'stop'.upper():
    msg = input("Введите item")
    mylist.append(msg)

print(mylist)







