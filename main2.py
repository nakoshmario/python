# import random

# i = random.randint(1,500)
# count = 0

# while True:
#     user = int(input('введите число: '))
#     if user == 0:
#         break
        
#     count += 1
#     if user > i:
#         print('меньше')
#     elif user < i:
#         print('больше')
#     elif user == i:
#         print("вы нашли число")
# print(count)
    

# number = int(input('введите число: '))
# res = number

# while res > 0:
#     print('* ' * number)
#     number -= 1


# number1 = int(input('введите число'))
# number2 = int(input('введите второе число'))
# while number2 > 0:
#     print ('*' * number1)
#     number2 -= 1


# num1 = int(input('введите первое число:'))
# # num2 = int(input('введите второе число:'))

# for i in range(0,num1):
#     for j in range(0,num1):
#         if i == 0 or j == 0 or i == num1-1 or j==num1-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print('')


# num1 = int(input('введите первое число: '))
# num2 = int(input('ввдетие втророе число: '))


# for i in range(0,num1):
#     for i1 in range(0,num2):
#         if i == 0 or i1 ==  0 or i == num1 - 1 or i1 == num2 - 1:
#             print('*', end=" ")
#         else:
#             print(' ', end= ' ')
#     print('')


# number = str(input('введите число'))
# zero=0
# count=0
# sum=0
# for i in str(number):
#     count += 1
#     sum += int(i)
#     if int(i) == 0:
#         zero += 1
# midleArif=sum // count
# print(f'сумма {sum}, средне арифмитическое {midleArif}, нули {zero} ')


# import random

# while True:
#     lvl = int(input('введите уровень сложности: 1 = легкий. 2 = средний. 3 = сложный: '))
#     if lvl == 1:
#         num1 = random.randint(1,3)
#         num2 = random.randint(1,10)
#         a = int(input(f' {num1} * {num2} = '))
#         if a == num1*num2:
#             print('верно')
#             break
#         else:
#             print('ошибка')
#     if lvl == 2:
#         num1 = random.randint(1,10)
#         num2 = random.randint(1,10)
#         a = int(input(f'{num1} * {num2}= '))
#         if a == num1 * num2:
#             print('верно')
#             break
#         else:
#             print('шибка')
#     if lvl == 3:
#         num1 = random.randint(1,10)
#         num2 = random.randint(1,10)
#         num3 = random.randint(1,10)
#         a = int(input(f'{num1} * {num2} * {num3} = '))
#         if a == num1*num2*num3:    
#             print('верно')
#             break
#         else:
#             print('ошибка')
#  






