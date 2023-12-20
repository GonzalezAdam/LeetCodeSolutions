#I wanted to make a script that would take in the leetcode problem names and then output them with underscores between the words instead of spaces.
#ie: "1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence" -> "1455._Check_If_a_Word_Occurs_As_a_Prefix_of_Any_Word_in_a_Sentence.py"

import pyperclip #allows us to copy an output to clipboard automatically
def renamer(leetcodestring): #changes the text from space separation to _ separation
    newstring = ""
    holdlist = leetcodestring.split()
    for word in holdlist:
        newstring = newstring + str(word) + "_"
    return newstring[:-1]


value = input("Enter String:") #grabs input

pyperclip.copy(renamer(value)+".py") #copies output to clipboard as .py
