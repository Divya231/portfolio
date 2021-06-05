import random
def game(comp,you):
    if comp==you:
        return None
    elif comp=='stone':
        if you=='paper':
            return True
        elif you=='scissor':
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
    print(f"Computer Turn :  stone{s},Paper{p},Scissor{sc}")
    if rand==1:
        comp="s"
    elif rand==2:
        comp="p"
    elif rand==3:
        comp="sc"
     # print(random)
    you=input(f"NOW Your Turn :  stone{s},Paper{p},Scissor{sc}")
    a=game(comp,you)
    print(f"Computer Choose {comp}")
    print(f"You chooses {you}")
    if a==None:
        print("Tie...try for next time!!!!")
    elif a:
        print("HURRAY!!!! You Win....")
    else:
        print("ALAS!!! You Lose....")