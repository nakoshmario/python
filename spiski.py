# list_num = list()
# list_num2=[1,2,3,4,5,6,7,8,9]
# print(list_num2)


# cort = (1,2,3,4,5,6)
# cort[2] = 10
# print(cort)


# ola= input('ввдеите строку: ')

# count_str=0
# count_num=0
# count=0

# for i in range(len(ola)):
#     if  ola[i].isalpha():
#         count_str +=1
#     elif ola[i].isdigit():
#         count_num +=1
#     elif  ola[i].isalpha() == False and  ola[i].isdigit() ==False:
#         count+=1
# print (f'количество букв :{count_str},количество цифр:{count_num},символов:{count}')



# text=input('введите текст: ')
# text1=input('искомый символ: ')

# res = text.split(' ')
# for i in range(len(res)):
#     if res[i].lower()==text1.lower():
#         res[i]=input('введите текст: ')
        
# print(' '.join(res))
# # print(res)



# sp=[]

# number=





# sp=[]

# while True:
#     number=int(input("введите число: "))
#     sp.append(number)
#     vopros=int(input('продолжим?1=да.2=нет: '))
#     if vopros == 2:
#         num2 = int(input('CHto? '))
#         print(sp.count(num2))
#         break
#     # summa=0
#     # count=0
#     # for i in range(len(sp)):
#     #     summa+=sp[i]
#     #     count +=1

# s = sum(sp)
# count = len(sp)
# print(f'сумма элементов списка {s}')
# print(f'Sred {s/count}')

# # print(f'сумма всех чисел={summa}')
# # print(f'количество добавленых цифр={count}')
# # print(summa/count)



# import random

# list_test=[]

# for i in range(1,10):
#     list_test.append(random.randint(-10,20))
#     res=sum(list_test)
    
# print(list_test)

# y = 0
# r = 0
# t = 0

# for i in list_test:
#     if i % 2 == 0:
#         y += i
#     elif i % 2 == 1:
#         r += i
#     if i < 0:
#         t += i
# print(y,r,t)

# p=1
# for i in range(0,len(list_test),3):
#     p *= list_test[i]
# print(p)

    
# max_index = list_test.index(min(list_test))
# min_index = list_test.index(max(list_test))
# min_max = 1
# if min_index < max_index:
#     for i in range(min_index,max_index+1):
#         min_max *list_test[i]
# else:
#     if max_index < min_index:
#         for i in range(max_index,min_index+1):
#             min_max /list_test[i]

# print(f'самое маленькое ччисло: {min(list_test)}')
# print(f'самое большое число: {max(list_test)}')
    






 


