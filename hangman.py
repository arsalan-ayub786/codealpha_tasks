import random

# Predefined list of words
words = ["python", "hangman", "computer", "keyboard", "program"]

# Randomly select one word
word = random.choice(words)

# Track guessed letters
guessed_letters = []

# Track wrong guesses
wrong_guesses = 0
max_wrong_guesses = 6

# Track if game is won
game_won = False

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")

while wrong_guesses < max_wrong_guesses and not game_won:
    print("\nWord: " + display_word(word, guessed_letters))
    print("Wrong guesses left: " + str(max_wrong_guesses - wrong_guesses))
    
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    guessed_letters.append(guess)
    
    if guess in word:
        print("Correct!")
        if all(letter in guessed_letters for letter in word):
            game_won = True
    else:
        wrong_guesses += 1
        print("Wrong guess!")

if game_won:
    print("\nCongratulations! You guessed the word: " + word)
else:
    print("\nGame Over! The word was: " + word)