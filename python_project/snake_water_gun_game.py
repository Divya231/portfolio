import random
def game(comp,you):
    if comp == you:
        return None
    elif comp=="s":
        if you=='w':
            return False
        elif you=="g":
            return True
    elif comp=="w":
        if you=="g":
            return False
        elif you=="s":
            return True
    elif comp=="g":
        if you=="s":
            return False
        elif you=='w':
            return True


rand=random.randint(1,3)
print("computer turn : snake{s},water{w},gun{g} ")
if rand==1:
    comp="s"
elif rand==2:
    comp="w"
elif rand==3:
    comp="g"
# print(rand)
you=input("your's turn : snake {s},water{w} & gun{g}-----> ")
a=game(comp,you)
print(f"computer choose : {comp}")
print(f"your turn : {you}")
if a==None:
    print("tie")
elif a:
    print("you win")
else:
    print("you lose")