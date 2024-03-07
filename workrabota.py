

# people = ['anton','sonya','kolya','jenya','tonya','stepa']

# def say_to_all(func,sequence):
#     for item in sequence:
#         func(item)


# say_to_all(lambda x:print(f'привет {x}'),people)


# say_to_all(lambda x:print(f'до свидания {x}'),people)


# say_to_all(lambda x:print(f'{'здравствуйте' if x[0] == 's' else 'привет'}{x}!'),people)
        

# import datetime

# def prints_stats(func):
#     def wrapper():
#         print('*********************')
#         func()
#         print('*******************')
#     return wrapper




# def prints_hash(func):
#     def wrapper():
#         print('###############')
#         func()
#         print('################')

#     return wrapper




# decorated_current_time = prints_stats(current_time)

# x = prints_hash(decorated_current_time)

# @prints_hash
# @prints_stats

# def current_time():
#     print(datetime.datetime.now().strftime('%H:%M'))
# current_time()




def pizza():
    return ['тесто','томатный соус','сыр']

def margarita(func):
    def wrapper():
        result = func()
        result.append('томаты')
        result.append('пармезан')
        return result
    return wrapper


@margarita
def margarita_pizza():
    return pizza()


print('маргарита:',margarita_pizza())