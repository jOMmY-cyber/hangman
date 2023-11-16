import random
from words import abc

def get_word():
    word = random.choice(abc)
    return word.upper()
# word = get_word()
# print('word=',word)
# print('len word=',len(word))
# print('mul len=', 'c'*len(word))

def play(word):
    word_completion = '_' *len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!!")
    print(display_hangman(tries))
    word_completion2 = ' '.join(word_completion)
    print(word_completion2, '('+str(len(word_completion))+' letters)')
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) ==1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess , "is in the word!!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
            guessed_ = guessed_letters
            print('you already guessed = ', ','.join(guessed_))
        elif len(guess) ==len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you alredy guessed the word")
            elif guess != word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("not a valid guess.")
        print(display_hangman(tries))
        word_completion2 = ' '.join(word_completion)
        print(word_completion2, '('+str(len(word_completion))+' letters)')
        print("\n")
    if guessed == True:
        print('you win')
    else: 
        print('you lose')
        print('word = ',word)
        
def display_hangman(tries):
    stages = [ """
                    
                    --------
                    |       |
                    |       o
                    |      \\|/
                    |       |
                    |      / \\
                    -
                """,
                """
                    --------
                    |       |
                    |       o
                    |      \\|/
                    |       |
                    |      / 
                    -
                """,
                """
                    --------
                    |       |
                    |       o
                    |      \\|/
                    |       |
                    | 
                    -       
                """,
                """
                    --------
                    |       |
                    |       o
                    |      \\|
                    |       |
                    |          
                    -
                """,
                """
                    --------
                    |       |
                    |       o
                    |       |
                    |       |
                    |       
                    -
                """,
                """
                    --------
                    |       |
                    |       o
                    |       
                    |       
                    |
                    -
                """,
                """
                    --------
                    |       |
                    |       
                    |       
                    |      
                    |
                    -
                """            
    ]
    return stages[tries]

# a = input('test:')
# print(a)
# print(type(a))

print('finish import')
wordtest = get_word()
play(wordtest)