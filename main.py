import json
import string
import random

# filter all words with that letter in them
# create an array with these words
# from the array, pick 6 random letters
# take user input
# if user input lower than 4, contains other letters or doesn't contain main letter, it's wrong, else OK.
# make a cli

# txt_file = "words.txt"
# word_py_dict = {}

# with open(txt_file) as fh:
#     for line in fh:
#         command, description = line.strip().split(None, 1)
#         word_py_dict[command] = description.strip()
        
# output_file = open("words_dictionary.json", "w")
# json.dump(word_py_dict, output_file, indent = 4, sort_keys = False)
# output_file.close()
# the code above was made to convert the words.txt file to json

with open("words.txt", "r") as read_file:
    words = read_file.read()
    print("txt load successful")
    
word_dict = words

def by_length(words):
    return [word for word in words if len(word) >= 4]

allowed_words = by_length(word_dict)
print(allowed_words)

main_letter = random.choice(string.ascii_uppercase)
print("Main letter: " + main_letter)
