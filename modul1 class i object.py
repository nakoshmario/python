class Car:
   def __init__(self, marka='', model='', data_vypuska='', madein='', obmdvigka='', color='', price=''):
       self.marka = marka
       self.model = model
       self.data_vypuska = data_vypuska
       self.madein = madein
       self.obmdvigka = obmdvigka
       self.color = color
       self.price = price

   def mobildata(self):
       self.marka = input('Введите марку автомобиля: ')
       self.model = input("Введите модель автомобиля: ")
       self.data_vypuska = int(input("Укажите год выпуска: "))
       self.madein = input("Укажите страну производства: ")
       self.color = input("Укажите цвет автомобиля: ")
       self.price = input("Укажите цену автомобиля: ")
       self.obmdvigka = int(input("Укажите объем двигателя: "))

   def mobilShow(self):
       print("Марка: ", self.marka)
       print("Модель: ", self.model)
       print("Год выпуска: ", self.data_vypuska)
       print("Страна производства: ", self.madein)
       print("Цвет: ", self.color)
       print("Цена: ", self.price)
       print("Объем двигателя: ", self.obmdvigka)

   def showInPole(self, pole):
       if pole == 'model':
           return self.model
       elif pole == 'data_vypuska':
           return self.data_vypuska
       elif pole == 'marka':
           return self.marka
       elif pole == 'madein':
           return self.madein
       elif pole == 'obmdvigka':
           return self.obmdvigka
       elif pole == 'color':
           return self.color
       elif pole == 'price':
           return self.price
       else:
           print('Такого поля не существует')
           return None

car = Car()
car.mobilShow()
car.mobildata()
print(car.showInPole('marka'))

# -------------------------------------------
