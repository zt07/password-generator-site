from random import choice
from english_words import get_english_words_set as words


set = words(['web2'])
#only 5 letter words or less are allowed
words = [word for word in set if len(word) <= 5]


# Generate a random password of the given length
def generate_password(length):
    # Generate a random password of random words that is less then the given length in total
    password = ''
    while True:
        password += choice(words) + '-'
        if len(password) >= length:
            return password[:-5]