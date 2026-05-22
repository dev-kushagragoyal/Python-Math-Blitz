import time as t
import random as r

print("Welcome to the Math game")
print()

while True:

        t.sleep(2)
        print('''Select your choice : 
                1.Square game 
                2.Cube game
                3.Exit''')
        print()

        choice_game = int(input("Enter your choice : "))
        print()

        if choice_game == 1:

                print("In square game you have to find the square of the number and tell your answer")
                print()

                print("Please choose the level of the game")
                print()

                print('''
                    1 == Easy level i.e.numbers from 1 to 10
                    2 == Medium level i.e.numbers from 11 to 20
                    3 == Difficult level i.e.numbers from 21 to 35
                    4 == Extreme Difficult level i.e.numbers from 36 to 50
                    ''')
                print()

                choice_level = int(input("Enter your choice : "))
                print()


                if choice_level == 1:

                    print("You have chosen easy level")
                    print()
                    t.sleep(1)

                    choice_time = int(input("Enter the number of times you want to play : "))
                    print()
                    print()
                    print()
                    print("Let's Begin")
                    print()
                    print()
                    print()
                    t.sleep(2)

                    score = 0

                    for i in range(choice_time):

                        num_1 = r.randint(1,10)

                        print("Your number is : ",num_1)
                        print()

                        print("Calculate the square of the number and tell the answer : ")
                        print()
                        t.sleep(1)

                        answer_user = int(input("Enter your answer : "))
                        print()

                        answer_computer = num_1 * num_1

                        if answer_user == answer_computer : 

                            print("Your answer is correct that is : ",answer_computer)
                            print()
                            print()
                            print()
                            score = score + 1
                            t.sleep(1)

                        else:

                            print("Oops! Your answer is not correct")
                            print()
                            t.sleep(1)
                            print("Your answer is : ",answer_user,",But the correct answer is : ",answer_computer)
                            print()
                          

                    t.sleep(2)
                    print("Here is the result")
                    print()
                    t.sleep(1)
                    print("You have answered : ",score,"correct out of",choice_time)
                    print()



                elif choice_level == 2:

                    print("You have chosen medium level")
                    print()
                    t.sleep(1)

                    choice_time = int(input("Enter the number of times you want to play : "))
                    print()
                    print()
                    print()
                    print("Let's Begin")
                    print()
                    print()
                    print()
                    t.sleep(2)

                    score = 0

                    for i in range(choice_time):

                        num_1 = r.randint(11,20)

                        print("Your number is : ",num_1)
                        print()

                        print("Calculate the square of the number and tell the answer : ")
                        print()
                        t.sleep(1)

                        answer_user = int(input("Enter your answer : "))
                        print()

                        answer_computer = num_1 * num_1

                        if answer_user == answer_computer : 

                            print("Your answer is correct that is : ",answer_computer)
                            print()
                            print()
                            print()
                            score = score + 1
                            t.sleep(1)

                        else:

                            print("Oops! Your answer is not correct")
                            print()
                            t.sleep(1)
                            print("Your answer is : ",answer_user,",But the correct answer is : ",answer_computer)
                            print()
                            

                    t.sleep(2)
                    print("Here is the result")
                    print()
                    t.sleep(1)
                    print("You have answered : ",score,"correct out of",choice_time)
                    print()



                elif choice_level == 3:

                    print("You have chosen difficult level")
                    print()
                    t.sleep(1)

                    choice_time = int(input("Enter the number of times you want to play : "))
                    print()
                    print()
                    print()
                    print("Let's Begin")
                    print()
                    print()
                    print()
                    t.sleep(2)

                    score = 0

                    for i in range(choice_time):

                        num_1 = r.randint(21,35)

                        print("Your number is : ",num_1)
                        print()

                        print("Calculate the square of the number and tell the answer : ")
                        print()
                        t.sleep(1)

                        answer_user = int(input("Enter your answer : "))
                        print()

                        answer_computer = num_1 * num_1

                        if answer_user == answer_computer : 

                            print("Your answer is correct that is : ",answer_computer)
                            print()
                            print()
                            print()
                            score = score + 1
                            t.sleep(1)

                        else:

                            print("Oops! Your answer is not correct")
                            print()
                            t.sleep(1)
                            print("Your answer is : ",answer_user,",But the correct answer is : ",answer_computer)
                            print()
                           

                    t.sleep(2)
                    print("Here is the result")
                    print()
                    t.sleep(1)
                    print("You have answered : ",score,"correct out of",choice_time)
                    print()



                elif choice_level == 4:

                    print("You have chosen extreme difficult level")
                    print()
                    t.sleep(1)

                    choice_time = int(input("Enter the number of times you want to play : "))
                    print()
                    print()
                    print()
                    print("Let's Begin")
                    print()
                    print()
                    print()
                    t.sleep(2)

                    score = 0

                    for i in range(choice_time):

                        num_1 = r.randint(36,50)

                        print("Your number is : ",num_1)
                        print()

                        print("Calculate the square of the number and tell the answer : ")
                        print()
                        t.sleep(1)

                        answer_user = int(input("Enter your answer : "))
                        print()

                        answer_computer = num_1 * num_1

                        if answer_user == answer_computer : 

                            print("Your answer is correct that is : ",answer_computer)
                            print()
                            print()
                            print()
                            score = score + 1
                            t.sleep(1)

                        else:

                            print("Oops! Your answer is not correct")
                            print()
                            t.sleep(1)
                            print("Your answer is : ",answer_user,",But the correct answer is : ",answer_computer)
                            print()
                            

                    t.sleep(2)
                    print("Here is the result")
                    print()
                    t.sleep(1)
                    print("You have answered : ",score,"correct out of",choice_time)
                    print()

                else:
                     print("Please choose the correct option")
                     print()

        elif choice_game == 2:

                print("In cube game you have to find the cube of the number and tell your answer")
                print()

                print("Please choose the level of the game")
                print()

                print('''
                    1 == Easy level i.e.numbers from 1 to 10
                    2 == Medium level i.e.numbers from 11 to 20
                    3 == Difficult level i.e.numbers from 21 to 35
                    4 == Extreme Difficult level i.e.numbers from 36 to 50
                    ''')
                print()

                choice_level = int(input("Enter your choice : "))
                print()


                if choice_level == 1:

                    print("You have chosen easy level")
                    print()
                    t.sleep(1)

                    choice_time = int(input("Enter the number of times you want to play : "))
                    print()
                    print()
                    print()
                    print("Let's Begin")
                    print()
                    print()
                    print()
                    t.sleep(2)

                    score = 0

                    for i in range(choice_time):

                        num_1 = r.randint(1,10)

                        print("Your number is : ",num_1)
                        print()

                        print("Calculate the cube of the number and tell the answer : ")
                        print()
                        t.sleep(1)

                        answer_user = int(input("Enter your answer : "))
                        print()  

                        answer_computer = num_1 * num_1 * num_1

                        if answer_user == answer_computer : 

                            print("Your answer is correct that is : ",answer_computer)
                            print()
                            print()
                            print()
                            score = score + 1
                            t.sleep(1)

                        else:

                            print("Oops! Your answer is not correct")
                            print()
                            t.sleep(1)
                            print("Your answer is : ",answer_user,",But the correct answer is : ",answer_computer)
                            print()
                           

                    t.sleep(2)
                    print("Here is the result")
                    print()
                    t.sleep(1)
                    print("You have answered : ",score,"correct out of",choice_time)
                    print()

                elif choice_level  == 2:

                        print("You have chosen medium level")
                        print()

                        choice_time = int(input("Enter the number of times you want to play : "))
                        print()
                        print()
                        print()
                        print("Let's Begin")
                        print()
                        print()
                        print()
                        t.sleep(2)

                        score = 0

                        for i in range(choice_time):

                                num_1 = r.randint(11,20)

                                print("Your number is : ",num_1)
                                print()

                                print("Calculate the cube of the number and tell the answer : ")
                                print()
                                t.sleep(1)

                                answer_user = int(input("Enter your answer : "))
                                print()  

                                answer_computer = num_1 * num_1 * num_1

                                if answer_user == answer_computer : 

                                    print("Your answer is correct that is : ",answer_computer)
                                    print()
                                    print()
                                    print()
                                    score = score + 1
                                    t.sleep(1)

                                else:

                                    print("Oops! Your answer is not correct")
                                    print()
                                    t.sleep(1)
                                    print("Your answer is : ",answer_user,",But the correct answer is : ",answer_computer)
                                    print()
                                    

                        t.sleep(2)
                        print("Here is the result")
                        print()
                        t.sleep(1)
                        print("You have answered : ",score,"correct out of",choice_time)
                        print()

                elif choice_level  == 3:

                        print("You have chosen difficult level")
                        print()

                        choice_time = int(input("Enter the number of times you want to play : "))
                        print()
                        print()
                        print()
                        print("Let's Begin")
                        print()
                        print()
                        print()
                        t.sleep(2)

                        score = 0

                        for i in range(choice_time):

                                num_1 = r.randint(21,35)

                                print("Your number is : ",num_1)
                                print()

                                print("Calculate the cube of the number and tell the answer : ")
                                print()
                                t.sleep(1)

                                answer_user = int(input("Enter your answer : "))
                                print()  

                                answer_computer = num_1 * num_1 * num_1

                                if answer_user == answer_computer : 

                                    print("Your answer is correct that is : ",answer_computer)
                                    print()
                                    print()
                                    print()
                                    score = score + 1
                                    t.sleep(1)

                                else:

                                    print("Oops! Your answer is not correct")
                                    print()
                                    t.sleep(1)
                                    print("Your answer is : ",answer_user,",But the correct answer is : ",answer_computer)
                                    print()
                                    

                        t.sleep(2)
                        print("Here is the result")
                        print()
                        t.sleep(1)
                        print("You have answered : ",score,"correct out of",choice_time)
                        print()

                elif choice_level  == 4:

                        print("You have chosen extreme difficult level")
                        print()

                        choice_time = int(input("Enter the number of times you want to play : "))
                        print()
                        print()
                        print()
                        print("Let's Begin")
                        print()
                        print()
                        print()
                        t.sleep(2)

                        score = 0

                        for i in range(choice_time):

                                num_1 = r.randint(36,50)

                                print("Your number is : ",num_1)
                                print()

                                print("Calculate the cube of the number and tell the answer : ")
                                print()
                                t.sleep(1)

                                answer_user = int(input("Enter your answer : "))
                                print()  

                                answer_computer = num_1 * num_1 * num_1

                                if answer_user == answer_computer : 

                                    print("Your answer is correct that is : ",answer_computer)
                                    print()
                                    print()
                                    print()
                                    score = score + 1
                                    t.sleep(1)

                                else:

                                    print("Oops! Your answer is not correct")
                                    print()
                                    t.sleep(1)
                                    print("Your answer is : ",answer_user,",But the correct answer is : ",answer_computer)
                                    print()

                        t.sleep(2)
                        print("Here is the result")
                        print()
                        t.sleep(1)
                        print("You have answered : ",score,"correct out of",choice_time)
                        print()

                else:
                     print("Please choose the correct option")
                     print()

        elif choice_game == 3:

                print("Thank you for playing")
                print()
                break


        else:
            print("Please choose the correct option")
            print()
