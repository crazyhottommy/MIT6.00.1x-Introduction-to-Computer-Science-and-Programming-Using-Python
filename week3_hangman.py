# 6.00 Problem Set 3
# 
# Hangman game: https://en.wikipedia.org/wiki/Hangman_(game)
#

## to start play this game, put the script in the same directory as the words.txt file
## and then: python week3_hangman.py

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    word_list = []
    for letter in secretWord:
        word_list.append(letter)
    ## list is mutable, get a copy of the list
    for letter in word_list[:]:
        if letter in lettersGuessed:
            word_list.remove(letter)
    if len(word_list) == 0:
        return True
    elif len(word_list) > 0:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word_list = []
    for letter in secretWord:
        word_list.append(letter)
    ## list is mutable, get a copy of the list
    guessedword_list=[]
    for letter in word_list[:]:
        if letter in lettersGuessed:
            guessedword_list.append(letter)
        else:
            guessedword_list.append("_ ")
    return "".join(guessedword_list)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    all='abcdefghijklmnopqrstuvwxyz'
    alpha_list=[]
    for letter in all:
        alpha_list.append(letter)
    for letter in alpha_list[:]:
        if letter in lettersGuessed:
            alpha_list.remove(letter)
    return "".join(alpha_list)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print "Welcome to the game Hangman!"
    print "I am thinking of a word that is %s letters long" % str(len(secretWord))
    print "-----------"

    guess_num = 8
    lettersGuessed=[]
    while guess_num > 0:
        print "You have %s guesses left" % str(guess_num)
        print "Available Letters: " + getAvailableLetters(lettersGuessed)
        guess = raw_input("Please guess a letter: ")
        guess = guess.lower()
        if isWordGuessed(secretWord, lettersGuessed):
            print "Congratulations, you won!"
            break
        else:
            if guess not in lettersGuessed:
                lettersGuessed.append(guess)
                # print lettersGuessed
                if guess in secretWord:
                    print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
                    print "-----------"
                    if isWordGuessed(secretWord, lettersGuessed):
                        print "Congratulations, you won!"
                        break
                elif guess not in secretWord:
                    print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
                    print "-----------"
                    guess_num -= 1
            elif guess in lettersGuessed:
                print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
                print "-----------"
    print "Sorry, you ran out of guesses. The word was %s." % secretWord


def main():
    wordlist = loadWords()
    secretWord = chooseWord(wordlist)
    hangman(secretWord)

if __name__ == '__main__':
    main()
    
