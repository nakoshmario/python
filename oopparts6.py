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
    def __init__(self, name):
        self.name = name

    def draw(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for line in self.get_lines():
                line = ['*' for _ in line]
                file.write(" ".join(line) + "\n")
            file.write(f"{self.name}\n")
    def figury_show(self):
        f'{self.name} - фигура'

    def get_lines(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, x, y, side, name):
        super().__init__(name)
        self.x = x
        self.y = y
        self.side = side

    def get_lines(self):
        lines = []
        for i in range(self.side):
            line = []
            for j in range(self.side):
                line.append('*')
            lines.append(line)
        return lines

class Triangle(Shape):
    def __init__(self, x, y, width, height, name):
        super().__init__(name)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_lines(self):
        lines = []
        for i in range(self.height):
            line = []
            for j in range(i + 1):
                line.append('*')
            lines.append(line)
        return lines


square = Square(10, 21, 10, "квадрат-- последнияя цифра опеределяет размер  стороны квадрата")


square.draw('square.txt')


triangle = Triangle(10, 5, 10, 15, "треугольник --  последние две цифры определяют размер у треугольника")


triangle.draw('triangle.txt')



    
       