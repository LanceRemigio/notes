from numpy import random

num_range = int(input("Please enter the upper bound of list: ")) # Picks upper bound of numbers
num_list = random.randint(10,size = (8)) # Generates a random list of numbers
less_five = [] # Initializing empty list 

# written using a regular for loop
for i in range(len(num_list)):
    if (num_list[i] <= num_range):
        less_five.append(num_list[i])

print(less_five)





