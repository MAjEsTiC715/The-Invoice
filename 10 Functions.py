#=================================================================  Documentation  =========================================================================

#A function that displays your name and your major at UAT. The output should look like this:
    #Name: Drale Glacen
    #Major: Advancing Computer Science
#A function that prompts the user to enter their age and returns the user's input as an int.
#A function that takes one argument - the argument will be a name that is a string. The function will display a message like this:
    #Hello Drale Glacen!
#A function that takes an integer argument called number and returns the inverse of that number.
    #For example, if you pass it 3, it will return -3, and if you pass it -3 it will return 3 
#A function that takes an integer argument called count and a string argument called message.
    #The function will display the message <count> times. For example, if the message is "Hello!"
    #and the count is 3, then the functions will display "Hello!" three times.
#A function called getBiggest that takes two int arguments called num1 and num2. The function will return the largest of the two argument values.
    #If the arguments are equal, then it will return the first argument value.
#A function that takes a string argument and counts and returns the number of capital letters in the argument string.
    #For example, if the argument value is "My name is Albert Einstein.", then the return value will be 3.
#A function that takes three int arguments and returns the middle value. for example, if the argument values are 5, 3, and 4, then the function will return 4. 
    #If there is no middle value then the function will return the most common value.
    #For example, if the argument values are 5, 3, and 5, then the function will return 5.
#A function that takes two string arguments and returns a string with only the characters that are in both of the argument strings.
    #There should be no duplicate characters in the return value.
    #For example, if the two argument values are "spaghetti" and "shipping" then the function should return "spghi"
    #(or any five character string with these five characters that are common to both argument strings).
#A function that calls each of the functions above in order to show that they work correctly
#and provides all data to run them so the user of the main program doesn't have to provide inputs for the other 9 functions.
#Be sure to use comments for both structure of the program and documentation of the code.
#All code must completely be your own individual work product.

#===========================================================================================================================================================




#======================================================== Global Variables and Imports  =========================================================================
#import random and re (re will allow us to exclude integers from a character only string later on)
#set name, major, message, sentence, wordMatch1, wordMatch2 to empty string variables
#set age, number, count to int variables with a value of 0
#set start, run, retry to True
#===========================================================================================================================================================

import random
import re

name = ''
major = ''
message = ''
sentence = ''
wordMatch1 = ''
wordMatch2 = ''
age = 0
number = 0
count = 0
start = True
run = True
retry = True

#=============================================================  Display function  ==============================================================================================

#define display() as a function
    #call global variables name, major, and retry (this allows us to recall and change them)
        #The while loop allows us to control how long to run the function with retry being our sentinel
            #prints the strings 'name' and 'major
            #establish change as an input variable asking if the user would like to change info
            #if yes then it asks user to re-enter specific info pertaining to that function
                #runs the display() function again
            #else set 'retry' to FALSE (this exits out of the loop)
            
#===========================================================================================================================================================


def display():
    global name
    global major
    global retry
    while retry == True:
        print ('----------------------------------------------------------------------')
        print ('\n Your name is:', name,'\n', 'and your major is:', major, '\n')
        print ('----------------------------------------------------------------------')

        change = input('Would you like to change some information? enter y for yes: ')
        if change == 'y' or change == 'Y':
            name = input('Please enter your first and last name: ')
            major = input('Please enter your major: ')
            display()
        else:
            retry = False

#=============================================================  ageInput function  ==============================================================================================
#define ageInput() as a function
    #call global variables age and retry (this allows us to recall and change them)
    #The while loop allows us to control how long to run the function with retry being our sentinel
        #prints out the string 'age' that the user previously entered
        #establish change as an input variable asking if the user would like to change info
        #if yes then it asks user to re-enter specific info pertaining to that function
            #runs the ageInput() function again
        #else set 'retry' to FALSE (this exits out of the loop)
#===========================================================================================================================================================

def ageInput():
    global age
    global retry
    while retry == True:
        print ('----------------------------------------------------------------------')
        print ('\nyour age is ', format(age, '.0f'), '\n')
        print ('----------------------------------------------------------------------')
        
        change = input('Would you like to change your age? enter y for yes: ')
        if change == 'y' or change == 'Y':
            age = int(input('Please enter you age: '))
            ageInput()
        else:
            retry = False

