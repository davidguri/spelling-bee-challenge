import json

# import wordlist from github.com/dwyl/english-words
# filter all 4 letter and above words
# pick a random letter
# filter all words with that letter in them
# create an array with these words
# from the array, pick 6 random letters
# take user input
# if user input lower than 4, contains other letters or doesn't contain main letter, it's wrong, else OK.
# make a cli

with open("words_dictionary.json", "r") as read_file:
    words = json.load(read_file)
    print("json load successful")
    

