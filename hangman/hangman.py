from words import words
import random, string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        #print the used letters,to keep track of which words the user have used
        print('You have ' , lives ,"lives left and You have used these letters:", ' '.join(used_letters))
        #To let the user know what current word is and the progress
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list)) 
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1
                print('\nYour letter' ,user_letter,  'is not in the word\n')

        elif user_letter in used_letters:
            print("You have already used that character")
        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print('\nYou have used all your lives please try again.\n')
    else:
        print("\nYAYY!! you have guessed the word correctly\n")
    print('\n\nThe actual word is: ', word)

if __name__ == '__main__':
    hangman()