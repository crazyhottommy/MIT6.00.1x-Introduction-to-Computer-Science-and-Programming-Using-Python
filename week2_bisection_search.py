
##In this problem, you'll create a program that guesses a secret number!

##The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
## The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, 
## the computer will guess the user's secret number!

low = 0
guess = 50
high = 100
print "Please think of a number between 0 and 100!"
while True:
    print "Is your secret number %s?" %str(guess)
    ans = raw_input("Enter 'h' to indicate the guess is too high.\
    Enter 'l' to indicate the guess is too low. \
    Enter 'c' to indicate I guessed correctly. ")

    if ans not in ["h", "l", "c"]:
        print "Sorry, I did not understand your input."
    elif ans == 'h':
        low = low
        high = guess
        guess = low + (high-low)/2
    elif ans == "l":
        low = guess
        high = high
        guess = low + (high -low)/2
    elif ans == "c":
        print "Game over, Your secret number was %s" %str(guess)
        break
