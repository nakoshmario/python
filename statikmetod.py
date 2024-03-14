

# class Drob:
#     count = 0
#     def __init__(self,name):
#         self.name = name
#         Drob.count +=1
#     @ staticmethod
#     def test():
#         return Drob.count

# test1 = Drob('правильнаяа дробь')
# test1 = Drob('неправильная дробь')
# test1 = Drob('десятичная дробь')
# test1 = Drob('бесконечная дробь')

# print(Drob.test())


# Создайте класс для конвертирования температуры из 
# Цельсия в Фаренгейт и наоборот

class TemperatureConverter: 
   count = 0  

   def __init__(self,):  
     
       TemperatureConverter.count += 1 

   @staticmethod
   def c_f(c):  
       return (c * 9 / 5) + 32
   

   @staticmethod
   def f_c(f):  
       return (f - 32) * 5 / 9
   
   @staticmethod
   def test():
       return TemperatureConverter.count



# ---------------------------------
# print("темпиратура в фарингейтах: ",TemperatureConverter.c_f(100))
# print("темпиратура в цельсиях: ",TemperatureConverter.f_c(212) )
# test1 = TemperatureConverter.c_f(40)
# test2 = TemperatureConverter.f_c(500)
# -------------------------------------------
# рабочий вариант
# test1 = TemperatureConverter()
# test2 = TemperatureConverter()

# print(test1.c_f(500),'цельсии в фарингейт')
# print(test2.f_c(78),'фарингейт в цельсии')
# print( TemperatureConverter.test())
# --------------------------------------------
   