import random
def number_guessing_game():
    print("Welcome To The Number Guessing Game!")
    print("I'm Thinking Of A Number Between 1 And 100.")

    secret_number = random.randint(1,100)
    attempts = 0
    
    while True:
        guess = int(input("Take A Guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too Low!")
        elif guess > secret_number:
            print("Too High!")
        else:
            print(f"Contratulations! You Have Guessed The Secret Number, {secret_number} In {attempts} Attempts!")
            break

number_guessing_game()