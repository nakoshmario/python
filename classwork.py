# import random

# list_quest = ['домашку делаешь?','какие оценнки в школе?','как зовут?']

# list_action = ['сделай дз','скажи как тебя зовут','не балуйся']

# game_list = []

# def userList(list):
#     while  True:
#         name = input('введите имя игрока: ')
#         if len(name) < 2:
#             print ('имя должно быть не меньше двух символов')   
#             continue
#         list.append(name.title())
#         if len(list) >= 2:
#             text=input('продолжаем? ')
#             if text.lower() == 'да':
#                 continue
#             else:
#                 break
# userList(game_list) 

# print(game_list)

# def game(list_quest,list_action,game_list):
#     for i in game_list:
#         print(i)
#         quest = input("правда или действие: ")
#         if quest.lower() == 'правда':
#             xindex = random.randint(0,len(list_quest)-1)
#             print(list_quest[xindex])
#             list_quest.pop(xindex)
#         elif quest.lower() == 'действие':
#             xactindex = random.randint(0,len(list_action)-1)
#             print(list_action[xactindex])
#             list_action.pop(xactindex)
#         else:
#             continue
#         if game_list[-1] == i:
#             break
#         gameCont=input('продолжить? ')  
#         if  gameCont.lower() == 'да':
#             continue
#         if gameCont.lower()  == 'нет':
#             break

# game(list_quest,list_action,game_list)  
        

# ================================


# with open('pi.txt') as file:
#     res = file.read()
#     print(res)

# test = 'words.txt'
# with open ('words.txt','w',encoding='utf-8') as file:
#     file.write(f'работает \n')
#     file.write('еще раз рабоает')
# with open (test,'a',encoding='utf-8') as file:
#     file.write(f'\n добавили еще\n')    



# for i in  range(3):
#     with open('pi.txt', encoding="utf-8") as file:
#         if i == 0:
#             chtenie = file.read()
#             print(chtenie)
#             print('---------------')
#         if i == 1:
#             for i in file:
#                 print(i)
#         print('-----------------')
#         if i == 2:
#             spisok = file.readlines()

# res=' '.join(spisok)
# text= res.replace('пайтене','С++')
# print(text)


# f = 'pi.txt'
# while True:
#     name=input("Введите имя персонажа: ")
#     print(f'{name} привет')
#     with open(f, 'a', encoding='utf-8') as file:
#         file.write(f'{name} привет\n')
#     answer=input("Продолжить? Y/N ").lower()
#     if answer == 'y':
#             continue
#     else:
#             break
# print(file)




