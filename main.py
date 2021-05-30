import random
def gameWin(comp,you):
    if comp==you:
        return False
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
def game():
    pass
print("Computer TURN turn:Snake(S) Water(W) Gun(G)")
randNo=random.randint(1,2)
print(randNo)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp=='g'
you=input("Player 2 turn:Snake(1) Water(2) Gun(3)")
a=gameWin(comp,you)
if a==None:
    print("the game is tie")
elif a:
    print("You win:")
else:
    print("You loose:")