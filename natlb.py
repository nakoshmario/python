import matplotlib.pyplot as plt

# input_values = [1,2,3,4,5]
# squares = [1,4,9,16,25]

# plt.style.use('seaborn-v0_8-darkgrid')

# ax = plt.subplot()
# ax.plot(input_values, squares,linewidth=3)

# ax.set_title('моя диаграмма',fontsize=20)
# ax.set_xlabel('gorizont',fontsize=14)
# ax.set_ylabel('vertikont', fontsize=14)
# ax.tick_params(axis='both', which='major', labelsize=10)
# plt.show()

from random import choice
# блуждающие точки
class Rand():
    def __init__(self,col_point=5000):
        self.col_point = col_point

        self.x_arr = [0]
        self.y_arr = [0]

    def walk(self):
        while len(self.x_arr) < self.col_point:
            x_nap = choice([1,-1])
            x_distance = choice([0,1,2,3,4,])
            x_step = x_nap * x_distance

            y_nap = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_nap * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_arr[-1] + x_step
            y = self.y_arr[-1] + y_step

            self.x_arr.append(x)
            self.y_arr.append(y)
            print(f'{x},{y}')
        plt.plot(self.x_arr,self.y_arr)
        plt.show()

    def plot(self):
        plt.plot(self.x_arr,self.y_arr)
        plt.show()
r = Rand()
r.walk()