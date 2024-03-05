



# class Koleco:
#     def __init__(self,count='',diametr='',disk=''):
#         self.count = count
#         self.diametr = diametr
#         self.disk = disk
#     def koleco_show(self):
#         print(f'у нашей машины есть {self.count} колеса диматером {self.diametr} и {self.disk} диски')

# class Dvigatel:
#     def __init__(self,horsepower='',litraj=''):
#         self.horsepower = horsepower
#         self.litraj = litraj
    
#     def dvij_show(self):
#         print(f'наша машина имеет-{self.horsepower} лошадинных сил,обьем двигателя {self.litraj}')

# class Doors:
#     def __init__(self,countdor='',):
#         self.countdor=countdor
        
#     def door_show(self):
#         print(f'наша машина имеет {self.countdor} двери')


 

# class Car(Doors,Dvigatel,Koleco):
#     def __init__(self,model):
#         Doors.__init__(self)
#         Dvigatel.__init__(self)
#         Koleco.__init__(self)
#         self.model = model
        
#     def car_show(self):
#         Koleco('4','17mm','литые').koleco_show()
#         Dvigatel('250','2,2').dvij_show()
#         Doors('4').door_show()
#         print(f"модель нашего авто {self.model}") 




# print('------------')
# car = Car('audi')
# car.car_show()



class Emploer:
    def __init__(self,name,age,):
        self.name = name
        self.age = age
    def info(self):
        print(f'{self.name} работает в госпитале врачом ему {self.age} лет')

class President:
    def __init__(self,name,age,country):
        self.country = country
        self.name = name
        self.age = age 
    # def info(self):
    #     print(f'{self.name} работает президентом ему {self.age} в стране {self.country}')
    def __str__(self):
        return f'{self.name}'

class Manager:
    def __init__(self,name,age,departament):
        self.name = name 
        self.age = age 
        self.departament = departament
    def __int__(self):
        return self.age
    
    # def info(self):
    #     print(f'{self.name} работает в банке ему {self.age} в отделении {self.departament}')
class Worker:
    def __init__(self,name,age,profession):
        self.name=name
        self.age = age
        self.profession = profession
    # def info(self):
    #     print(f"Имя - {self.name}, возраст - {self.age}, профессия - {self.profession}")

# emploer = Emploer('иван','30')
president = President('вова',70,'Россия')
manager = Manager('петр',50, 'финансы')
# worker = Worker('мария','28','домохозяйка')
# emploer.info()
# president.info()
# manager.info()
# worker.info()
# print(president.name)
# emploer = Emploer(1,'Иван',45)

print('--------------')
# print(emploer)

print(president)
print(int(manager))


print(president)