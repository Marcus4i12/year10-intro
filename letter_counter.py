from collections import *
import string

with open(r"c:\Users\training.user\Documents\words.txt", "r") as f:
    words = f.read().upper()        

    letters = Counter(words)

    sorted_letters = dict(sorted(letters.items()))              #sorts alphabetically
    for letter, count in sorted_letters.items():
        if letter not in string.punctuation and letter not in string.digits:        #only keeps letters
            print(f'{letter} : {count}')