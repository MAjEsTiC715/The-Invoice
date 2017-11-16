#===============================================================================  Documentation  ===========================================================================================================================
#Program Starts and asks the user how many problems they want to solve. 
#If user enters any input other than the valid range of one through 10, program interprets this as an error and re-asks for input.
#Program generates a random multiplication problem with two random factors between zero and 12 (zero and 12 are valid factors).
#Program displays the problem for the user.
#Program asks the user for the answer to the current problem. If the user's answer is not correct then the program gives a hint by telling the user if their answer is too high or too low, and then returns to step 3.
#If the user's answer is correct then the program displays a message telling the user that the answer is correct, and then the program either returns to step 2
#(if the user has not solved the requested number of problems) or the program continues on to step 5.
#The program displays the average number of tries the user took to get the correct answer.
#Be sure to use comments for both structure of the program and documentation of the code.
#All code must completely be your own individual work product.
#===========================================================================================================================================================================================

# Import Random and randint and sys
import random
from random import randint
import sys

#establish 'tries' as a variable = 0 because this will be used as a global variable to track the amount of 'tries' the user makes.
tries = 0

#===============================================================================  main() function  ===========================================================================================================
#define main() as a function (this will be the function that runs all the code)
    #set 'sentinel' and 'tries' to a global variable, this will allow us to communicate values of those set variables through the other functions.
    #establish a try/except loop to catch any exceptions that might cause the program to crash.
        #set 'intStr' to an int(input() to ask what amount of questions the user would like to do.
        #establish an if statement with '(intStr > 0 and intStr < 11)' checking if the value entered in 'intStr' is between 0 and 11.
            #set a 'for' loop called 'execLoop' with a range determined by 'intStr'.
                #within the 'for' loop it sets 'sentinel' to FALSE, this essentially resets the 'sentinel' value that will be changed in calc(), enabling calc() to run again.
                #execute calc() function.
            #create the variable 'triesAvg', this takes the number of 'tries' divided by the amount of questions 'intStr'
            #the 5 print lines print the values calculated from calc() and the amount of question entered in 'intStr' and then prints the average tries 'triesAvg' using the .format() method.
            #execute raplay() function.
        #else statement is correlated with the prev 'if' statement, if proven true it prints ("You must enter an integer 1 through 10") and restarts the main() function.
    #we set two 'execpt' statements catching the 'ValueError', if caught then it prints ("That's not an integer!") and restarts main()
#=============================================================================================================================================================================================

def main():
    global sentinel
    global tries
    try:
        intStr = int(input("Please enter the amount of questions you desire: "))
        if (intStr > 0 and intStr < 11):
            for execLoop in range(intStr):
                sentinel = False
                calc()
            triesAvg = tries / intStr
            print ("=====================================================")
            print ("It took you " + format(tries, '.0f') + " tries.")
            print ("You asked for " + format(intStr, '.0f') + " questions.")
            print ("Your avgerage tries per question is: " + format(triesAvg, '.2f'))
            print ("=====================================================")
            replay()
        else:
            print ("You must enter an integer 1 through 10")
            print ("=====================================================")
            main()
                
    except ValueError:
        print ("That's not an integer!")
        main()
    except UnboundLocalError:
        print ("You entered a Character, you need an Integer!")

#===============================================================================  calc() function  ===========================================================================================================
#define calc() as a function (this is the function that handles calculating what the random integers are as well as counting the amount of tries it takes for the user to get the correct answer)
    #set 'sentinel' and 'tries' to a global variable, this will allow us to communicate values of those set variables through the other functions
    #establish 'num1' 'num2' and 'solve' as variables
    #'num1' and 'num2' create random integer from 0 to 12
    #'solve' multiplies the integers created in 'num1' and 'num2'
    #set a 'while' loop with the variable 'sentinel' == False
        #establish a try/except loop to catch any exceptions that might cause the program to crash
            #print the multiplication problem using the .format() method for 'num1' and 'num2'
            #create the int(input() variable 'answer' and ask the user what the answer is
            #establish an 'if' statement to determine whether 'answer' is greater than 'solve'
                #if true then we add 1 to 'tries'
                #and then print 'too high'
            #establish an 'elif' statement to determine whether 'answer' is less than 'solve'
                #if true then we add 1 to 'tries'
                #and then print 'too low'
            #establish an 'else' statement which tells the user they got the correct answer and changes 'sentinel' to TRUE which exits the 'while' loop
        #we set two 'execpt' statements catching the 'ValueError', if caught then it prints ("That's not an int, you need to try!") and re-prints the question and asks for the answer
    #return 'tries'
#==============================================================================================================================================================================================
        
def calc():
    global sentinel
    global tries
    
    num1 = randint(0,12)
    num2 = randint(0,12)
    solve = num1 * num2

    while sentinel == False:
        try:
            print ("Solve this: " + format(num1, '.0f') + " * " + format(num2, '.0f'))
            answer = int(input("what is the answer: "))
            if answer > solve:
                tries += 1
                print ("too high")
            elif answer < solve:
                tries += 1
                print ("too low")
            else:
                print ("Hurray! You got the correct answer!")
                sentinel = True
        except ValueError:
            print ("That's not an int, you need to try!")
        except:
            print ("Unexpected error:"), sys.exc_info()[0]
            raise

    return tries

#===============================================================================  replay() function  ===========================================================================================================
#define raplay() as a function (this asks the user whether he/she would want to restart the program)
    #set 'tries' to a global variable, this will allow us to communicate values of those set variables through the other functions
    #set 'ask' to an int(input() to ask the user whether he/she would like to play again
    #establish an 'if' statement, if 'ask' == Yes it resets 'tries' to 0 and 'sentinel' to FALSE and runs main() function
    #establish an 'else' statement, if user does not enter Yes then it exits the program with sys.exit and prints ("OK, maybe next time.")
#=========================================================================================================================================================================================

def replay():
    global tries
    ask = input("""Would you like to play again?    Type "Yes" or "No"    : """)
    if ask == "Yes":
        tries = 0
        sentinel = False
        main()
    else:
        print ("OK, maybe next time.")
        sys.exit('end')

#===============================================================================  Input  ===========================================================================================================
#set 'start' to an int(input() to ask the user whether he/she would like to start solving problems
#establish an 'if' statement, if 'start' == Y or == y and runs main() function
#establish an 'else' statement, if user does not enter Y or y then it exits the program with sys.exit and prints ("Alright, thank you")
#==========================================================================================================================================================================================        

start = input("Would you like to solve some problems, enter 'Y' for Yes and 'N' for No: ")
if (start == 'Y' or start == 'y'):
    main()
else:
    print ("Alright, thank you")
    sys.exit("The program has ended")
        
