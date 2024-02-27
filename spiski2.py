
# test = {
#     'name':'John',
#     'age':30,
# }

# test['city'] = 'москва'

# print(test)


# test ={
#     'name':'dima',
#     'age':20,
# }
# for i in test.keys():   -------ключ
#     print(i)
# for i in test.values(): -----значение
#     print(i)
# for key,value in test.items(): -------итоидругое
#     print(f'ключ: {key}, значение: , {value}')



# words = {}

# for i in range(1,11):
#     words[i] = i**3
# print(words)

# my_dict = {i : i ** 3 for i in range(1,11)}
# print(my_dict) -----------через генератор


# spis1 = [1,2,3,4,5]

# spis2 = ['hello','world','test','good','ola']

# spisok = zip(spis1,spis2)
# print(dict(spisok))

# text = 'pythonist'
# dict_test= {}
# for i in text:
#     dict_test[i] = text.count(i)

# print(dict_test)



# points_en = {1:'AEIOULNSTR',
#       	2:'DG',
#       	3:'BCMP',
#       	4:'FHVWY',
#       	5:'K',
#       	8:'JZ',
#       	10:'QZ'}
# points_ru = {1:'АВЕИНОРСТ',
#       	2:'ДКЛМПУ',
#       	3:'БГЁЬЯ',
#       	4:'ЙЫ',
#       	5:'ЖЗХЦЧ',
#       	8:'ШЭЮ',
#       	10:'ФЩЪ'}

# words = input('введите слово: ').upper()
# summa =  0
# for i in words:
#     for key,value in points_en.items():
#         if i in value:
#             summa +=key
#     for key,value in points_ru.items():
#         if i in value:
#             summa +=key
# print(summa)



# name_1 = {
#     'имя': 'илон',
#     'фамилия':'маск',
#     'возраст':'50',
#     'город':'техас',
# }
# name_2 = {
#     'имя': 'киану',
#     'фамилия':'ривз',
#     'возраст':'67',
#     'город':'канзас',
# }
# name_3 = {
#     'имя': 'джони депп',
#     'фамилия':'воробей',
#     'возраст':'60',
#     'город':'черная жемчужина',
# }
# name_0=[name_1,name_2,name_3]

# for i in name_0:
#     print('инфо')
#     for key,value in i.items():
#         print(f'{key}:{value}')
#         if key == 'город':
        
#             print("----------")



# friuts=('apple','bananawqesdqwd','strawbarry','banana','sliva','blackberry','cherry','banana','aplle','banana')

# text=input('введите название фрукта: ')

# count = friuts.count(text)
# # print(count)

# count2 = 0
# for i in friuts:
#     if text in i:
#         count2 +=1 
# print(count2)



marka = ('lada','bmw','opel','honda','dodge',)

marka1=[]
text=input('Выберите марку авто: ')
text1=input('Выберите марку для замены: ')

for i in marka:
    if text == i:
        marka1.append(text1)
    else:
        marka1.append(i)

marka = tuple(marka1)
print(marka)    
print(marka1)









    
    
