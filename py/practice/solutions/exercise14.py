# import random


# x_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# y_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# list_second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x_1 = [1,1,2,3,4,7,9,7]

# def check_duplicates (x): # remove duplicates using sets
#     uniq_num = set()
#     for i in range(len(x)):
#         uniq_num.add(x[i])
#     return uniq_num


# print(check_duplicates(x_1))

# def check_duplicates (x):
#     return [i for n, i in enumerate(x) if i not in x[:n]] # Using list comprehension to return a list with unique elements


# def check_duplicates(x):
#     tmp = []
#     for i in x:
#         if i not in tmp:
#             tmp.append(i)
#     return tmp




# def check_duplicates (x):                    
#     tmp = []
#     for n,i in enumerate(x):
#         if i not in x[:n]:
#             tmp.append(i)
#     return tmp


    # for i in range(len(x)):
    #     for j in range(i+1, len(x)):
    #         if (x[i] == x[j]):
    #              x.remove(x[j])
    #              return x
    #         else:
    #             return "There are no duplicates"
# print(check_duplicates(x_1))




