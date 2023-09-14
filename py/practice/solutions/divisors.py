
num_in = int(input("Please enter a postive integer: "))

divisor_list = []

for i in range(1,num_in + 1):
    if (num_in%i == 0):
        divisor_list.append(i)
print(divisor_list)
