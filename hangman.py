def guess_letter():
    find=input("Enter a guessing letter :")
    print(len(find))
    if(len(find)!=1 or find.isdigit()):
        print("Invalid input")
        guess_letter()
    return(find.upper())
import random
f = open("hw.txt")
ip = f.read()
words=ip.split()
word=random.choice(words)
word1=word
print("WElCOME TO HANGMAN GAME BY RAYUGA\n")
name=input("Enter your Name : ")
print("Hello",name+"! Best of luck!\n\nLets play Hangman",word)
n=len(word)
word=word.upper()
guess='-'*n
count=0
li=list()
print(guess)
while(True):
    find=guess_letter()
    if find in word:
        index = word.find(find)
        word = word[:index] + "_" + word[index + 1:]
        guess = guess[:index] + find + guess[index + 1:] 
        print(guess)
        if word == '_' * n:
            print("Congrats! You have guessed the word correctly!")
            break;
    else:
         count += 1
         li.append(find)
         if count == 1:
             print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
           
             print("Wrong guess. ")
             for i in li:
                print (i)
         elif count == 2:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("Wrong guess. ")
                for i in li:
                    print (i)
         elif count == 3:
             print("   _____ \n"
                   "  |     | \n"
                   "  |     |\n"
                   "  |     | \n"
                   "  |      \n"
                   "  |      \n"
                   "  |      \n"
                   "__|__\n")
             print("Wrong guess. ")
             for i in li:
                 print (i)
         elif count == 4:
             print("   _____ \n"
                   "  |     | \n"
                   "  |     |\n"
                   "  |     | \n"
                   "  |     O \n"
                   "  |      \n"
                   "  |      \n"
                   "__|__\n")
             print("Wrong guess. ")
             for i in li:
                 print (i)
         elif count == 5:
             
             print("   _____ \n"
                   "  |     | \n"
                   "  |     |\n"
                   "  |     | \n"
                   "  |     O \n"
                   "  |    /|\ \n"
                   "  |    / \ \n"
                   "__|__\n")
             print("Wrong guess. You are hanged!!!")
             print("The word was:",word1)
             break;
             
            

    