#=============================================================  helloStr function  ==============================================================================================
#define helloStr() as a function
    #call global variables name and retry (this allows us to recall and change them)
    #The while loop allows us to control how long to run the function with retry being our sentinel
        #prints out the string 'name' that the user previously entered with a personal greeting
        #establish change as an input variable asking if the user would like to change info
        #if yes then it asks user to re-enter specific info pertaining to that function
            #runs the helloStr() function again
        #else set 'retry' to FALSE (this exits out of the loop)
#===========================================================================================================================================================

def helloStr():
    global name
    global retry
    while retry == True:
        print ('----------------------------------------------------------------------')
        print('\nHello', name, 'it is very nice to meet you today!\n')
        print ('----------------------------------------------------------------------')
        
        change = input('Would you like to change your name? enter y for yes: ')
        if change == 'y' or change == 'Y':
            name = input('Please enter your first and last name: ')
            helloStr()
        else:
            retry = False
        
#=============================================================  negInteger function  ==============================================================================================
#define negInteger() as a function
    #call global variables number and retry (this allows us to recall and change them)
    #The while loop allows us to control how long to run the function with retry being our sentinel
        #prints out the string 'number' that the user previously entered
        #prints out the opposite of 'number' by using '-number'
        #establish change as an input variable asking if the user would like to change info
        #if yes then it asks user to re-enter specific info pertaining to that function
            #runs the negInteger() function again
        #else set 'retry' to FALSE (this exits out of the loop)
#===========================================================================================================================================================

def negInteger():
    global number
    global retry
    while retry == True:
        print ('----------------------------------------------------------------------')
        print ('\nyou previously entered', number)
        print ('your inverted number is:', format(-number,'.0f'), '\n')
        print ('----------------------------------------------------------------------')
        
        change = input('Would you like to change the integer? enter y for yes: ')
        if change == 'y' or change == 'Y':
            number = int(input('Please enter an integer: '))
            negInteger()
        else:
            retry = False
        
#=============================================================  cntLoop function  ==============================================================================================
#define cntLoop() as a function
    #call global variables count, message, and retry (this allows us to recall and change them)
    #The while loop allows us to control how long to run the function with retry being our sentinel
        #prints out the users 'message' as well as displaying how many loops the user had entered
        #establish a 'for' loop with 'count' representing increments in how many times the loop will repeat
            #within the loop it will print 'message' 'count' amount of times
        #establish change as an input variable asking if the user would like to change info
        #if yes then it asks user to re-enter specific info pertaining to that function
            #runs the cntLoop() function again
        #else set 'retry' to FALSE (this exits out of the loop)
#===========================================================================================================================================================

def cntLoop():
    global count
    global message
    global retry
    while retry == True:
        print ('----------------------------------------------------------------------')
        print ('\nYour message was:', message)
        print ('You asked to loop your message', count, 'times, here it is\n')
        print ('----------------------------------------------------------------------')
        for loop in range(count):
            print (message)

        print ('----------------------------------------------------------------------\n')
        change = input('Would you like to change some information? enter y for yes: ')
        if change == 'y' or change == 'Y':
            message = input('Enter in your message: ')
            count = int(input('How many times would you like to loop this message: '))
            cntLoop()
        else:
            retry = False

#=============================================================  cntLoop function  ==============================================================================================
#define getBiggest() as a function
    #call the global variable retry (this will be our sentinel)
    #establish 'num1' and 'num2' as empty lists using []
    #The while loop allows us to control how long to run the function with retry being our sentinel
        #establish a 'for' loop with 10 being the number of increments in 'i'
            #inside here we append a random range of numbers from 1 to 100
            #since this loops 10 times, there will be 10 random numbers inside of 'num1' and 'num2'
        #find the max number in each list by using 'max(num1/2)' and set that as its own variable
        #print all numbers in both lists, then use the .format() method to print the max number from each list
        #establish an if elif and else statement to find out which number is the greatest or if it is the same
        #if maxNum1 > maxNum2 then print maxNum1 and vice versa
        #else then they are both the same, so print maxNum1
        #establish change as an input variable asking if the user would like to restart
        #if yes 
            #uses 'del' to get rid of the items in both lists so we can start off with an empty list
            #runs the getBiggest() function again
        #else set 'retry' to FALSE (this exits out of the loop)
#===========================================================================================================================================================

