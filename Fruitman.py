# hamzah
# Mr.George Khoury

# import 
import random
import string
# 
# def function 
#
# start the game
def start_game():
    print (" The game is starting")
    check_guess()

# Random list of fruits 
def get_fruit():
    fruit = ['Apple', 'Orange' , 'Watermelon' , 'Pear' , 'Cherry'  , 'Strawberry' , 'Nectarine' , 'Grape']
    return random.choice(fruit).upper()

# prints the current state of the fruit (all visible, all hidden letters)
def print_fruit(fruit , used_letters):
        
    word_list = [letter if letter in used_letters else ' _ ' for letter in fruit]
    print('Current word: ', ' '.join(word_list))

# prints the information for the current game
def print_info(fruit):
    lenfruit = len(fruit)
    print('\nThe word contains:', lenfruit, 'letters?, and you have ' ,lenfruit , ' tries?. ')  

# checks a guesses provided by the user
def check_guess():

    fruit = get_fruit().upper()
    word_letters = set(fruit)
    used_letters = set() 
    tries = len(fruit)
    alphabet = set(string.ascii_uppercase)

    while len(word_letters) > 0 and tries > 0:
        print_info(fruit)
        print_fruit(fruit , used_letters)

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('good this is the right letter')
            else:
                tries = tries - 1  
                # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if tries == 0:
        print('You died, sorry. The word was', fruit)
    else:
        print('YAY! You guessed the word', fruit, '!!')

    
def read_fruits_list():
    pass

# Main --- Call the function
start_game()


