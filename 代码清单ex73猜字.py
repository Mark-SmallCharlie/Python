import random
counts =6
secret = random.randint(1,99)
guess = 0
tries = 1
print("I have an 1~99 number ,you can guess 6 times ,guess right then you win!")
while tries <=6:
    guess = int(input("No"+str(tries)+"times)you get it?"))
    if guess<secret:
        print("shamll")
    elif guess >secret:
        print("big")
    else:
        print("right")
        break
    counts = counts -1
if guess!=secret:
    print("no change!")
    print("the number is ",secret)
