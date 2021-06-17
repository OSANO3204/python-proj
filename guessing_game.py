import random
def guessgame():

    rand= random.randint(0,9)
    num= int(input("Enter a digit between 0 and 9 :"))
    while num !='':
        if num>rand:
            print("you guessed  too high , keep trying !!")
            num = int(input("Enter a digit between 0 and 9 :"))
        elif num<rand:
            print("You guessed too low , Keep trying ")
            num = int(input("Enter a digit between 0 and 9 :"))
        elif  num== rand:
            print("You guessed  right !!, you won the  game, congrats!!")
            exit()

print(guessgame())