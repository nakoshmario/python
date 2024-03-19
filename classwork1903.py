# import random



# numbers = []
# for i in range(10):
#     numbers.append(random.randint(0, 100))
# print(numbers)

# num = int(input('введите число от 1 до 100: '))

# index = -1
# for i in range(len(numbers)):
#     if numbers[i] == num:
#         index = i
       
# if index != -1:
#     print(f'число найдено {numbers[index]}')
# else:
#     print('число не найдено')


# бинарный поиск



# numbers = []
# for i in range(1000):
#     numbers.append(random.randint(0, 1025))

# def bubble_sort(data):
#     last_index = len(data) - 1
#     flag = True

#     while flag:
#         flag = False
#         for item_index in range(last_index):
#             if data[item_index] > data[item_index + 1]:
#                 data[item_index], data[item_index + 1] = data[item_index + 1], data[item_index]
#                 flag = True
#         last_index -= 1
      
#     return data
# print(bubble_sort(numbers))

        

# numbers.sort()
# print(numbers)

# num = int(input('введите число от 1 до 1000: '))
# def binary_search(spisok, x):
#     left = 0
#     rigth = len(spisok)
    
#     while left <= rigth:
#         mid = (left + rigth) // 2

#         if spisok[mid] == x:
          
#             print(f'цифра стоит под индксом {mid}')
           
        
#             return True
#         if spisok[mid] < x:
#             left = mid + 1
#         else:
#             rigth = mid - 1
#     print(f'{num} такого числа в списке нет')

#     return False


    
# binary_search(numbers,num)



# ---------------------------------

# num = int(input('введите числа через пробел'))
# spis = input().split(' ')
# def main():
#     unique = []
#     unique.sort()
#     dublicat = []
    
#     for value in spis:
#         if value not in unique:
#             unique.append(value)
#         else:
#             dublicat.append('_')
#     res = unique + dublicat
#     print(' '.join(res))

# if __name__ == "__main__":
#     main()


    