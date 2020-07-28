import random

print("hello")
print("Write your name")
name=input()
print("Well " + name + " i am thinking a number between 1 to 20 ")

ran_no=random.randint(1,20)

for i in range(1,6):

    guess = int(input())
    print("you have choosen " + str(guess))
    if ran_no>guess:
        print("you have choosen no. too low")

    elif ran_no<guess:
        print("you have choosen no. too high")

    else:
        break

if ran_no==guess:
    print("congrats you did guess your number correctly.")


