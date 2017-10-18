# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    partial_guess = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            partial_guess += letter
        else:
            partial_guess += "_ "
    return partial_guess



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    available_letters = ""
    for letter in all_letters:
        if letter not in lettersGuessed:
            available_letters += letter
    return available_letters


def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.
    """
    available_guesses = 8
    letters_guessed = []
    available_letters = getAvailableLetters(letters_guessed)
    partial_guess = getGuessedWord(secretWord, letters_guessed)

    print("Welcome to the game, Hangman!")

    # Let the user know how many letters the secretWord contains
    print("I am thinking of a word that is", len(secretWord), "letters long.")

    # Stop running when no guess is left
    while available_guesses > 0:
        print("-------------")
        print("You have", available_guesses, "guesses left")

        # Display available letters after the last guess
        print("Available letters:", available_letters)

        # Ask the user to supply one guess (i.e. letter) per round
        guessed_letter = input("Please guess a letter: ")

        # If letter was already guessed (not in available letters anymore),
        # keep no. of remaining guesses the same and re-ask for new guess
        if guessed_letter not in available_letters:
            print("Oops! You've already guessed that letter:", partial_guess)

        # If letter was not yet guesses (still in available letters),
        # update the list of letters guessed and remove it from the list of available letters
        else:
            letters_guessed.append(guessed_letter)
            available_letters = getAvailableLetters(letters_guessed)

            # If guessed letter is in secret word, display the partial guess with the new letter appearing
            # If the word is fully guessed, congratulate user and break out of function
            if guessed_letter in secretWord:
                partial_guess = getGuessedWord(secretWord, letters_guessed)
                print("Good guess:", partial_guess)
                if isWordGuessed(secretWord, letters_guessed):
                    print("-------------")
                    print("Congratulations, you won!")
                    break

            # If guessed letter is not in secret word, reduce the available guesses by 1
            # Thereafter, if no more guess is available, print consolation message and loop ends
            else:
                print("Oops! That letter is not in my word:", partial_guess)
                available_guesses -= 1
                if available_guesses == 0:
                    print("-------------")
                    print("Sorry, you ran out of guesses. The word was", secretWord, ".")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = chooseWord(wordlist).lower()
print(secretWord)
hangman(secretWord)
