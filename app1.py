import json
from difflib import SequenceMatcher
from difflib import get_close_matches

# loads static data set from json file
data = json.load(open("data.json"))

# functionality to match user input to data as key
# returns value for matched key
# checks several conditions to improve user experience
def lookup(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yesno = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead? Enter Y or N.").lower()
        if yesno == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yesno == "n":
            return "The word does not exist, please double check it."
        else:
            return "We didnt understand your entry."
    else:
        return "Word does not exist. Please try another word."


# takes user input into variable so it can be passed to lookup function
word = input("Enter a word to look up its definition: ")

# calls lookup function with user input passed in and assigns to output variable
output = lookup(word)

# conditional check on the result to print all items in a list if word matches
# if word does not match, a string is returned and the loop is skipped, which
# only prints out the string
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)