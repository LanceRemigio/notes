import random

# generate a number between 1 and 9 (inclusive)
# Ask the user to guess the number, then thell them whether they guessed too low, too high, or exactly right.

def intersection (x,y):
   return [
           x[i] for i in range(min(len(x), len(y))) 
            for j in range(min(len(x),len(y))) 
            if (x[i] == y[j])
           ] 



num = random.randint(1,9)
guess = 0

usr_command = input("Type 'enter' to start a game: ")
while usr_command == "enter":
    num_guess = input("Enter a number between 1 and 9: ")
    if num_guess == "quit":
        break
    num_guess = int(num_guess)
    guess += 1
    if (num_guess > num):
        print("Too big!")
    elif (num_guess < num):
        print("Too small!")
    else:
        print("Right!")
        print("You only took " + str(guess) + "guesses")


