import random
print("Welcome to Stone-Paper-Scissor Game\nbefore start the game please understand the rules of the game\nRock wins against scissors, paper wins against rock, and scissors wins against paper. ")
name = input("Enter your name:")
print(f"Hello {name} Let's start the game!!!")
options = ['Rock','Paper','Scissor\n']
com_choice = random.choice(options)
com_score = 0
user_score= 0
number_chances = 1
while(number_chances<=5):
    user_choice = input(f"Which option {name} you go with?\n Rock\tPaper\tScissor")
    if user_choice == 'Rock':
        if com_choice == 'Rock':
            print("It's tie")
        if com_choice=='Paper':
            print("Sorry computer won this time")
            com_score+=1
        if com_choice=='Scissor':
            print(f"Congratulation {name} you got the point")
            user_score+=1
    elif user_choice == 'Paper':
        if com_choice == 'Rock':
            print(f"Congratulation {name} you got the point")
            user_score+=1
        if com_choice=='Paper':
            print("It's tie")
        if com_choice=='Scissor':
            print("Sorry computer won this time")
            com_score+=1
    elif user_choice == 'scissor':
        if com_choice == 'Rock':
            print("Sorry computer won this time")
            com_score+=1
        if com_choice=='Paper':
            print(f"Congratulation {name} you got the point")
            user_score+=1
        if com_choice=='Scissor':
            print('Its tie')
    print(number_chances,f"Total no.of chances took by {name}")
    print(5-number_chances,"number_chances")
    number_chances=number_chances+1
    if user_score>com_score:
        print(f"Congratulation {name} you won the game")
    elif user_score<com_score:
        print("Computer won the game")
    else:
        print("Sorry It's tie")
    print(f"Final score:{user_score},{com_score}")
if number_chances>5:
    print("Game over")


