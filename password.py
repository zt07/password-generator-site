from english_words import english_words_set as words
from random import choice


words = filter(lambda word: word<=5, words)
#Penis




# Generate a random password of the given length
def generate_password(length):
    password = ''
    for i in range(length):
        password += choice(words)
        password+= ' '
    return password

