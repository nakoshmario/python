import datetime
Date_D = '%Y-%m-%d'
goods = {
    'пельмени':[
        {'amount': 1, 
        'expiration_date': datetime.date(2024, 3,30)
    },]
}
def add(goods,title,amount,expriration_date=None):
    holod=goods.keys()
    if expriration_date != None:
        data_test = datetime.datetime.strptime(expriration_date,Date_D)
        dataD = data_test.date()
        if  title in holod :
            goods[title].append({'amount': amount,'expiration_date':dataD})
        else:
            goods[title]=[{'amount':amount,'expriration_date':dataD}]
    else:
       if title in holod :
           goods[title].append({'amount':amount,'expiration_date':expriration_date})
       else:
           goods[title]=[{'amount':amount,'expiration_date':expriration_date}]


add(goods,"пельмени-детские",5, '2023-3-12' )
add(goods,"пельмени",4)
add(goods,'курица',4,   '2024-8-17')
add(goods,'квас',6)
print(goods)


def add_line(line):
    name, amount, expiration_date = line.split(',')
    amount = int(amount)
    if expiration_date.lower() != 'none':
        expiration_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date()
    else:
        expiration_date = None
    add(name, amount, expiration_date)


                



# поиск продуктов 
# def search(goods,title):
#     for i in goods:
#         if i == title:
#             return goods[i]
        
        
# print(search(goods,'курица'))




# def findAmount(goods, title):
#    for item in goods:
#        if item["name"] == title:
#            return (item, item["amount"])
#    return None

# goods = [
#    {"name": "курица", "amount": 10},
#    {"name": "картошка", "amount": 5},
#    {"name": "грибы", "amount": 20}
# ]

# print(findAmount(goods, "курица"))
# print(findAmount(goods, "пельмени"))
    
# функция на проверку по сроку годности всех продуктов и вывод списком каждого продукта
    

# Function to find the amount of an item in the goods list
def findAmount(goods, item):
   for good in goods:
       if good["name"] == item:
           return good["amount"]
   return 0

def checkExpiration(goods):
   for good in goods:
       if good["expiration_date"] < current_date:
           print(f"The {good['name']} has expired.")
       else:
           print(f"у продукта {good['name']} истечет срок годности через {good['expiration_date'] - current_date} дней.")

current_date = 25 

goods = [
   {"name": "грибы", "amount": 20, "expiration_date": 28},
   {"name": "курица", "amount": 10, "expiration_date": 26},
   {"name": "пельмени", "amount": 15, "expiration_date": 30}
]


print(findAmount(goods, "курица"))
print(findAmount(goods, "пельмени"))


checkExpiration(goods)
