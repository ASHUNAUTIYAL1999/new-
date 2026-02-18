import random

def number_generator():
    num=random.randint(1,100)
    return num

def guess():
    try : gues=int(input("the number you are guessing"))
    except ValueError:
        print("please enter a valid number")
        return guess()
    return gues

def compare(numss,gue):
    if numss==gue:
        print("Correct")
    elif numss>gue:
        print("go larger")
    else:
        print("go smaller")


def main():
    chance=0
    numss=number_generator()
    while chance<6:
        gue=guess()
        compare(numss,gue)
        chance+=1
    print("chance ended")
    print(numss)

main()