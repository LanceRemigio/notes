def square (x):
    """
    Square each element of a list and returns each element of 
    the list but squared
    """
    return [x[i]**2 for i in x]

a_list = [2,3,4,5]

print(square(a_list))




