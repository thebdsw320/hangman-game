import os
import random
import time

forbidden_chars = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}

def welcome():
    name_input = input('What\'s your name? ')

    HANGMAN_TITLE = """██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
            an Open Source Project (by @bdsw320 -AMGD-)"""   

    print(f'Hello {name_input}, welcome to')
    time.sleep(1)
    print('\n'*2)
    print(HANGMAN_TITLE)
    print('\n'*2)
    print(f'Time to play {name_input}')
    time.sleep(1)
    print('Start guessing your first word!')

def pick_a_word():
    with open('data.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        word_list = content.splitlines()
        r_word = random.choice(word_list)
        u_word = r_word.upper()
    return u_word

def catch_chars(word):
    for char, r_char in forbidden_chars.items():
        if char in word:
            word = word.replace(char, r_char)
    return word

def play(word):
    word = catch_chars(word)
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
                print('If you want to stop playing, please put Ctrl+C')
            elif guess not in word:
                print(f'{guess} is not in the secret word')
                tries -= 1
                guessed_characters.append(guess)
            else:
                print(f'Great!, {guess} is in the secret word')
                print('If you want to stop playing, please put Ctrl+C')
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
            print('If you want to stop playing, please put Ctrl+C')
            tries -= 1
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f'You already guessed the word {guess}')
                print('If you want to stop playing, please put Ctrl+C')
            elif guess != word:
                print(f'{guess} is not the word')
                print('If you want to stop playing, please put Ctrl+C')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = guess
        else:
            print(f'Oh no! {guess} is incorrect, please try again...')
            print('If you want to stop playing, please put Ctrl+C')
            tries -= 1
        print(display_hangman(tries))
        time.sleep(1)
        print(word_completion)
        print('\n')

    if guessed:
        print(f'Congrats! You won, the word was {word}')
    else:
        print(f'Sorry!, you ran out of tries, the correct word was {word}')


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

def main():
    welcome()
    word = pick_a_word()
    play(word)

if __name__ == '__main__':
    main()
