# EX 5
import random

random_list1 = random.sample(range(100), 10)
random_list2 = random.sample(range(100), 15)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_list = []

print(random_list1,"\n",random_list2, "\n")

for termOf1 in random_list1:
    for termOf2 in random_list2:
        if termOf1 == termOf2:
            if termOf1 in common_list:
                continue
            common_list.append(termOf1)
print(common_list)  

# EX 6
string = input("Enter a string: ")
string_reversed = string[::-1]
if string == string_reversed:
    print("This is a palindrome")
else:
    print("This is NOT a palindrome")

 EX 7
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([even for even in a if even % 2 == 0])

# EX 8
while True:
    player1 = input("First Player: rock, paper or scissors ?")
    player2 = input("Second Player: rock, paper or scissors ?")

    if player1 == player2:
        print("It's a tie!")
    elif player1 == "rock":
            if player2 == "paper":
                print("Player2 won")
            else:
                print("Rock break scissors, Player1 won")
    elif player1 == "paper":
            if player2 == "rock":
                print("Player1 won, paper over rock")
            else:
                print("Player2 won, scissors over paper")
    else:
        if player2 == "paper":
            print("Scissers cut paper, Player1 won")
        else:
            print("Rock break scissors, Player2 won")

    continue_game = input("Would you like to continue to play ?")
    if continue_game == "yes":
        continue
    else:
        print("Game over")
        break

# EX 9
from random import randrange

random_number = randrange(1,10)
guess = int(input("Guess a number between 1 and 9: "))
continue_game = True

while continue_game:
    while guess != random_number:
        if guess > random_number:
            print("Your number is too high")
            guess = int(input("Guess a number between 1 and 9: "))
        else:
            print("Your number is too small, guess higher")
            guess = int(input("Guess a number between 1 and 9: "))
    else:
        print("You've guessed it congrats!")
        cont = input("Would you like to continue playing ?")
        if cont == "yes":
            random_number = randrange(1,10)
            guess = int(input("Guess a number between 1 and 9: "))
            continue_game = True
        else:
            print("Game over")
            continue_game = False
            

# EX 9
import random

number = random.randint(1,9)
guess = 0
count = 0


while guess != number and guess != "exit":
    guess = input("What's your guess?")
    
    if guess == "exit":
        break
    
    guess = int(guess)
    count += 1
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it!")
        print("And it only took you",count,"tries!")

# EX 10
from random import sample

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_nums = [i for i in a if i in b]
print(common_nums)
