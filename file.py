from collections import *
import string

with open(r"c:\Users\training.user\Documents\words.txt", "r") as f:
    words = f.read().split()

letter_counts = {}
for word in words:
    word = word.upper()         #makes all letters lowercase
    for letter in word:
        if letter not in letter_counts:
            letter_counts[letter] = 0       #none letters removed
        letter_counts[letter] += 1
sorted_letters = sorted(letter_counts.items(), key=lambda x: x[0])          #sorts in order of alphabet
for letter, count in sorted_letters:
    if letter not in string.punctuation and letter not in string.digits:       #removes numbers/symbols
        print(f"{letter}: {count}")