#Author: Levi George
#Program: Word swap
#Create a function to replace words in a given text file and print them

#INPUT:     accept a string for auditing
#PROCESS:   Swap each word that we are looking for, with a word we provide
#OUTPUT:    text file that has replaced words
def replace_words(line, keyWord, SwapWord):
    #print("Work Line:", line, "key word:", keyWord, "swap word:", SwapWord, sep="\n")
    str = line
    return str.replace(keyWord, SwapWord)


#Start "main" 


foo = open('WordReplacer\Sample.txt', "r")

keyWord = input(f"Enter a keyword to search for..... [")
SwapWord = input(f"Enter the word to insert in place of your key..... [")

for x in foo:
    modLine = replace_words(x, keyWord, SwapWord)
    print(modLine)

print("\n [Line modification complete] \n")

foo.close()

