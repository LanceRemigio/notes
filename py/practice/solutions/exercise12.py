
from numpy import random
list_num = random.randint(100, size = (9))

def end_list (x):
    return [x[0], x[-1]]

print(end_list(list_num))



