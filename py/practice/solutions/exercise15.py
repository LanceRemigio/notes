
usr_in = input("Enter a string containing multiple words: ")

# result = usr_in.split()
# reversed_result = []

# for i in reversed(range(len(result))):
#         reversed_result.append(result[i])        

# final_result = " ".join(reversed_result)


# print(final_result)


def reversed_order (x):
    res = x.split()
    rev_result = [res[i] for i in reversed(range(len(res)))]
    return " ".join(rev_result)


print(reversed_order(usr_in))

