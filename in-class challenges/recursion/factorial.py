def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = 1
while True:
    print(factorial(num))
    num = num + 1