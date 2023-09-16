# list comprehensions

# years_of_birth = [1990, 1991, 1990, 1992, 1991]

# ages = []

# for year in years_of_birth:
#     ages.append(2014-year)

# Using list comprehensions
# ages = [2014 - year for year in years_of_birth]

# print(ages)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list_even = [a[i] for i in range(len(a)) if a[i] % 2 == 0]
print(list_even)



