# Input user guess (4 digit number)
# For every digit guessed correctly in the right place, the user gets a cow
# For every digit quess correctly but in the wrong place, the user gets a bull
# Keep track of how many guesses by telling the user how many "bulls" and "cows" they have.
# Once the user guesses the number correctly, the game ends.

# usr_in = int(input("Enter a number: "))

import random

num = str(random.randint(1000,9999))

print(num)

usr_command = input("Type 'enter' to start a game: ")

cow = 0
bull = 0


while usr_command == "enter":

    usr_in  = input("Enter a number: ")

    if usr_in == num:
        break
    
    guess = [i for i in usr_in]
    num_to_guess = [i for i in num]
    
    x = len(num)
    
    y = len(num_to_guess)

    for i in range(min(x,y)):
        for j in range(min(x,y)):
            if (guess[i] == num_to_guess[j] and i == j):
                cow +=1
            elif (guess[i] == num_to_guess[j] and i != j):
                bull +=1
                cow -= 1

    print("You have " + str(cow) + " cows and " + str(bull) + " bulls." ) 
