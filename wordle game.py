import time
import random


# Initializing variables/lists

with open("wordle_words.txt", "r") as file:
    word_list = file.read().splitlines()

with open('wordle_answers.txt', 'r') as file:
    answers = file.read().split()

remain = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
discovered = []
used = []
board = []
temp = []

word = None
player_guess = None
player_victory = None

turns = 0
tries = 6

'''
Any variables with "_out" are altered to be suitable for output

'''


# Defining functions

def intro():
    
    print('Greetings! Welcome to the Wordle Game!')
    print('\nYou will have to try to guess a random word with 5 letters.')
    print('You can do this by typing in a 5 letter word.')
    
    print('\nIf any letters in the word you typed in do not appear in the random word,')
    print('they will have an "X" in front of them.')
    print('\nIf any letters are present in the random word but not in the right position,')
    print('they will have a "?" in front of them.')
    print('\nIf any letters are present and in the right position,')
    print('they will remain unchanged.\n')
    
    print('Legend: aX = a is not in the word')
    print('        a? = a is in the word, but in the wrong position')
    print('        a  = a is in the word and in the right position')
    print("\nYou'll only get 6 tries, so good luck!")

    input('Press enter to begin...')


def display_board(board):

    index = 0
    
    for x in board:

        print(board[index])
        index += 1
    

def game():

    global word

    print('\n--------------------------------------------------------------------------------------')
    print('(Start)')
    print('I am thinking of a word...')
    time.sleep(1)

    word = list(random.choice(answers).lower())
    
    while player_victory == None:
        
        make_guess()


    # End
    
    time.sleep(1)
    
    print('\n--------------------------------------------------------------------------------------')
    print('(End Result)')

    if player_victory == 'Y':   # if player wins

        if tries == 5:
            print('Congratulations on guessing the word on your first try! Crazy luck!')

        elif tries == 0:
            print('Close call! You guessed the word on your final try!')

        else:
            print(f'Well done on guessing the word in {tries} tries!')

    else:   # if player loses

        print('Game over! You ran out of tries!')
        print('The word was:', ''.join(word))

    time.sleep(1)

        

def make_guess():

    global turns, tries, player_victory, discovered

    turns += 1
    tries -= 1
    
    print('\n--------------------------------------------------------------------------------------')
    print(f'(Turn #{turns})')
    player_guess = str(input('Enter your guess (5 letters): ')).lower().strip()

    while player_guess not in word_list:    # if player_guess is invalid

        if len(player_guess) < 5:
            player_guess = str(input('Not enough letters! Enter your guess (5 letters): ')).lower().strip()

        elif len(player_guess) > 5:
            player_guess = str(input('Too many letters! Enter your guess (5 letters): ')).lower().strip()

        else:
            player_guess = str(input('Not a real word! Enter your guess (5 letters): ')).lower().strip()

    player_guess = list(player_guess)   # easier to compare


    # Updates letter lists
    
    for x in range(5):

        if player_guess[x] in remain:
             
            remain.remove(player_guess[x])
            used.append(player_guess[x])
             

    # Compares player_guess and word   
        
        if player_guess[x] == word[x]:
            
            temp.append(player_guess[x] + ' ')
            discovered.append(player_guess[x])

        elif player_guess[x] in word:   # in wrong spot, but in word
            
            temp.append(player_guess[x] + '?')
            discovered.append(player_guess[x])

        else:
            temp.append(player_guess[x] + 'X')


    discovered = list(set(discovered))   # removes duplicates

    # Makes suitable for output
    
    discovered_out = str(sorted(discovered)).replace("'","")
    remain_out = str(remain).replace("'","")       
    used_out = str(sorted(used)).replace("'","")
    temp_out = ' |  '.join(temp)

    board.append(temp_out)

    print("\nHere's the word:", temp_out, '\n')

    display_board(board)
        
    print("\nLetters you haven't used:", remain_out)
    print('Used letters:', used_out, '\n')

    if discovered != []:    # only shows letters in word when the list is not empty
        print('Letters discovered:', discovered_out)
    
    if player_guess == word:

        player_victory = 'Y'
        return

    elif tries == 0:

        player_victory = 'N'
        return
        
    print('Tries left:', tries)

    temp.clear()     


# Running game

intro()
    
game()


print('Thanks for playing!')
time.sleep(1.5)

exit()
