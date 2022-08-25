"""EX01 - Chardle - A cute step toward Wordle"""

__author__ = "730553817"

x: int = 0

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    quit()

character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    quit()
    
print("Searching for " + character + " in " + word)

if character == word[0]:
    print(character + " found at index 0")
    x = x + 1

if character == word[1]:
    print(character + " found at index 1")
    x = x + 1

if character == word[2]:
    print(character + " found at index 2")
    x = x + 1

if character == word[3]:
    print(character + " found at index 3")
    x = x + 1

if character == word[4]:
    print(character + " found at index 4")
    x = x + 1

if x == 1:
    print(str(x) + " instance of " + character + " found in " + word)
else:
    if x < 1 :
        print("No instances of " + character + " found in " + word)
    else:
        print(str(x) + " instances of " + character + " found in " + word)