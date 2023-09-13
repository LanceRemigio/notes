

num_in = int(input("Enter any positive integer: "))


def check_even(num):
    if( num % 2 == 0 ): 
        return  "The number is even."
    else:
        return "The number is odd." 
    
    
print(check_even(num_in)) 
