# Blank line.

lives = 3
gameover = 0

secret = "hamlet"

print("\nWelcome to this guess a word!\n")
word = input("_ _ _ _ _ _ \nGuess which word is! Only 3 Chances!\n\nWhile writing a 6 letter long word. A little hint appears!\n\nHint: Literature.\n\nWrite your guess here: ")

# Part where i Begin. 

if word != "hamlet":
    lives = lives - 1
else:
    input("CONGRATS!! you have successfully guessed it!")
    print("")()

if lives == gameover:
    input("\nGame over, ran out of chances!")
    print("Try again!") 

# Forseful crash so the player no longer advances more.

# Here is if the player wrote less or more letters than 6.

maxnum = 6

while maxnum != len(word):
    print("\nYour guess has less or more letters than 6.")
    word = input("\nGuess your word again: ")
    if word != "hamlet":
        lives = lives - 1
        if lives == gameover:
            input("\nGame over, ran out of chances!")
            print("")()  

# The whole secondary hint part of the code, in case a user wrotes a 6 letters long word.

if secret[0].lower() == word[0].lower():
    print(f"\n{secret[0].upper()} ", end="")
else:
    print("_ ", end="")

    if secret[1].lower() == word[1].lower():
            print(f"{secret[1].upper()} ", end="")
    else:
        print("_ ", end="")

    if secret[2].lower() == word[2].lower():
        print(f"{secret[2].upper()} ", end="")
    else:
        print("_ ", end="")

    if secret[3].lower() == word[3].lower():
        print(f"{secret[3].upper()} ", end="")
    else:
        print("_ ", end="")

    if secret[4].lower() == word[4].lower():
        print(f"{secret[4].upper()} ", end="")
    else:
        print("_ ", end="")

    if secret[5].lower() == word[5].lower():
        print(f"{secret[5].upper()} ", end="")
    else:
        print("_ ", end="")

# If the word is incorrect, this happens:

while word != "hamlet":
    lives = lives - 1
    print("\nIt wasn't the word.")
    word = input("\nGuess the word again: ")
    
    if word == "hamlet":
        input("CONGRATS!! you have successfully guessed it!") 
        print("")() 
    if lives == gameover:
            input("\nGame over, ran out of chances!")
            print("")() 
            
# If word has less or more letter, this ahappens:

    while maxnum != len(word) and word != "hamlet":
        lives = lives - 1
        print("\nYour guess has less or more letters than 6.")
        word = input("\nGuess the word again: ")
        
        if word == "hamlet":
            input("CONGRATS!! you have successfully guessed it!") 
            print("")()   
        if lives == gameover:
            input("\nGame over, ran out of chances!")
            print("")()   

#If any of this happens, go there:

else:
    input("CONGRATS!! you have successfully guessed it!")
    print("")()