import random

randomNumber = random.randint(1,9)
chance = 0


while chance<5 :

    guess = int(input("Choose a number between 1 to 9: "))

    if(guess==randomNumber) :
        print("Congratulations YOU HAVE WON!!")
        break
    
    elif(guess>randomNumber) :
        print("The number is less than the number that you have guessed!")
    
    elif(guess<randomNumber) :
        print("The number is more that the number that you have guessed!")
    
    chance=chance+1

if not chance<5 :
    print('YOU LOSE!! The number is : ',randomNumber)
#print(guess)