def getBiggest():
    global retry
    num1 = []
    num2 = []
    while retry == True:
        for i in range(10):
            num1.append(random.randrange(1,101,1))
            num2.append(random.randrange(1,101,1))
        
        maxNum1 = max(num1)
        maxNum2 = max(num2)
        print ('----------------------------------------------------------------------')
        print ('\nSet 1 =', num1)
        print ('Set 1 =', num2)
        print ('the first max number is: ', format(maxNum1, '.0f'))
        print ('the second max number is: ', format(maxNum2, '.0f'), '\n')
        print ('----------------------------------------------------------------------')

        if maxNum1 > maxNum2:
            print ('the max number is: ', format(maxNum1, '.0f'))
        elif maxNum2 > maxNum1:
            print ('the max number is: ', format(maxNum2, '.0f'))
        else:
            print ('Both numbers are the same, so the max is: ', format(maxNum1, '.0f'))
            
        change = input('Would you like to replay this? enter y for yes: ')
        if change == 'y' or change == 'Y':
            del num1[:]
            del num2[:]
            getBiggest()
        else:
            retry = False

#=============================================================  strTest function  ==============================================================================================
#define cntLoop() as a function
    #call global variables sentence and retry (this allows us to recall and change them)
    #set the local variable 'cnt' to 0
    #The while loop allows us to control how long to run the function with retry being our sentinel
        #print what the users previous sentence was along with what it found
        #establish a 'for' loop for 'c' with 'sentence' set as the sequence
            #establish an 'if' statement with 'c' representing items from 'sentence'
            #use 'isupper()' method to scan the sequence 'c' and find uppercase letters
            #with each one found use 'cnt += 1' to add 1 to cnt so we can total it up later
        #print the total of uppercase letters, 'cnt' added from that 'for' loop
        #establish change as an input variable asking if the user would like to change info
        #if yes then it asks user to re-enter specific info pertaining to that function
            #sets cnt to 0 so that when the program restarts the previous total is not there
            #runs the strTest() function again
        #else set 'retry' to FALSE (this exits out of the loop)
#===========================================================================================================================================================

def strTest():
    global sentence
    global retry
    cnt = 0
    while retry == True:
        print ('----------------------------------------------------------------------')
        print ('\nYour previous sentence was:', sentence)
        print('This is what I found:\n')
        print ('----------------------------------------------------------------------')

        for c in sentence:
            if c.isupper():
                cnt += 1
        print('There are', cnt, 'upper case letters in your sentence')
        
        change = input('Would you like to change your sentence? enter y for yes: ')
        if change == 'y' or change == 'Y':
            sentence = input('Enter a sentence with many capital letters: ')
            cnt = 0
            strTest()
        else:
            retry = False

#=============================================================  getMiddle function  ==============================================================================================
#define getMiddle() as a function
    #call the global variable retry (this will be our sentinel)
    #establish 'num1' as an empty list using []
    #The while loop allows us to control how long to run the function with retry being our sentinel
        #establish a 'for' loop with 3 being the number of increments in 'i'
            #inside here we append a random range of numbers from 1 to 10
            #since this loops 3 times, there will be 3 random numbers inside of 'num1' and 'num2'
        #we then use sort() to set the numbers in numberical order(this will make it easier to determine the middle number)
        #print the sorted list
        #establish an 'if', 'elif', and 'else' statement to determine a common number if there is no middle number
            #the 0 in 'num1[0]' represents the 1st item in the list
            #so if the 1st item ([0]) and the 2nd item ([1]) are the same then print out 'num1[0]'
            #if the 2nd item ([1]) and the 3rd item ([2]) are the same then print out 'num1[2]'
            #else then determine the middle number using [:]
                #establish a 'for' loop with num1 being the sequence
                #we use 'num1[1:2]' to pinpoint the second item in the list, and with 3 being the amount of items in the list we determined the middle num
        #establish change as an input variable asking if the user would like to retry
        #if yes 
            #uses 'del' to get rid of the items from 'num1[]' so we can start off with an empty list
            #runs the getMiddle() function again
        #else set 'retry' to FALSE (this exits out of the loop)
#===========================================================================================================================================================

