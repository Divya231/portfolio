import random
rand_num=random.randint(1,5)
# print(rand_num)
userGuess=None
guess=0
while userGuess!=rand_num:
    userGuess=int(input("enter a guess"))
    guess+=1
    if userGuess==rand_num:
        print("You Guess Right....")
    else:
        if userGuess>rand_num:
            print("Guessed Wrong!!!!.....enter a smaller number")
        else:
            print("Guessed Wrong !!!!...enter a larger number")
print(f"you guessed the number in {guess} guesses")
 
with open("sample.txt","r") as f:
    sample =int(f.read())
if guess<sample:
    print("you break the record...")
    with open("sample.txt","w") as f:
        f.write(guess)