# class Employee:
#     def __init__(self,name='',fullName='',gender='',otpusk='28'):
#         self.name = name
#         self.fullName = fullName
#         self.gender = gender
#         self.otpusk = otpusk

#     def employeInt(self):
#         self.name = input("введите имя: ")
#         self.fullName = input('введите полное имя: ')
#         self.gender = input('введите пол (муж/жен): ')

#     def showEmploye(self):
#         print(f'имя: {self.name} фамилия: {self.fullName} пол: {self.gender} отпускных дней в году {self.otpusk} дней')

# employee = Employee()

# employee.employeInt()
# employee.showEmploye()


class Transport:
    def __init__(self, power, color='red'):
        self.power = power
        self.color = color
    def start(self):
        print('go to hall')
    def stop(self):
        print('stop on the way')

# class Graund(Transport):
#     def __init__(self,power, color):
#         self.power = power
#         self.color = color
#     def start(self):
#         print('goo oo')
        


# bmw = Graund(100,"blue")
# talk=Transport(50)
# bmw.start()
# print(bmw.color)
# print(bmw.power)

# talk.start()


# class Graund(Transport):
#     def __init__(self, power, color,mesta):
#         super().__init__(power, color)
#         self.mesta = mesta
# bmw = Graund(320, 'black', 4)
# print(bmw.color)
# print(bmw.power)
# print(bmw.mesta)
        
# class Human:
#     def __init__(self, name='Jhon', age='30'):
#         self.name = name
#         self.age = age
# class Biulder(Human):
#     def __init__(self, name,age,work='сварщик',machine='аргон'):
#         super().__init__(name,age)
#         self.work = work
#         self.machine = machine
#     def biuld(self):
#         return (f' имя: {self.name} возраст {self.age} работает {self.work} на транспорте {self.machine}')




# class Sailor(Human):
#     def __init__(self, name, age, work='captain',machine='ship'):
#         super().__init__(name, age)
#         self.work = work
#         self.machine = machine
#     def sailor(self):
#         return (f' имя: {self.name} возраст {self.age} работает {self.work} на транспорте {self.machine}')


# class Pilot(Human):
#     def __init__(self, name, age, work='pilot', machine='airplane'):
#         super().__init__(name, age)
#         self.work = work
#         self.machine = machine
#     def fly(self):
#         return (f' имя: {self.name} возраст {self.age} работает {self.work} на транспорте {self.machine}')





# mark = Biulder('Mark','28','builder','crane')
# print(mark.biuld())
# sophia = Sailor('Sophia','19')
# print(sophia.sailor())
# nikita = Pilot('Nikita','47','pilot','raketa')
# print(nikita.fly())
        


# class Passport():
#     def __init__(self,name='Ivan',fullName='Ivanov',age='10.10.2000',country='Russia',seria='AB123CD'):
#         self.name = name 
#         self.full_name = fullName
#         self.country = country
#         self.age = age
#         self.seria = seria 
    
#     def passport(self):
#         print(f' имя {self.name} фамилия {self.full_name} страна {self.country} возраст {self.age} серия {self.seria}')
# class Zagran(Passport):
#     def __init__(self,name,fullName,age, country,seria,visa):
#         super().__init__(name,fullName,age,country,seria)
#         self.visa = visa

#     def  zagran(self):
#         print('========================')
#         super().passport()
#         for i in self.visa:  
#            print(f' - {i}')

         

# passport = Passport("Alex","25","Alexander","USA", "12-06-2005")
# print(passport.country)
# zagran = Zagran("Alex","25","Alexander","USA", "12-06-2005",['gold', 'silver', 'bronze'])
# zagran.zagran()
        

class Animal:
    def __init__(self,eat='',sleep=''):
        self.eat = eat
        self.sleep= sleep
    def  action(self):
        print(f'есть и спит')
class Crocodail(Animal):
    def __init__(self,eat,sleep,swim,speed,):
        super().__init__(eat,sleep)
        self.swim = swim
        self.speed = speed
    def  croc_show(self):
        print(f'крокодил ест {self.eat}, спит {self.sleep}, быстро {self.swim}, со скоростью {self.speed} км/час')



class Tigr(Animal):
    def __init__(self,eat,sleep,swim,speed,):
        super().__init__(eat, sleep)
        self.swim = swim
        self.speed = speed
    def tiger_show(self):
        print(f'тигр ест {self.eat}, спит {self.sleep}, плохо {self.swim}, бегает со скоростью {self.speed}')



class Kengyry(Animal):
    def __init__(self,eat,sleep,swim,speed):
        super().__init__(eat, sleep)
        self.swim = swim
        self.speed = speed
    def kengyry_show(self):
        print(f"Кенгуряй ест {self.eat}, спит {self.sleep},  плавает {self.swim}, бегает со скростью {self.speed}")

animal = Animal()
Kengyry('траву',"ночью",'плохо','15').kengyry_show()
Tigr('мясо','ночью','плавает',',40').tiger_show()
Crocodail('рыбу','ночью','плавает','30').croc_show()
    




