from collections import Counter
my_file = open(r"c:\Users\training.user\Documents\words.txt", "r")
counter = Counter(my_file.read())
counter['a']
print(counter)