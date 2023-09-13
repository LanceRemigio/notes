from numpy import random
list_first = random.randint(100, size = (9))
list_second = random.randint(100, size = (8))

print(list_first)
print(list_second)

upper = min(len(list_first), len(list_second))
inter_list = []
for i in range(upper):
    if(list_first[i] == list_second[i]):
        inter_list.append(list_first[i])

print(inter_list)
 

