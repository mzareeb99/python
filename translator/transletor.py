import json
import os
import difflib
from difflib import SequenceMatcher 
from difflib import get_close_matches
data = json.load(open("data.json",'r'))

class bcolors:
    PURPLE = '\033[95m'
    PINK = '\033[94m'
    BLUE = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def translate(word) :
    if word in data :
        return data[word]
    else:
        x = 'N'
        y = get_close_matches(word,data.keys(),n=4, cutoff=0.7)
        if y == []:
                return bcolors.RED + word + " does't exist."+ bcolors.ENDC
        else:
            for i in y or x == 'Y':
                x = input(f"Maybe did you mean {i} ?? " +bcolors.GREEN+"Y/N    "+bcolors.ENDC)
                while x.upper() != 'Y' and x.upper() != 'N':
                    x = input("please enter " +bcolors.GREEN+"Y/N    "+bcolors.ENDC)
                if x.upper() =='Y':
                    return translate(i)
                    break   


temp = input("Enter the word: ")
temp = temp.lower()
while(temp != "q"):
    os.system("clear")
    print(f"Your word is: {temp}")
    temp2 = translate(temp)
    if type(temp2) == list and len(temp2) != 1:
        j=1
        for i in temp2:  
          print(f"{j}.{i}")
          j=j+1
    else:
        if type(temp2) == list:
            print(temp2[0])
        else:
            print(temp2)
    print(bcolors.BLUE + "write 'q' to get out" + bcolors.ENDC)
    temp = input("Enter the word: ")


#get_close_matches(word,1)