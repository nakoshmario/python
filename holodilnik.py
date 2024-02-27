# функция добавления продукта в холодильник
# import datetime
# Date_D = '%Y-%m-%d'
# goods = {
#     'пельмени':[
#         {'amount': 1, 
#         'expiration_date': datetime.date(2024, 2, 27)
#     },]
# }
# def add(goods,title,amount,expriration_date=None):
#     holod=goods.keys()
#     if expriration_date != None:
#         data_test = datetime.datetime.strptime(expriration_date,Date_D)
#         dataD = data_test.date()
#         if  title in holod :
#             goods[title].append({'amount': amount,'expiration_date':dataD})
#         else:
#             goods[title]=[{'amount':amount,'expriration_date':dataD}]
#     else:
#        if title in holod :
#            goods[title].append({'amount':amount,'expiration_date':expriration_date})
#        else:
#            goods[title]=[{'amount':amount,'expiration_date':expriration_date}]


# add(goods,"пельмени-детские",5, '2023-3-30' )
# add(goods,"пельмени",4)
# add(goods,'курица',4,   '2024-8-17')
# add(goods,'квас',6)
# # print(goods)
# def add_by_note(items,note):
#     key=goods.keys()
#     spisok = title.split(" ")
#     stroka= spisok[-1]
#     if stroka.find('-') != -1:
#         numb = stroka[-2]
#         datetime=spisok[-1]
#         data_test = datetime.datetime.strptime(spisok).date()
#         title=spisok[0:len(spisok)-2]
#         title_res = ''.join(title)
#         if title_res in key:
#             items[title_res].append({'amount':numb,'expiration_date':data_test})
#         else:
#             num = float(spisok[-1])
#             amount = num
            # print(amount)

                



# поиск продуктов 
# def search(goods,title):
#     for i in goods:
#         if i == title:
#             return goods[i]
        
# print(search(goods,'курица'))

# поиск количества продукта

# def findAmount(goods,title):

#     for i in goods:
#         if i == title:
#             return (goods,i['amount'])
#     print(findAmount(goods,'курица'))
    # функция удаления продукта
# def deleteGoodFromList(goods,name):
#     goods.remove(name)
#     return goods
# print(deleteGoodFromList(goods,'курица'))

# функция проверки на срок годности
# def  checkExpire(item,in_advanca_days):
#     res  = []
#     now = datetime.date.today()
#     amountD = datetime.timedelta(days = in_advanca_days)
   
#     print('------')
#     print('срок истечет в течении',amountD )
#     print('------')
#     print('сенодняшняя дата',now)
#     print('------')
#     print('дней до просрочки')
#     print('------')

#     for i in item:
#         for j in item[i]:
#             if j ['expiration_date'] != None:
#                 print('продукты которые истекают',j['expiration_date']- now)
#                 if (j['expiration_date'] - now) <= amountD:
#                     findAmount(item,i)
#                     list.append(res,(i,findAmount(item,i)))
#     return res
# print(checkExpire(goods,2))
    