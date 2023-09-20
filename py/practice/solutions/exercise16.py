import random
import string
import time

# Create a password generator

usr_in = input("Please specify how many letters, numbers, and punctuation marks you want in your password (seperated them by spaces): ")


num_in = usr_in.split()

num1 = int(num_in[0])
num2 = int(num_in[1])
num3 = int(num_in[2])


def pass_gen (k,x,z):
    i = 0
    j = 0
    l = 0
    tmp = []
    for i in range(i,k):
          tmp.append(random.choice(string.ascii_letters))
    for j in range(j,x):
          tmp.append(str(random.randint(1,9)))
    for l in range(l,z):
          tmp.append(str(random.choice(string.punctuation)))
    return "".join(tmp) 

st = time.time() 

et = time.time()

elapsed_time = et - st

print(pass_gen(num1,num2,num3))

print('Execution time: ', elapsed_time, 'seconds')

 






