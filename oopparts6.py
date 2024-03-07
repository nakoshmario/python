# class Figure:

#     def area(self):
#         pass

#     def __int__(self):
#         return (self.area())
    
#     def __str__(self):
#         return f'{self.__class__.__name__} с площадью: {self.area()}'
# class Pryamoygolnik(Figure):
#     def __init__(self,a='',b='',c=''):
#         self.a = a
#         self.b = b
#         self.c = c
#     def  area(self):
#         return self.a * self.b *self.c


# class Squir(Figure):
#     def __init__(self,a=''):
#         self.a = a
        
#     def area(self):
#         return self.a * 4

    
# class Treygol(Figure):
#     def __init__(self,a='',b=''):
#         self.a = a 
#         self.b =b 
         
#     def area(self):
#         return 0.5 * self.a * self.b

# class Trapecia(Figure):
#     def __init__(self,a='',b='',h=''):
#         self.a = a
#         self.b = b
#         self.h =h
#     def area(self):
#         return ((self.a + self.b)/ 2 * self.h )

# class Krug(Figure):
#     def __init__(self,r=''):
#         self.r = r
#     def area(self):
#         return  3.14*self.r**2

        


# pryamoygolnik = Pryamoygolnik(3,4,5)
# # # print(Pryamoygolnik(3,4,5).area())
# squir = Squir(12)
# # # print(Squir(12).area())
# treygol= Treygol(6,8)
# # # print(Treygol(6,8).area(),'площадь через основание')
# trapecia = Trapecia(4,7,9)
# # # print(Trapecia(4,7,9).area())
# krug = Krug(5)
# # # print(Krug(5).area())





# print(int(pryamoygolnik))
# print((pryamoygolnik))
# print('-----------------')
# print(int(squir))
# print(squir)
# print('-----------------')
# print(float(treygol.area()))
# print(treygol)
# print('-----------------')
# print(float(trapecia.area()))
# print(trapecia)
# print('-----------------')
# print(float(krug.area()))
# print(krug)
# print('-----------------')



class Shape:
    def __init__(self,name=''):
        self.name = name

    def show(self):
        return f"Я {self.name}"
    def save(self,file_name):
        with open(file_name,'w') as file:
            file.write(self.show())
 



class Square(Shape):
    def __init__(self, x, y, side, name=''):
        super().__init__(name)
        self.x = x
        self.y = y
        self.side = side

    def loadd(self):
        return f"Сquare: x={self.x}, y={self.y}, side={self.side}"
class Rectangle(Shape):
    def __init__(self, x, y, width, height, name=''):
        super().__init__(name)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def loadd(self):
        return f"Rectangle: x={self.x}, y={self.y}, width={self.width}, height={self.height}"
class Circle(Shape):
    def __init__(self, x, y, radius, name=''):
        super().__init__(name)
        self.x = x
        self.y = y
        self.radius = radius

    def loadd(self):
        return f"Circle: x={self.x}, y={self.y}, radius={self.radius}"
class Ellipse(Shape):
    def __init__(self, x, y, semi_axis_1, semi_axis_2, name=''):
        super().__init__(name)
        self.x = x
        self.y = y
        self.semi_axis_1 = semi_axis_1
        self.semi_axis_2 = semi_axis_2

    def loadd(self):
        return f"Ellipse: x={self.x}, y={self.y}, semi_axis_1={self.semi_axis_1}, semi_axis_2={self.semi_axis_2}"
            

