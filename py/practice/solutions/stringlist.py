

string_in = input("Enter a string: ")

test_string = []
actual_string = []

for i in reversed(range(len(string_in))):
    test_string.append(string_in[i])

for i in range(len(string_in)):
    actual_string.append(string_in[i])

if(test_string == actual_string):
    print("This string is a palindrome")
else: 
    print("This is not a palindrome")









