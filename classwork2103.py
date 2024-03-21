# def list_superset(x,y):
#     count = 0
#     count2 = 0
#     if len(x) > len(y):
#         for i in range(len(x)):
#             index = x[i]
#             for j in range(len(y)):
#                 if  y[j] == index:
#                     count += 1

#     elif len(y) > len(x):
#         for i in range(len(y)):
#             index = y[i]
#             for j in range(len(x)):
#                 if x[j] == index:
#                     count2 +=1

#     elif x == y:
#         print(f'{x} и {y} - равны')
    

#     if  count == len(y):
#         print(f'{x}являестя супермножеством по отношению к {y}')
#     if count2 == len(x):
#         print(f'{y}являестя супермножеством по отношению к {x}')
#     if len(x)==2  and len(y)== 2 :
#         print(f'{y} and {x} это не супармножества')



# list_set_1 = [1, 3, 5, 7]
# list_set_2 = [3,5]
# list_set_3 = [5,3,7,1]
# list_set_4 = [5,6]

# list_superset(list_set_1,list_set_2)
# list_superset(list_set_2,list_set_3)
# list_superset(list_set_1,list_set_3)
#list_superset(list_set_2,list_set_4)


import time 

from random import randint

start_time = time.time()

DATA_SIZE = 10000

MAX_RAND_NUMBER= 10000000

data = [randint(1,MAX_RAND_NUMBER) for _ in range(DATA_SIZE)]


print(f'коллекция data сгенерирована за {time.time() - start_time} сек')

count = 0

for i in range(10000):
    num =  randint(1, MAX_RAND_NUMBER)
    if num in data:
        count += 1  

print(f'найдено совпадений: {count}')
print(f'обьектов в data найдено: {len(data)}')

print(f'программа отработала за {time.time() - start_time} сек')