def getMiddle():
    global retry
    num1 = []
    while retry == True:
        for i in range(3):
            num1.append(random.randrange(1,11,1))
        num1.sort()
        print ('----------------------------------------------------------------------')
        print ('\n', num1)
        if num1[0] == num1[1]:
            print('since it repeats, the most common number is ', num1[0], '\n')
            print ('----------------------------------------------------------------------')
        elif num1[1] == num1[2]:
            print('since it repeats, the most common number is ',num1[2], '\n')
            print ('----------------------------------------------------------------------')
        else:
            for item in num1[1:2]:
                print ('the middle number is ',item, '\n')
                print ('----------------------------------------------------------------------')
                
        change = input('Would you like to replay this? enter y for yes: ')
        if change == 'y' or change == 'Y':
            del num1[:]
            getMiddle()
        else:
            retry = False

#=============================================================  strMatching function  ==============================================================================================
#define strMatching() as a function
    #call global variables wordMatch1, wordMatch2, and retry (this allows us to recall and change them)
    #set strMatch to TRUE (this will be another sentinel along with retry)
    #The 'retry' while loop allows us to control how long to run the function with retry being our sentinel
        #The 'strMatch' while loop allows us to control how long to run the function with strMatch being our sentinel
            #create an empty list named 'letters'
            #establish a 'for' loop with the variable being 'ch' and the sequence being named 'wordMatch1'
                #if 'ch' in wordMatch2 is found in wordMatch1 continue
                    #if the letters found in wordMatch 1 and 2 are not in the list 'letters'
                        #then we will append (add) those letters into the list and set 'strMatch' to FALSE exiting us out of the loop
        #print what the user inputed for both wordMatch1 and wordMatch2
        #then print the the list 'letters'
        #establish change as an input variable asking if the user would like to change info
        #if yes then it asks user to re-enter specific info pertaining to that function
            #uses 'del' to get rid of the items from 'letters[]' so we can start off with an empty list
            #sets strMatch to TRUE so the while loop can become valid
            #runs the strMatching() function again
        #else set 'retry' to FALSE (this exits out of the loop)
#===========================================================================================================================================================

def strMatching():
    global wordMatch1
    global wordMatch2
    global retry
    strMatch = True
    while retry == True:
        while strMatch is True:
            letters = []
            for ch in wordMatch1:
                if ch in wordMatch2:
                    if ch not in letters:
                        letters.append(ch)
                        strMatch = False
        print ('----------------------------------------------------------------------')
        print ('\nYour first word to compare was:', wordMatch1)
        print ('Your second word to compare was:', wordMatch2)
        print ('The letters that are in both words are: ', letters, '\n')
        print ('----------------------------------------------------------------------')
        
        change = input('Would you like to change your two words? enter y for yes: ')
        if change == 'y' or change == 'Y':
            wordMatch1 = input('first word to compare: ')
            wordMatch2 = input('second word to compare: ')
            del letters[:]
            strMatch = True
            strMatching()
        else:
            retry = False

#=============================================================  inputFunction function  ==============================================================================================
#define inputFunction() as a function
    #call global variables name, major, age, number, message, count, sentence, wordMatch1, wordMatch2, and start (this allows us to recall and change them)
    #issue a try/catch statement starting with 'try'
        #The 'start' while loop allows us to control how long to run the function with start being our sentinel
            #establish 'name' as a user input asking what his/her name is
            #use re.match() to only look for letters a-zA-z and whitespaces '\s'
            #if the characters entered are within the limit then proceed to the second input
                #repeat this step for every STRING input there is except for the int(input()
                    #age, number, and count ask the user to input an integer
                    #if it is not an integer then the try/catch except loop will catch it and restart the program indicating an error
                #all the else statements are there if the user doesn't enter a valid character
                #if that happens then it prints out an error and restart inputFunction()
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error and restarts inputFunction()
#===========================================================================================================================================================

