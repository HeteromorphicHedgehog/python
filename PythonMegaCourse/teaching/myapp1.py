import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def getDefinition(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys(),cutoff = 0.8)) > 0:
        yn = input("We were not able to find a match for '{:^2}'.\nThe closet match to your entry is '{:^2}'? Is this what you meant? Enter 'Y' for yes, or 'N' for no: " .format(w, get_close_matches(w, data.keys())[0]))
        if yn.lower() == 'y':
            return data[get_close_matches(w,data.keys(),cutoff=0.8)[0]]
        elif yn.lower() == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry, it was not 'y' or 'n'."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = getDefinition(word)

if type(output) == list:
    print("")
    count = 1
    for item in output:
        print("{:>2}. {}".format(count,item))
        count += 1
    print("")
else:
    print(output)
