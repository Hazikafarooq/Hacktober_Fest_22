secret_number = int(input())
num_tries = int(input())

def guessing_game(sn, num_tries):
    if num_tries < sn:
        return("Try again! Your guess is too low.")
        guessing_game(sn, num_tries)
    elif num_tries > sn:
        return("Try again! Your guess is too high.")
        guessing_game(sn, num_tries)
    elif num_tries == sn:
        return("Congratulations, you won! You guessed the secret number")
    else:
        return("Sorry, you lose! Too many wrong guesses.")