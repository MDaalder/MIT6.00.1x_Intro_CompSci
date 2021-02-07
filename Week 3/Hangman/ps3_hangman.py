# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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
    print(len(wordlist), "words loaded.")
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
#secretWord = 'apple' # chooseWord(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE..
    secretWordList = list(secretWord) # convert the secretWord into a list to make checking easier
    dummySecretWordList = secretWordList[:] # make a dummy variable to mutate and iterate through
    

    for letter in secretWordList: # iterate through the secret word letter by letter
        if letter in lettersGuessed: # if the letter in the secret word is in the list of letters guessed, then
            dummySecretWordList.remove(letter) # remove that letter from the dummy secret word
    
    if len(dummySecretWordList) > 0: # if there some letters left in the dummy secret word list after checking all the letters guessed
        return False # return false
    
    else: # if there are no letters left in the dummy secret word list after checking all the letters guessed, then the word was guessed!
        return True
   
    
#print('You have guessed the word?', isWordGuessed(secretWord, lettersGuessed))


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secretWordList = list(secretWord) # convert the secretWord into a list to make checking easier
    printedList = secretWordList[:]
    
    for n in range(len(secretWordList)): # this loop replaces all characters in the list with underscores
        printedList[n] = '_'
    
   
    for k in range(len(secretWordList)): # iterates over all the indices of the secret word
        if secretWordList[k] in lettersGuessed: # if the letter guessed is in the secret word
            printedList[k] = secretWord[k] # replace the _ at index k with the guessed letter

            
    return(' '.join(printedList)) # converts the remaining list into a string

# print(getGuessedWord(secretWord, lettersGuessed))

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string # imports string ?library?
    alphabet = string.ascii_lowercase # a string of the english alphabet
    alphabetList = list(alphabet) # convert to a list
    
    for letter in lettersGuessed: # iterates over the letters in the lettersGuessed list
        if letter in alphabetList: 
            alphabetList.remove(letter) # will remove all letters in lettersGuessed from the alphabet list
                        
    return(''.join(alphabetList))  #converts the list back into a string for return value
    
    
    
# print(getAvailableLetters(lettersGuessed))

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
    #global mistakesMade
    #global mistakesLeft
    
    global lettersGuessed # create a variable that is useable outside of this function
    lettersGuessed = [] # lettersGuessed will be a list populated with letters as they are guessed
    
    print('Welcome to the game, hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    print('-------------')
    
    mistakesLeft = 8    # number of mistakes that can be made before ending the game
    #import time # uncomment if you would like to implement pauses in this game.
           
    while mistakesLeft > 0: # while we still have guesses left, run the function
        
               
        if (isWordGuessed(secretWord, lettersGuessed)) is True: # if the win condition is met
            return(print('Congratulations, you won!'))
            #return
        
        print('You have', mistakesLeft, 'guesses left.') # prints the number of tries left
        print('Available letters:', getAvailableLetters(lettersGuessed))#, end='') # shows the user what letters they have left to choose from. Calls the function mentioned.
        guess = input('Please guess a letter: ') # asks the user for a guess
        guess = guess.lower() # converts the guessed letter into lower case, if an upper case letter was input
        
                
        if guess not in lettersGuessed and guess in list(secretWord): # if the guess is new, and it's in the secret word
            lettersGuessed.append(guess) # add the guessed letter to the list of guessed letters
            guessedWord = getGuessedWord(secretWord, lettersGuessed) # give the program a word to print that includes unguessed and guessed values
            print('Good guess:', guessedWord,'\n------------')
            #time.sleep(2) # can be used to implement a pause after this if statement is complete
            
        elif guess not in lettersGuessed: # if the guess is new, but is not in the secret word.
            lettersGuessed.append(guess) # add the guessed letter to the list of guessed letters
            mistakesLeft -= 1 # user made a mistake. Subtract 1 from guesses remaining
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            print('Oops! That letter is not in my word:', guessedWord,'\n------------')
            #time.sleep(2) # can be used to implement a pause after this if statement is complete
        
        else: # if the guess has been made previously
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed),'\n------------')
            #time.sleep(2) # can be used to implement a pause after this if statement is complete
        
    if mistakesLeft == 0: # if you run out of guesses
        return (print('Sorry, you ran out of guesses. The word was', secretWord))
            


secretWord = chooseWord(wordlist).lower() # populates the word to be guessed from a random list. Makes sure the word is lower case
hangman(secretWord) # invokes the function to start the game!
