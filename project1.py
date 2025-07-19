'''
1 for snake
-1 for water
0 for gun
'''
import random
computer = random.choice([-1,0,1])

you_str = (input("Enter your choice:"))
youdict = {
           "s" : 1,
           "w" : -1,
           "g" : 0 
}

reversedict = {
           1 : "snake",
           -1 : "water",
           0 : "gun"
}

you = youdict[you_str]

print("You choose:",reversedict.get(you),"\n",  "Computer choose:",reversedict.get(computer))
# print("Computer choose:",reversedict.get(computer))

'''
if (computer == you):
    print("Draw")

else:
    if(computer == -1 and you ==1 ):#com - you is -2
        print("You win!")

    elif(computer == -1 and you == 0):# com - you is -1
        print("You lose!")
mojfo
    elif(computer == 1 and you == 0):# com - you is 1
        print("You win!")

    elif(computer == 1 and you == -1):# com - you is 2
        print("You lose!")

    elif(computer == 0 and you == 1):# com - you is -1
        print("You lose")

    elif(computer == 0 and you == -1):# com - you is -2
        print("You win")
    
    else:
        print("Something went wrong")
'''
#we are winning at -2 and 1(comp = you)
#we are losing at -1 and 2(comp = you)

if (computer == you):
    print("Draws")

elif((computer - you) == 1 or (computer - you) == -2):
        print("You win!")

else:
     print("You lose!")
     
















