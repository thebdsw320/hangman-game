import os
import random
import time

def welcome():
    name_input = input('What\'s your name? ')
    print(f'Hello {name_input}, welcome to HANGMAN GAME!')
    time.sleep(1)
    print(f'Time to play HANGMAN {name_input}')
    time.sleep(1)
    print('Start guessing your first word!')

def pick_a_word():
    with open('/mnt/c/Users/norma/OneDrive/Escritorio/Python/Platzi Python/Python Intermedio/data.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        word_list = content.splitlines()
        r_word = random.choice(word_list)
        u_word = r_word.upper()
    return u_word

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_characters = []
    guessed_words = []
    tries = 6
    print(display_hangman(tries))
    
    while not guessed and tries > 0:
        guess = input('Please enter a word or a letter: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_characters:
                print(f'You guessed that letter ({guess}) already')
            elif guess not in word:
                print(f'{guess} is not in the secret word')
                tries -= 1
                guessed_characters.append(guess)
            else:
                print(f'Great!, {guess} is in the secret word')
                word_as_list = list(word_completion)
                guessed_characters.append(guess)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == 0:
            print('Please enter something!, like a or b, idk :/')
            tries -= 1
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f'You already guessed the word {guess}')
            elif guess != word:
                print(f'{guess} is not the word')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = guess
        else:
            print(f'Oh no! {guess} is incorrect, please try again...')
            tries -= 1
        print(display_hangman(tries))
        time.sleep(1)
        print(word_completion)
        print('\n')

    if guessed:
        print(f'Congrats! You won, the word was {guess}')
    else:
        print(f'Sorry!, you ran out of tries, the correct word was {word}')
# indices = [i for i, letter in enumerate(word) if letter == guess]


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


if __name__ == '__main__':
    welcome()
    word = pick_a_word()
    play(word)