from numpy import random
# y_1 = random.randint(100, size = (8))
# x_1 = random.randint(100, size = (9))

x_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
y_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# print(x_1)
# print(y_1)

# r1 = len(x_1)
# r2 = len(y_1)


# for i in range(min(range1, range2)):
#     for j in range(min(range1, range2)):
#         if (list_first[i] == list_second[j]):
#             inter_list.append(list_first[i])

# print(inter_list)
# Using list comprehensions 
# inter_list = [list_first[i] for i in range(min(range1, range2)) for j in range(min(range1, range2)) if (list_first[i] == list_second[j])]
# print(inter_list)

def clean_up (x):
    tmp = []
    for i in x:
        if i not in tmp:
            tmp.append(i)
    return tmp


def intersection (x,y):
   return [
           x[i] for i in range(min(len(x), len(y))) 
            for j in range(min(len(x),len(y))) 
            if (x[i] == y[j])
           ] 



# x_clean = clean_up(x_1)
# y_clean = clean_up(y_1)

# print(x_clean)
# print(y_clean)


# print(intersection(x_clean,y_clean))