def inputFunction():
    global name
    global major
    global age
    global number
    global message
    global count
    global sentence
    global wordMatch1
    global wordMatch2
    global start
    print ('before we run the official program we would like to ask you to enter some information first')
    try:
        while start == True:
            name = input('Please enter your first and last name: ')
            if re.match("^[a-zA-Z\s]*$", name):
                major = input('Please enter your major: ')
                if re.match("^[a-zA-Z\s]*$", major):
                    age = int(input('Please enter you age: '))
                    number = int(input('Please enter an integer: '))
                    message = input('Enter in your message: ')
                    if re.match("^[a-zA-Z\s]*$", message):
                        count = int(input('How many times would you like to loop your message: '))
                        sentence = input('Enter a sentence with many capital letters: ')
                        if re.match("^[a-zA-Z\s]*$", sentence):
                            wordMatch1 = input('first word to compare: ')
                            if re.match("^[a-zA-Z\s]*$", wordMatch1):
                                wordMatch2 = input('second word to compare: ')
                                if re.match("^[a-zA-Z\s]*$", wordMatch2):
                                    start = False
                                else:
                                    print ("Error! Only letters a-z allowed!")
                                    inputFunction()
                            else:
                                print ("Error! Only letters a-z allowed!")
                                inputFunction()
                        else:
                            print ("Error! Only letters a-z allowed!")
                            inputFunction()
                    else:
                        print ("Error! Only letters a-z allowed!")
                        inputFunction()
                else:
                    print ("Error! Only letters a-z allowed!")
                    inputFunction()
            else:
                print ("Error! Only letters a-z allowed!")
                inputFunction()
                
    except ValueError:
        print ('That is not a valid input')
        inputFunction()
    except UnboundLocalError:
        print ('That is not a valid input')
        inputFunction()

#=============================================================  main function  ==============================================================================================
#define main() as a function
    #execute inputFunction()
    #call global variables run and retry
    #issue a try/catch statement starting with 'try'
    #The 'run' while loop allows us to control how long to run the function with run being our sentinel
        #establish a local variable 'choice' and set it to 0
        #establish 'choice' as a user int(input() asking what type of function he/she would like to run
        #we use multiple 'if' statements to deteremine which function the user wants to run
        #if 'choice' is 1 then it runs the first function being 'display()'
        #set 'retry' to True to start the function with its replay loop
        #if 'choice' is 2 then it runs the second function being 'ageInput()'
        #set 'retry' to True to start the function with its replay loop
        #if 'choice' is 3 then it runs the third function being 'helloStr()'
        #set 'retry' to True to start the function with its replay loop
        #if 'choice' is 4 then it runs the fourth function being 'negInteger()'
        #set 'retry' to True to start the function with its replay loop
        #if 'choice' is 5 then it runs the fifth function being 'cntLoop()'
        #set 'retry' to True to start the function with its replay loop
        #if 'choice' is 6 then it runs the six function being 'getBiggest()'
        #set 'retry' to True to start the function with its replay loop
        #if 'choice' is 7 then it runs the seventh function being 'strTest()'
        #set 'retry' to True to start the function with its replay loop
        #if 'choice' is 8 then it runs the eigth function being 'getMiddle()'
        #set 'retry' to True to start the function with its replay loop
        #if 'choice' is 9 then it runs the ninth function being 'strMatching()'
        #set 'retry' to True to start the function with its replay loop
        #if 'choice' is 10 then it exits and asks the user to hit ENTER to exit
        #else: if the user does not enter any one of these numbers then they are prompted to enter a number between 1 and 10
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================

def main():
    inputFunction()
    global run
    global retry
    while run == True:
        try:
            choice = 0
            choice = int(input('\nPlease select what function to test\n\n(1)'
                               ' Tell me my name and major.\t(6) Generates list and gets biggest'
                               ' of 2 lists.\n\n(2) Repeat my age '
                               'back to me.\t(7) Count capatalized letters in '
                               'a statement.\n\n(3) Give me a greeting\t\t(8) '
                               'Find a middle value\n\n(4) Reverse a number'
                               '\t\t(9) Find simular letters in 2 words \n\n(5)'
                               ' Create and loop a message.'
                               '\t(10) Exit\n\n---------------------------------'
                               '-----------------------------------------\n:'))
            if choice == 1:
                retry = True
                display()
            if choice == 2:
                retry = True
                ageInput()
            if choice == 3:
                retry = True
                helloStr()
            if choice == 4:
                retry = True
                negInteger()
            if choice == 5:
                retry = True
                cntLoop()
            if choice == 6:
                retry = True
                getBiggest()
            if choice == 7:
                retry = True
                strTest()
            if choice == 8:
                retry = True
                getMiddle()
            if choice == 9:
                retry = True
                strMatching()
            if choice == 10:
                input('Exit\nPress enter to exit.')
                run = False
            else:
                print ('You Need To Enter A Number Between 1 and 10')

        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')

#executes the entire program
main()
