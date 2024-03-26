# def valid_mountains_array(spis):

#     if  len(spis) < 3: return False
    

#     max_num =max(spis)
#     max_index = spis.index(max_num)

#     if spis.count(max_num) != 1:return False

#     for i in range(1,max_index):
      
#         if spis[i] <= spis [i - 1]: return False
        

#     for i in range(max_index+1,len(spis)):
#         if spis[i] >= spis[i-1]:
#             return False
    
#     if max_index == 0 or max_index == len(spis)-1 :
#         return False
   
#     return True

# print(valid_mountains_array([1,2,3,4,3,2,1])) 
# print(valid_mountains_array([1,2,3,6,5,4]))
# print(valid_mountains_array([1,2,3,4,5,4,3,2,1]))
# print(valid_mountains_array([1,2,3,4,5,6]))
# print(valid_mountains_array([5,4,3,2,1]))    
# print(valid_mountains_array([1,2,3,4,3,7,5,6]))



# стек


class Steck:
    def __init__(self):
        self.stack = []
   
    def push(self, element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()
        print(f'вытащили : {self.stack}')
    
    def size(self):
        print(f'размер стека : {len(self.stack)}')
    
    def peek(self):
        print(f'последний элемент {self.stack[-1]}')
    
 

s = Steck()
s.push('1')
s.push('2')
s.push('3')
s.push('4')
print(s.stack)
s.size()
s.pop()
s.size()
s.peek()



'''
Марсоход отправляет на Землю структурированные данные; в структурах применяются скобки трёх разных видов: [], () и {}. Скобки могут быть вложены друг в друга сколько угодно раз.

Всё бы хорошо, но во время жаркого марсианского лета марсоход перегрелся и по неизвестной причине начал путать скобки. Это привело к тому, что открытые скобки остаются незакрытыми и закрывающие скобки не имеют открывающих. Прочесть такую структуру становится невозможно.

В Центре управления марсоходами решили создать программу для контроля за расстановкой скобок. Если в сообщении порядок скобок нарушен, марсоход создаст сообщение заново: в этом случае вероятность повторения ошибок минимальна.

Напишите функцию is_correct_bracket_seq(), которая принимает на вход скобочную последовательность и возвращает True, если последовательность правильная, и False — в остальных случаях.
'''

'''
Что считать правильной последовательностью
 - Пустая строка — это правильная скобочная последовательность.

 - Правильная скобочная последовательность, взятая в скобки одного типа, — тоже правильная: ( { [ ] } ).

 - Правильная скобочная последовательность с приписанной слева или справа правильной скобочной последовательностью — правильная: ( { [ ] } ) ( [ ] ).

Формат ввода
На вход подаётся одна строка, содержащая скобочную последовательность. Скобки записаны подряд, без пробелов.
{[()]}

'''
def is_correct_bracket_seq():
    bracket_sequence = input().strip()

    
    for i in bracket_sequence :
 