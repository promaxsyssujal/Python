import random
jackpot=random.randint(1,100)
guess=int(input("Guess the jackpot>>"))
count=1

while guess !=jackpot:
    if guess<jackpot:
        print("guess bigger")
    else:
        print("guess lower")
    
    guess=int(input("Guess the jackpot again>>"))      
    count+=1 

print("Correct Answer",guess)
print("NO. of attempt",count)