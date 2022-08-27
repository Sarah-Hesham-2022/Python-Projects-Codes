
from typing import Type


word = "Hello World"  # creation
Letter = word[0]  # accessing
print(Letter)
print(len(word)) # length of string
print("."* 10) # prints ten dots
print(word + "!") # concatenation "Hello World!"

print(word[0:len(word)]) # items start through end-1
print(word[0]) #get one char of the word
print(word[0:1]) #get one char of the word (same as above)
print(word[0:3]) #get the first three char
print(word[:3]) #get the first three char
print(word[-3:]) #get the last three char
print(word[3:]) #get all but the three first char
print(word[:-3]) #get all but the three last character
print(word[:]) # a copy of the whole list

print(word.find("H"))
print(word.startswith("H"))
print(word.endswith("d"))
print(word.endswith("w"))
print(word.upper()) # HELLO WORLD
print(word.lower()) # hello world
print('hello world'.capitalize()) # Hello world
print(word.swapcase()) # hELLO wORLD
print(*reversed(word)) # dlrow olleh

print(help(str.capitalize))
print(help(reversed))

stmts = word.split(' ') # Split on whitespace
print(stmts)
print(' '.join(['Morning', 'dear'])) # Morning dear
print('-'.join(stmts)) # "Hello-World"
print(word.replace("Hello", "Goodbye")) # "Goodbye World"

#strip() removes from both ends
#lstrip() removes leading characters (Left-strip)
#rstrip() removes trailing characters (Right-strip)

word = "   hello world      "
print(word.strip()) # "hello world"
print(word.lstrip()) # "hello world "
print(word.rstrip()) # "  hello world"


#Tasks:

#1- Write down a longestCommonPrefix function that returns the longest prefix that is common in two strings.
def longestCommonPrefix(word1,word2):
    l1=len(word1)
    l2=len(word2)
    l=0
    prefix=""
    if(l1>l2):
        l=l2
    else:
        l=l1
    i=0
    while(i<l):
        if(word1[i]==word2[i]):
            prefix=prefix+word1[i]
        i=i+1
    return prefix

print(longestCommonPrefix("Hello Wolrd","Hell is bad"))
print(longestCommonPrefix("Hello Wolrd","Hell "))
print(longestCommonPrefix("Farah","Sarah"))
print(longestCommonPrefix("Why","Hell"))

#2- Write down a match function that returns whether the two given strings are matching or not.
def matching(word1,word2):
    l1=len(word1)
    l2=len(word2)
    if(l2!=l1):
        return False
    i=0
    while(i<l1):
        if(word1[i]!=word2[i]):
            return False
        i=i+1
    return True

print(matching("Sarah","Farah"))
print(matching("Sarah","Sarah"))
print(matching("Hello World","Hello Word  "))


