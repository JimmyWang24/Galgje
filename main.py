# All stored variables
lives_remaining = 6

secret_word = []
blank_word = []

guessed_letters = []
wrong_letters = []


# The main fuction. Clears variables when player chooses to play again. Lets the 1st player write a word. Loops the game using the two functions below and ends the game if the player guesses correct or is out of lives.
def main_game():

    # Allows change of variables outside the function and resets them.
    global lives_remaining, guessed_letters, wrong_letters
    lives_remaining = 6
    guessed_letters = []
    wrong_letters = []

    #Lets player choose a secret word. Hides it with 100 blanks and then shows the word in blanks
    secret_word = list(input("Player 1, please enter a secret word: ").lower())
    print("\n" * 100)
    blank_word = list("_" * len(secret_word))

    # Main loop. Shows progression of the word and calls to the other functions
    while lives_remaining > 0 and secret_word != blank_word:
        print("Guess the word: "+"".join(blank_word))
        guessed_letter = check_letter(guessed_letters)
        check_correct(guessed_letter, secret_word, blank_word, wrong_letters)

    # Ends this round and asks if the player wants to play again
    if secret_word == blank_word:
        print(f"You win! The secret word is: {"".join(secret_word)}")
    else:
        print("You're out of lives. You lost. :(")
    play_again()


# This function checks if the player entered a valid single letter
def check_letter(guessed_letters):
    while True:
        print()
        letter = (input("Enter a letter: ").lower())
        if len(letter
               ) != 1:
            print("Please enter a single letter")
        elif not letter.isalpha():
            print("Please enter a letter")
        elif letter in guessed_letters:
            print("You already entered that letter")
        else:
            guessed_letters.append(letter)
            return letter


# This function checks if the entered letter is or isn't in the secret word. If it is, it'll update the word shown to the player. If not, substract 1 life and show the remaining lives.
def check_correct(letter, secret_word, blank_word, wrong_letters):
    global lives_remaining

    if letter in secret_word:
        for index in range(len(secret_word)):
            if secret_word[index] == letter:
                blank_word[index] = letter
        print(f"Correct! The letter {letter} is in the secret word.")
    else:
        lives_remaining -= 1
        wrong_letters.append(letter)
        wrong_letters = ', '.join(f"'{letter}'" for letter in wrong_letters)
        print(f"Wrong. The letter '{letter}' is not in the secret word.")
        print(f"Wrong letters: {wrong_letters}")
        print(f"You have {lives_remaining} lives remaining.")


# Return to the main loop by calling main function or exit the game
def play_again():
    replay_choice = input("Would you like to play again? Please enter 'yes' or 'no': ")
    while True:
        if replay_choice == 'yes':
            main_game()
        elif replay_choice == 'no':
            print("Thanks for playing!")
            exit()
        else:
            replay_choice = input("Please enter 'yes' or 'no'")



# Main game
print("Welcome to Hangman!")
print("All your words will be converted to lowercase")

main_game()