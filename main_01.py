import time as t
import random as r


def start_choice():

        print('''
        Select your choice : 
                1.Square game 
                2.Cube game
                3.Exit''')
        print()

        global choice_game
        choice_game = int(input("Enter your choice : "))
        print()

def levels_of_game():

                print("Please choose the level of the game")
                print()

                print('''
                    1 == Easy level i.e.numbers from 1 to 10
                    2 == Medium level i.e.numbers from 11 to 20
                    3 == Difficult level i.e.numbers from 21 to 35
                    4 == Extreme Difficult level i.e.numbers from 36 to 50
                    ''')
                print() 

                global choice_level
                choice_level = int(input("Enter your choice : "))
                print()

def times_of_play():

        global choice_time
        choice_time = int(input("Enter the number of times you want to play : "))

        print()
        print()
        print()
        print("Let's Begin")
        print()
        print()
        print()

def easy_level():
        global num_1
        num_1 = r.randint(1,10)

def medium_level():
    global num_1
    num_1 = r.randint(11,20)

def difficult_level():
    global num_1
    num_1 = r.randint(21,35)

def extreme_difficult_level():
    global num_1
    num_1 = r.randint(36,50)


while True:

        start_choice()

        if choice_game == 1:
                
                print("In square game you have to find the square of the number and tell your answer")
                print()

                levels_of_game()

        elif choice_game == 2:
                
                print("In cube game you have to find the cube of the number and tell your answer")
                print()

                levels_of_game()

        elif choice_game == 3:
        
                        print("Thank you for playing")
                        print()
                        break

        else:
            print("Please choose the correct option")
            print()