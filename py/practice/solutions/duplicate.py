from numpy import random
list_first = random.randint(100, size = (9))
list_second = random.randint(100, size = (8))

# list_first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list_second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list_first)
print(list_second)

range1 = len(list_first)
range2 = len(list_second)

inter_list = []

for i in range(min(range1, range2)):
    for j in range(min(range1, range2)):
        if (list_first[i] == list_second[j]):
            inter_list.append(list_first[i])

print(inter_list)
 

