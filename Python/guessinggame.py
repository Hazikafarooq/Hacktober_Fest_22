def guessing_game(secret_number, num_tries):
        for num_tries in range(5):
            player_guess = int(input())
            if num_tries+1 < 5:
                if player_guess == secret_number:
                    print("Attempt number "+str(num_tries+1)+"\nCongratulations, you won! You guessed the secret number "+ str(secret_number)+" in "+str(num_tries+1)+" guesses.")
                    exit()
                elif player_guess == ' ':
                    print("\n")
                elif player_guess < secret_number:
                    print("Attempt number "+str(num_tries+1)+"\nTry again! Your guess is too low.")
                else:
                    print("Attempt number "+str(num_tries+1)+"\nTry again! Your guess is too high.")   
            else:
                if player_guess == secret_number:
                    print("Attempt number "+str(num_tries+1)+"\nCongratulations, you won! You guessed the secret number "+ str(secret_number)+" in 5 guesses.")
                else:
                    print("Attempt number 5\nSorry, you lose! Too many wrong guesses.")  
            
                
            
secret_number = int(input())           

guessing_game(secret_number, 1)
