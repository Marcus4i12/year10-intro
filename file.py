from collections import *

with open(r"c:\Users\training.user\Documents\words.txt", "r") as f:
    words = f.read().split()

letter_counts = {}
for word in words:
    word = word.lower()         #makes all letters lowercase
    for letter in word:
        if letter not in letter_counts:
            letter_counts[letter] = 0       #none letters removed
        letter_counts[letter] += 1
sorted_letters = sorted(letter_counts.items(), key=lambda x: x[0])          #sorts in order of alphabet
for letter, count in sorted_letters:
    print(f"{letter}: {count}")