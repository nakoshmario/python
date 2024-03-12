

# class Human:
#     chel= 0
#     def __init__(self, name, age,gender):
#         self.age = age
#         self.gender = gender
#         self.name = name
#         Human.chel +=1
#     def chel_show(self):
#         print(f"My name is {self.name},{self.age},{self.gender}")
    
    
#     @staticmethod
#     def test():
#         return Human.chel


# test1 = Human('ivan',25,'male')
# test2 = Human('masha',30,'female')
# test3 = Human('alesha',45,'male')
# test4 = Human('katya',30, 'female')

# print(Human.test())
    


# class Figury:
#     count_figura = 0
#     def __init__(self,name):
#         self.name = name





#     @staticmethod
#     def test():
#         return Figury.count_figura
    
#     @staticmethod
#     def area_kv(a ,b):
#         Figury.count_figura +=1
#         return f'площадь квадрата  {a*b}'
    
#     @staticmethod
#     def area_pryam(a,b):
#         Figury.count_figura +=1
#         return f'площадь  прямоугольника {a*b *2}'
    
# test1=Figury('triangle')
# print(test1.area_kv(5, 6))
# test2=Figury('rectangle')
# print(test2.area_pryam(7,8))


# class Number:
#     count = 0
#     def __init__(self):
        
#         pass


#     @staticmethod
#     def srednee(a,b,c,e):
#         return (a+b+c+e) / 4,'средне-арефмитическое'
#     @staticmethod
#     def min_number(a,b,c,e):
#         return min(a,b,c,e),'минимальное число'
#     @staticmethod
#     def max(a,b,c,e):
#         return max(a,b,c,e),'максимальное число' 
   
#     @staticmethod
#     def factorial(a,n):
#         return  a**n
 
   

    


# test1 = Number
# print(type(test1.srednee(2,3,4,5)))
# print(test1.min_number(9,8,7,6))
# print(test1.max(2,3,4,5))
# print(test1.factorial(5,2))






class Libarry:
    def __init__(self,name,address,count):
        self.name= name
        self.address= address
        self.count = count
    
    def __str__(self):
        return f"Название библиотеки {self.name}, адрес хранения {self.address} , количество экземпляров {self.count}"
    
    def __add__(self,other):
        if isinstance(other,Libarry):
            return Libarry(self.name+" "+other.name,self.address,self.count + other.count)
        else:
            raise TypeError("Unsupported operand type for +")
            
    def __sub__(self,other):    
        if isinstance(other,Libarry):
            return abs(self.count - other.count)
        else:
            raise TypeError("Unsupported operand type for -")  
        # операторы сравнениея
    def __gt__(self.other):
        if isinstance(other,Libarry):
            return self.count > other.count 
           


A = Libarry("Book", "India", 50)
B = Libarry("Science Book", "USA", 30)
C = A+B
print(C)
D = C-A
print(D)
    

book1 = Libarry('ly','moscow',50)
book2 = Libarry('sh', 'spb', 100)

print(book1)







    



    