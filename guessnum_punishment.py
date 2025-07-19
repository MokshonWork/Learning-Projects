from random import randint # to generate a randon number
import time

n = randint(1,100) #random no. bw 1 and 100
guesses = 1
a = -1

print("\n--- GUESS THE NUMBER GAME---")
def countdown(end , start = 0):
    print(f"Starting the game in {end} seconds")
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Enjoy your game.....")

countdown(10)

try: 
    while( a != n ):
         
         a = int(input("GUESS THE NUMBER:"))

         if( a > n ):
            print("LOWER NUMBER PLEASE...")
            guesses +=1

         elif(a < n):
            print("GREATER NUMBER PLEASE...")
            guesses +=1

    print(f"You Guessed the correct number that is {n} in {guesses} Attempt")

except ValueError:
    print("Invalid input. Please enter valid numbers.")

except Exception as e:
    print(f"An error occurred: {e}")

else:
    print("\n ..... THANKS FOR PLAYING THE GAME...")


    




