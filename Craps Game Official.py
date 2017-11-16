#################        DOCUMENTATION         ###############################################################################################################
#Rules of the game (and the program):
#Player and “house” start with a score of 0 before the first roll.  Scores for both are accumulated through the number of rolls (1,2, and 3). 
#For each roll of the 2 dice: NOTE – this does not require a loop as we have not covered this, but you may use loops if you have moved ahead and mastered them.
    #If the sum of the dice is 7 or 11, display “CRAPS” and increment “house score by 2”.
    #If the dice are the same value (doubles) and the values are even, increment the player score by 2 (NOTE – you should use the modulo operator with an operand of 2 for determining whether the value is even). 
    #If the dice are the same value (doubles) and the values are odd, increment the “house” score by 2.  
    #If not CRAPS or doubles, and the total is less than 7, houseScore = houseScore +2.
    #If not CRAPS or doubles, and the total is greater than 7, playerScore = playerScore + 2.
#Determine the winner and display the results (with 3 rolls, there cannot be a tie!).
#Be sure to use comments for both structure of the program and documentation of the code.
#All code must completely be your own individual work product.
###############################################################################################################################################################

#import
#here we import 'sys' and the 'randint' from 'random'
#this allows use to create random values for the dice as well as closing out the program
#######################################################################################################################################################

from random import randint
import sys

#input
#we begin by setting the 'player' and 'house' variable to 0
#we will use this as the base number when adding the points from the craps game as well as being the total value once the process is done, this will allow us to determine the winner
#########################################################################################################################################################

player = 0
house = 0

#Game Function
#we define game as a function and its only task to run the game
#a 'for' loop is used because we are rolling the dice 3 times before determining the winner
#within the 'for' loop we initiate the 'rollDie()' function which will calculate and store the score for both the player and house
#once that is calculated, two print statements with .format() methods are used to print and convert the values to a string
#we then initiate the 'scoring()' function which will determine the winner by taking the scores and using 'if' statements to determine the winner
#it then asks the user if he/she would want to play again, we then reset the values by saying 'player = 0' and 'house = 0' before perfoming the 'game()' function again
#this prevents the values being added on to each other from the previous game
#########################################################################################################################################################

def game():
    for roll in range(3):
        rollDie()
    print ('player got: ' + format(player, '.0f'))
    print ('house got: ' + format(house, '.0f'))
    scoring()

#Scoring Function (Output)
#we then initiate the 'scoring()' function which will determine the winner by taking the scores and using 'if' statements to determine the winner
#we say 'global player' and 'global house' to allow us to recall and store new values into those variables
#it then asks the user if he/she would want to play again, we then reset the values by saying 'player = 0' and 'house = 0' before perfoming the 'game()' function again
#this prevents the values being added on to each other from the previous game
#########################################################################################################################################################

def scoring():
    global player
    global house
    if player > house:
        print ('Player wins')
        ask = input("""Would you like to play again?    Type "Yes" or "No"    : """)
        if ask == "Yes":
            player = 0
            house = 0
            game()
        else:
            print ("OK, maybe next time.")
            sys.exit('end')
    elif player == house:
        print ('you cannot have a tie, the game is restarting')
        player = 0
        house = 0
        game()
    else:
        print ('house wins')
        ask = input("""Would you like to play a game of Craps?    Type "Yes" or "No"    : """)
        if ask == "Yes":
            player = 0
            house = 0
            game()
        else:
            print ("OK, maybe next time.")
            sys.exit('end')

#rollDie (Calculation)
#we say 'global player' and 'global house' to allow us to store new values into those variables
#this will allow us to add the dice values to the variable 'player' and 'house' and will allow us to recall it later in the program
#we use boolean variables to establish a 'true' and 'false' value when determining if the total of dice added is doubles or craps
#we use 'randint(1,6)' to randomly generate a number from 1 to 6. this is possible because we imported 'randint' from 'random'
#we used the variable 'dice' to be the total added from the randomly generated 'dice1' and 'dice2'
#if dice == 7 or dice == 11: is true then we print 'craps', set 'craps' to 'True' and then 'house += 2' adds 2 points to the 'house' variable
#elif (dice1 == dice2) and ((dice1 % 2) == 0): determines if 'dice' is a double and an even. we use the modulo operator with an operand of 2 for determining whether the value is even or odd
        #we then set True to 'double' and add 2 points to 'player'
#elif (dice1 == dice2) and ((dice1 % 2) == 1): determines if 'dice' is a double and an odd. we use the modulo operator with an operand of 2 for determining whether the value is even or odd 
        #we then set True to 'double' and add 2 points to 'house'
#elif (dice < 7) and (craps != True or double != True):
        #this is only true if 'craps' or 'double' = False and add value,'dice' is less than 7
        #if true then we add 2 points to 'house'
#elif (dice > 7) and (craps != True or double != True):
        #this is only true if 'craps' or 'double' = False and add value,'dice' is greater than 7
        #if true then we add 2 points to 'player'
#we use return 'player' and return 'house' to store the values into those two variables
###########################################################################################################################################################
def rollDie():
    global player
    global house
    craps = False
    double = False
    
    dice1 = randint(1,6)  
    print (format(dice1, '.0f'))
    dice2 = randint(1,6)
    print (format(dice2, '.0f'))
    dice = dice1 + dice2
    print ("You Rolled a total of " + format(dice, '.0f'))

    if dice == 7 or dice == 11:
        print ("Craps")
        craps = True
        house += 2

    elif (dice1 == dice2) and ((dice1 % 2) == 0):
        double = True
        player += 2
    
    elif (dice1 == dice2) and ((dice1 % 2) == 1):
        double = True
        house += 2

    elif (dice < 7) and (craps != True or double != True):
        house += 2

    elif (dice > 7) and (craps != True or double != True):
        player += 2
        
    return player
    return house

#User Input(Start of Program)
#we use an input statement to ask the user if he/she would like to play,
#entering 'Yes' starts the function 'game()', entering 'No' prints ("OK, maybe next time.")
###########################################################################################################################################################
ask = input("""Would you like to play a game of Craps?    Type "Yes" or "No"    : """)
if ask == "No":
    print ("OK, maybe next time.")
elif ask == "Yes":
    game()
    

