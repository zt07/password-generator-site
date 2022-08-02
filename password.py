from english_words import english_words_alpha_set as words
from random import choice


words = list(filter(lambda x: len(x) < 5, words))




# Generate a random password of the given length
def generate_password(length):
    password = ''
    for i in range(length):
        password += choice(words)
        password+= ' '
    return password

