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


