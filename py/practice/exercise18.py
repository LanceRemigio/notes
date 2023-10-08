# For every digit guessed correctly -> user gets a cow
# For every digit guessed correctly but in the wrong the place -> user gets a bull
# If all the digits have been guessed correctly -> end the game
# Tell the user how many cows and bulls they have at the end
import random 

num = str(random.randint(1000,9999))

print(num)

usr_command = input("Type 'enter' to start a game: ")

cow = 0
bull = 0

while usr_command == "enter":
    
    usr_in = input("Enter a number: ")
    
    if usr_in == num:
        print("You have " + str(cow) + " cows and bulls " + str(bull))
        break
    
    guess = [i for i in usr_in]
    num_to_guess = [i for i in num]

    for i in range(min(len(guess) , len(num_to_guess))): # convert this into a function later
        for j in range(min(len(guess), len(num_to_guess))):
            if (guess[i] == num_to_guess[j] and i == j):
                cow += 1 
            elif (guess[i] == num_to_guess[j] and i != j):
                bull +=1
    

    


















