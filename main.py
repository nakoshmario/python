# message = 'Hello world'
# print(message)
# import this

# print(1 + 2)
# print(1 - 2)
# print(1 * 2)
# print(1 / 2)
# print(1 // 2)

# print('привет','меня','зовут','игорь',sep='_____',end='*')
# print('приятно познакомится')

# print('nothing \n will  work \n unless you do' )

# print('\"Anyone who\n \t  stops \n \t \t learning is old,\n \t \t\t \t whether at twenty or eighty \". \n \t \t \t \t \t \t \t Henry Ford')

# num = int(input('введите число: '))
# num2 = 100
# print(num + num2)


# print('правильно' * 5)

# res = 2 + 10 -бинарный 
# # un = -2 -унарный

# res *=5 -умножение выведет умножнное на 5 раз
# res = 10 -перезапись
# print(res)


# num1 = int(input())
# num2 = int(input())

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)

# num = int(input())
# num2 = 10
# num3 = (num * num2) / 100
# print(num3)


# num1 =int(input())
# num2 =int(input())

# print(num1 * num2)

# num = int(input('введите двухзначное число'))
# res = num //100
# res1 = (num //10)%10
# res2 = num % 10
# print(res)
# print(res1)
# print(res2)


# num1 = int(input())
# num2 = int(input())

# print((num1 + num2))

# celcia = float(input())
# farenheit = float(celcia) * 9/5 + 32
# print(farenheit )

# age = int(input('введите ваш возраст'))

# if age >= 18:
#     print('доступ открыт')
# elif age >= 16 and age < 18:
#     print('родители разрешил?')
# else:
#     print('доступ закрыт')

# num1 = int(input('ввдетие первое число'))
# num2 = int(input('введите второе число'))
# op = int(input('1:+; 2:-; 3:*; 4:/'))

# if op == 1:
#     print(num1 + num2)
# elif op == 2:
#     print(num1 - num2)
# elif op == 3:
#     print(num1 * num2)
# elif op == 4:
#     print(num1 / num2)

# else:
#     print('такого оператора нет')

# age = int(input('введите возраст: '))

# if age <=2:
#     print('младенец')
# elif age > 2 and age <= 4:
#     print('малыш')
# elif age > 4 and age <=13:
#     print('ребенок')
# elif age > 13 and age <=20:
#     print('подросток')
# elif age >=20 and age <= 65:
#     print('взрослый')
# else:
#     print('пожилой')

# name = input('введите имя')


# if name.lower()== 'олег':
#    print('добро пожаловать олег')
#    password = int(input('введите пароль'))
#    if password == 123:
#         print('пароль верный')
#    else:
#         print('пароль неверный')
# else:
#     print('не зарегистрированный пользователь')

# number = int(input('введите число'))

# if number % 7 == 0:
#     print (f'число{number} делится на 7 без остатка')
# else:
#     print(f'{number} не четное')

# diametr = float(input('введите диаметр окрудности'))
# calc = input("введите 'площадь' или 'периметр'")

# if calc.lower() == 'площадь':
#     res = (diametr ** 2/4)* 3.14
#     print(f"площадь круга равна {res}")

# elif calc.lower() == "периметр":
#     perimetr = 3.14 * diametr
#     print('периметр окружности', perimetr)
# else:
#     print('неверный выбор.введите площадь или периметр')


# ps = int(input('ввдеите цену: '))
# count = int(input('введтие колиичество приставок: '))
# disk= int(input('введтие стоимость скилки: '))
# ps = ps * count
# res = (ps / 100)* disk
# if count > 0 and count < 2:
#     print(f' вы взяли {count} приставку. Цена с скидкой составит {ps - res}:  ')
# elif count > 1:
#     print(f'вы купили {count} приставок ваша цена с скидой {ps - res}: ')
# else:
#     print('введите коректные данные ')

# hour = int(input('введите колиство часов: '))
# if hour  >= 0 and hour > 6:
#     print('GOOD NIGHT')
# elif hour > 6 and hour < 13:
#     print('Good morning!')
# elif hour > 13 and hour < 17:
#     print('Good day')
# else:
#     print('Good evening')



# i = 0
# while  True:
#     print('опрос')
#     name = input('введте ваше имя или q для выхода')
#     if name.lower() == 'q':
#         break
#     print(f'очень приятно познакомится {name.title()}')
#     content = input('введите ваш любимый язык програмирования или q для выхода')
#     if content.lower() == 'q':
#         break
#     i += 1
#     v = input('можно ли опубликовать ваши данные? да/нет')
#     if v.lower() == 'да':
#         print(f'результат опроса: {name} love is {content}')
#     else:
#         print('так же хорошо.что вы решили не публиковать свои данные ')
#         continue 


# message = input('введите слово')
# for i in message[0]:
#     print(i)

# for i in range(1,11):
#     print('- * 10')
#     for j in range(1,11):
#         print(f'{i}*{j} = {i * j}')


# zada4ki

# number1 = int(input('введите первое число: '))
# number2 = int(input('введите второе число: '))
# for i in range(number1,number2):
#     print(i)


# number1 = int(input('введите первое число: '))
# number2 = int(input('введите второе число: '))
# for i in range(number1,number2):
#     if i % 2 == 0:
#         print(i+1)


# number1 = int(input('введите первое число: '))
# number2 = int(input('введите второе число: '))
# for i in range(number1,number2):
#     if i % 2 == 0:
#         print(i)


# number1 = int(input('введите первое число: '))
# number2 = int(input('введите второе число: '))

# while number1 <= number2:
#     print(number2)
#     number2 -= 1

# number1 = int(input('введите первое число: '))
# number2 = int(input('введите второе число: '))

# if number1 > number2:
#       print("нормализация не в пордяке")
#       for i in range(number2,number1):
#         if i % 2 == 0:
#             print(i+1)
# else :
#       for i in range(number1,number2):
#         if i % 2 == 0:
#             print(i+1)



# number = input('введтие 6 значное число:')

# if len(number) == 6:
#     num1 = int(number[0:3])
#     num2 = int(number[3:])

#     res_num_1 = (num1 // 100) + (num1 // 10 % 10) + (num1 % 10)
#     res_num_2 = (num2 // 100) + (num2 // 10 % 10) + (num2 % 10)

  
#     if res_num_1 == res_num_2:
#       print("числа счастливые")
#     if res_num_1 != res_num_2:
#       print('числа не счастливые')

# else:
#     print('много цифр')

# number = input('введите 6 значное число')

# if (number) == 6:
#     num1 = int(number[0:1])
#     num2 = int(number[5:])
#     num3 = int(number[1:2])
#     num4 = int(number[4:5])

#     print(num1)
#     print(num2)
#     print(num3)
#     print(num4)

    







    












