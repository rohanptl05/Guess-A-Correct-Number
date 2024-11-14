import random

n=random.randint(1,100)
a =-1
guesses=0
while (a !=n):
    a = int(input("Guess a number between 1 and 100 : "))
    guesses += 1
    if(a>n):
        print("Lower Number please ..")
    else:
        print("Higher Number please ..")    

print(f"You have correct Number is {n} currectly {guesses} attemps")
