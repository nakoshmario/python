# class Car:
#    def __init__(self, marka='', model='', data_vypuska='', madein='', obmdvigka='', color='', price=''):
#        self.marka = marka
#        self.model = model
#        self.data_vypuska = data_vypuska
#        self.madein = madein
#        self.obmdvigka = obmdvigka
#        self.color = color
#        self.price = price

#    def mobildata(self):
#        self.marka = input('Введите марку автомобиля: ')
#        self.model = input("Введите модель автомобиля: ")
#        self.data_vypuska = int(input("Укажите год выпуска: "))
#        self.madein = input("Укажите страну производства: ")
#        self.color = input("Укажите цвет автомобиля: ")
#        self.price = input("Укажите цену автомобиля: ")
#        self.obmdvigka = int(input("Укажите объем двигателя: "))

#    def mobilShow(self):
#        print("Марка: ", self.marka)
#        print("Модель: ", self.model)
#        print("Год выпуска: ", self.data_vypuska)
#        print("Страна производства: ", self.madein)
#        print("Цвет: ", self.color)
#        print("Цена: ", self.price)
#        print("Объем двигателя: ", self.obmdvigka)

#    def showInPole(self, pole):
#        if pole == 'model':
#            return self.model
#        elif pole == 'data_vypuska':
#            return self.data_vypuska
#        elif pole == 'marka':
#            return self.marka
#        elif pole == 'madein':
#            return self.madein
#        elif pole == 'obmdvigka':
#            return self.obmdvigka
#        elif pole == 'color':
#            return self.color
#        elif pole == 'price':
#            return self.price
#        else:
#            print('Такого поля не существует')
#            return None

# car = Car()
# car.mobilShow()
# car.mobildata()
# print(car.showInPole('marka'))

# -------------------------------------------



# class Book:
#     def  __init__(self,name='',data='',autor='',janr='',cena='',izdatel=''):
#         self.name = name
#         self.data = data
#         self.autor = autor
#         self.janr = janr
#         self.cena = cena
#         self.izdatel = izdatel

#     def knigaData(self):
#         self.name = input('ввдеите название книги: ')
#         self.data = input("Введите дату выхода книги: ")
#         self.autor = input("Введите автора: ")
#         self.janr = input("Введите жанр: ")
#         self.cena = input('Введите цену: ')
#         self.izdatel = input("Введите издательство: ")
#     def bookShow(self):
#         print('Название: ',self.name)
#         print('Дата выхода: ',self.data)
#         print('Автор: ',self.autor)
#         print('Жанр: ',self.janr)
#         print('Цена: ',self.cena)
#         print('издательство: ',self.izdatel)
#     def showLine(self,line):
#         if  line=='name':
#             return self.name
#         elif line == 'data':
#             return self.data
#         elif line == 'autor':
#             return self.autor
#         elif line == 'janr':
#             return self.janr
#         elif line == 'cena':
#             return self.cena
#         elif  line == 'izdatel':
#             return self.izdatel
#         else:
#             print('нет такой строки')
#             return None
# book = Book()
# book.bookShow()
# book.knigaData()
# print(book.showLine('janr'))

# -----------------------------

# class Stadion:
#     def  __init__(self, name='', city='',country='',dataOpen='',peopleCount=''):
#         self.name=name
#         self.city=city
#         self.country=country
#         self.dataOpen = dataOpen
#         self.peopleCount = peopleCount
#     def stadionData(self):
#         self.name = input('введите название стадиона: ')
#         self.city = input("Введите город расположения стадиона: ")
#         self.country = input("Введите страну расположения стадиона: ")
#         self.dataOpen = input("Укажите дату открытия стадиона: ")
#         self.peopleCount = input("Укажите количество мест на стадионе: ")
#     def  stadionShow(self):
#         print ('Стадион: ',self.name)
#         print ("Город: ",self.city)
#         print ("Страна: ",self.country)
#         print ("Дата открытия: ",self.dataOpen)
#         print ("Количество мест: ",self.peopleCount)
#     def  showLine(self,line):
#         if line == 'name':
#             return self.name
#         if line == 'city':
#             return self.city
#         if line == 'country':
#             return self.country
#         if line == 'dataOpen':
#             return self.dataOpen
#         if line == 'peopleCount':
#             return self.peopleCount
#         else:
#             print('нет такой строки')
#             return None
        
# stadion = Stadion()
# stadion.stadionShow()
# stadion.stadionData()
# print(stadion.showLine('city'))
# --------------------