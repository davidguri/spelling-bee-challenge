import json
import string
import random
import time

# filter all 4 letter and above words
# pick a random letter
# filter all words with that letter in them
# create an array with these words
# from the array, pick 6 random letters
# take user input
# if user input lower than 4, contains other letters or doesn't contain main letter, it's wrong, else OK.
# make a cli

main_letter = random.choice(string.ascii_lowercase)
print("\nMain letter: " + main_letter)
# pick main letter

with open("words_dictionary.json", "r") as read_file:
    words = json.load(read_file)
    # print(words)
# import wordlist
    
word_dict = words
# set the word dictionary

def by_length(words):
    return [word for word in words if len(word) >= 4]
# filter words by length

by_length_words = by_length(word_dict)
# print(by_length_words)
# these are the allowed words (by length)
