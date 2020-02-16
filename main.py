import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def dictionary(word):
    if word in data :
        return data[word]
    elif len(get_close_matches(word,data.keys(),cutoff = 0.8)) > 0 :
         print ("Do you mean %s instead?" % get_close_matches(word,data.keys(),cutoff = 0.8)[0])
         choice = input("Press [Y] for Yes And [N] for no :")
         if choice == 'Y' or choice == 'y':
             return data[get_close_matches(word,data.keys(),cutoff = 0.8)[0]]
         else:
             return "Sorry No result"
    else:
        return "Word Does Not Exist, Please double check it"

programLoop = 'Y'
while programLoop == 'Y' or programLoop == 'y':
     print(" WELCOME TO ENGLISH DICTIONARY")
     word = input("Enter Your Word : ").lower()
     output=dictionary(word)
     if type(output) == list:
         for i in output:
             print(i)
     else :
          print(output)
     programLoop = input("Do you want to Enter another word? [Y] for YES [N] for NO:")
