'''
1 = snake
0 = water
-1 = gun

'''

import random

computer = random.choice([-1,0,1]) # Using this method, the computer chooses a random number
you_number=input("You can choose any one from s, w, g: ")
you_dict={"s":1,"w":0,"g":-1}  #This line will give you 1, -1, 0 instead of s w g
reverse_dict={1:"snake",0:"water",-1:"gun"}

you= you_dict[you_number] #this line add you output

print(f"you chose {reverse_dict[you]}\nComputer chose {reverse_dict[computer]}") # This line prints your choice and the computer's selected output.


if (computer == you):
    print("it a draw")

else:
    if (computer == -1 and you == 1):
        print("you lose!")    
    elif (computer == -1 and you == 0):
        print("you win!")    
    elif (computer == 1 and you == 0):
        print("you lose!")    
    elif (computer == 1 and you == -1):
        print("you win!")    
    elif (computer == 0 and you == 1):
        print("you win!")    
    elif (computer == 0 and you == -1):
        print("you lose!")    
    else:
        print("something went wrong!")































