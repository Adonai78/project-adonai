import random 
playing = True 
secret_number=random.randint(1,25)
guess_number=int(input("Guess a number"))
if(secret_number== guess_number):
    print("correct")
else:
    print("wrong") 
    playagain = input("do you wanna play again") 
    if(playagain=="no"):
        playing= False
    else:
        playing=False             