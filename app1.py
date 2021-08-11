import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

# basic functionality to match user input to data as key
# returns value for matched key
# implements basic error handling
def lookup(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "Word does not exist. Please try another word."


word = input("Enter a word to look up its definition: ")
print(lookup(word))
