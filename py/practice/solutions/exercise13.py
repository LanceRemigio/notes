# Fibonacci
# Write a program that asks the user how many fibonacci numbers to generate and then generates them

num_in = int(input("Please enter a positive integer to generate the fibonacci numbers: "))

# def fib (x):
#     if (x < 1):
#         return 1
#     else:
#         return fib(x-1) + x


# print(fib(num_in))

def printNum (n):
    if (n > 0):
        printNum(n-1)
        print(n, end = '')

print(printNum(num_in))
