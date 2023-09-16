

usr_in = int(input("Enter a positive integer: "))

def check_prime (num):
    div_list = [i for i in range(1, num + 1) if (num%i == 0)]
    div_prime = [1,num]
    if (div_prime == div_list):
        return "This integer is prime"
    else:
        return "This integer is not prime"

print(check_prime(usr_in))
