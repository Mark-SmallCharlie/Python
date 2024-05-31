#caijitwo
import random

counts = 5
answer = random.randint(1,99)

while counts >0:
    temp= input("猜数字:")
    guess = int(temp)

    if guess == answer:
        print("right")
        print("fxxk you")
    else:
        if guess < answer:
            print("small")
        else:
            print("big")
        counts = counts -1
print("You had no times Game over")
