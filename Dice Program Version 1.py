#Documentation
#################################################################################
#User interaction with the program should look like this:
#Program generates two random dice values between 1 and 6 (one value for each dice).  See below for instructions on how to generate a random number. 
#Program displays the values of both dice. 
#Program displays the values of multiplication, division, addition, subtraction, and average of the dice in a nicely formatted display. 
#Be sure to use comments for both structure of the program and documentation of the code.
#################################################################################

#here we search through the 'random' library and pull 'randint' from there to use in our code to generate random numbers
#we also import sys which allows us to end the program properly 

from random import randint
import sys

#Input
#here we ask the user if he/she would like to play our game
#entering y or Y will result in the 'while' loop being executed
#entering any other character will result in the else statement saying 'thanks for playing' and then ending the program
#two numbers are generated using 'randint' with a variable being assigned as 'diceValue1' and 'diceValue2'
####################################################################################################################################

print ('\tWelcome to the dice game')
print ('*****************************************************')
print ('')

userIn = input('Would you like to roll dice, enter y for yes: ')
print ('')
print ('######################################################')
print ('')

while userIn == 'y' or userIn == 'Y':
    diceValue1 = randint(1, 6)
    diceValue2 = randint(1, 6)

#Calculations
#here is where we take 'diceValue1' and 'diceValue and add, subract, multiply, divide, and take the average of
#I used / when dividing in case the number ends up being a float
####################################################################################################################################

    diceAdd = diceValue1 + diceValue2
    diceSub = diceValue1 - diceValue2
    diceMulti = diceValue1 * diceValue2
    diceDiv = diceValue1 / diceValue2
    diceAvg = (diceAdd) / 2

#Output
#here is where all the information is printed beginning with 'diceValue1' and 'diceValue2'
#I put an 'if' statement in here for the reason of 'diceValue2' being greater than 'diceValue1'
    #if this statement is activated then it creates a new variable called 'diceSub2' which is 'diceValue2' - 'diceValue1'
#I used the .format() method to print out the numbers that were calculated
    #using '.0f' this prints the number with no decimal places
    #using '.2f' this prints the number with 2 decimal places
#this continues til the sentinel, 'userIn' is reached asking the user if he/she would like to play again
#entering y or Y will result in the 'while' loop being executed again
#entering any other character will result in the else statement saying 'thanks for playing' and then ending the program
####################################################################################################################################

    print ('the first dice is: ' + format(diceValue1, '.0f'))
    print ('the second dice is: ' + format(diceValue2, '.0f'))

    if diceSub < 0:
        diceSub2 = diceValue2 - diceValue1
        print ('')
        print ('dice1 + dice2 is: ' + format(diceAdd, '.0f'))
        print ('dice2 - dice1 is: ' + format(diceSub2, '.0f'))
        print ('dice1 * dice2 is : ' + format(diceMulti, '.0f'))
        print ('dice1 / dice2 is : ' + format(diceDiv, '.2f'))
        print ('(dice1 + dice2) / 2 is : ' + format(diceAvg, '.2f'))

        userIn = input('Would you like to play again? ')
        print ('***************************************************')
        
    else:
        print ('')
        print ('dice1 + dice2 is: ' + format(diceAdd, '.0f'))
        print ('dice1 - dice2 is: ' + format(diceSub, '.0f'))
        print ('dice1 * dice2 is : ' + format(diceMulti, '.0f'))
        print ('dice1 / dice2 is : ' + format(diceDiv, '.2f'))
        print ('(dice1 + dice2) / 2 is : ' + format(diceAvg, '.2f'))

        userIn = input('Would you like to play again? ')
        print ('***************************************************')

#this 'else' statement is only executed if the user did not enter a 'y' or 'Y'
#it exits the system by using the 'sys' import function with a print statement saying thanks for playing
####################################################################################################################################

else:
    print ('')
    print ('')
    print ('Thanks for playing')
    sys.exit('Thanks for playing')

####################################################################################################################################
#End


