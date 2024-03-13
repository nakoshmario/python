# def find_primes(n):
#     primes = [True] * (n + 1)
#     primes[0] = primes[1] = False
#     for num in range(2, int(n ** 0.5) + 1):
#         if primes[num]:
#             for multiple in range(num * num, n + 1, num):
#                 primes[multiple] = False
#     return [num for num in range(n + 1) if primes[num]]

# print(find_primes(1000))


# import time

# def time_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"затрачено время на вычесление {end_time - start_time:.4f} секунд")
#         return result
#     return wrapper



# @time_decorator
# def find_primes(start, end):
#     primes = []
#     for num in range(start, end + 1):
#         if num > 1:
#             is_prime = True
#             for i in range(2, int(num ** 0.5) + 1):
#                 if num % i == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 primes.append(num)
#     return primes

# find_primes(100, 500)


# отчеты разных организация по финансам с помощью декораторов

def finance_otchet():
    return []

def company_run(func):
    def wraper():
        res = func()
        res.append('январь -100')
        res.append('ферваль -400')
        res.append('март -100')
        res.append('апрель -100')
        res.append('май -100')
        res.append('июнь-1300') 
        return res
    return wraper
@company_run
def company_run():
    return  finance_otchet()

print('финансовый отчет компании за первое полугодие "run"',company_run())

def air_company(func):
    def wraper():
        res = func()
        res.append('январь -300')
        res.append('февраль -500')
        res.append('март -8100')
        res.append('апрель -900')
        res.append('май -1000')
        res.append('июнь -500')
        return res
    return wraper
@air_company
def air_company():
    return finance_otchet()
print('финансовый отчет за первое полугодие компании "air"',air_company())

def  bank(func):
    def wraper():
        res = func()
        res.append('июль-8000')
        res.append('август-18000')
        res.append('сентябрь-28000')
        res.append('октябрь-80000')
        res.append('ноябрь-5000')
        res.append('декабрь-4000')
        return res
    return wraper

@bank
def bank():
    return finance_otchet()

print('финаансовый отчет банка за второе полугодтие:',bank())

    

