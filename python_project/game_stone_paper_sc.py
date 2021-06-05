import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=="stone":
        if you=="paper":
            return True
        elif you=="scissor":
            return False
    elif comp=="paper":
        if you=="scissor":
            return True
        elif you=="stone":
            return False
    elif comp=="scissor":
        if you=="stone":
            return True
        elif you=="paper":
            return False
rand=random.randint(1,3)
print("Computer Turn : Stone{stone},Paper{paper},Scissor{scissor}")
if rand==1:
    comp="stone"
elif rand==2:
    comp="paper"
elif rand==3:
    comp="scissor"
you=input("Now Your Turn :  stone{stone},paper{paper},scissor{scissor}")
a=gamewin(comp,you)
print(f"Computer Chooses {comp} ")
print(f"you chooses {you}")
if a==None:
    print("tie")
elif a:
    print("you win")
else :
    print("lose")