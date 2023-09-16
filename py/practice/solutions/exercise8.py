# If rock and papers then rock wins 
# If scissors beats paper then scissors wins
# If paper beats rock then paper wins
# There has to be a better of way of doing this 
usr_command = input("Type 'enter' to start a game: ")

while usr_command == "enter":
    if usr_command == "quit":
        break
    else:
        player1 = input("Type rock, paper, or scissors: ")

        player2 = input("Type rock, paper, or scissors: ")

        if (player1 == "rock" and player2 == "paper"):
            print(player1 + " wins")
            usr_command = input("Start a new game?(type enter or quit): ")
            if (usr_command == "enter"):
                usr_command = "enter"
        elif (player1 == "paper" and player2 == "rock"):
            print(player2 + " wins")
            usr_command = input("Start a new game?(type enter or quit): ")
            if (usr_command == "enter"):
                usr_command = "enter"
        elif (player1 == "rock" and player2 == "scissors"):
            print(player1 + " wins")
            usr_command = input("Start a new game?(type enter or quit): ")
            if (usr_command == "enter"):
                usr_command = "enter"
        elif (player1 == "scissors" and player2 == "rock"):
            print(player2 + " wins")
            usr_command = input("Start a new game?(type enter or quit): ")
            if (usr_command == "enter"):
                usr_command = "enter"
        elif(player1 == "paper" and player2 == "scissors"):
            print(player2 + " wins")
            usr_command = input("Start a new game?(type enter or quit): ")
            if (usr_command == "enter"):
                usr_command = "enter"
        elif(player1 == "scissors" and player2 == "paper"):
            print(player1 + " wins")
            usr_command = input("Start a new game?(type enter or quit): ")
            if (usr_command == "enter"):
                usr_command = "enter"
        else:
            print("it is a draw")
            usr_command = input("Start a new game?(type enter or quit): ")
            if (usr_command == "enter"):
                usr_command = "enter"




