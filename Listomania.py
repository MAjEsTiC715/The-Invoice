#========================================================  Documentation  ==================================================================================
#Write a function that takes a list of any size as an argument, and returns a list where all adjacent, equal elements have been reduced to a single element.
    #For example [1, 2, 2, 3] would return as [1, 2, 3].
#Write a function that takes a list of numbers of any size as an argument and returns true if the list is sorted, and false otherwise.
    #For example, [1, 2, 3] would return True, and [2,1,3] would return false
#Write a function that takes a list of numbers of any size as an argument, and returns the sum of the numbers.
    #For example, [1,2,2,3] returns 8.
#Write a function that takes a list of any type and size as an argument, and returns a list where the elements are in reverse list order.
    #For example ['rubber', 'baby', 'bellybutton'] returns ['bellybutton', 'baby', 'rubber']
#Write a function that takes two sorted lists as arguments, and returns a single sorted list.
    #For example, providing lists [1, 5, 7] and [1, 2, 4] results in [1,1,2,4,5,7].
#Write a function that demonstrates and tests each of the above functions.
#Be sure to use comments for both structure of the program and documentation of the code.
#All code must completely be your own individual work product.
#===========================================================================================================================================================

#imports the 'random' library 
import random

#set 'retry' and 'run' as True (these will be used as global functions)
retry = True
run = True

#=============================================================  sort_list function  ==============================================================================================
#define sort_list() as a function
    #call global variable retry 
    #The while loop allows us to control how long to run the function with retry being our sentinel
        #establish a try catch method
            #create a list called 'numList'
            #ask the user 'How many items would you like your list to have' using int(input() with increment being the variable
            #ask the user what they want they range of numbers using int(input() with 'minNum' and 'maxNum' being the variable
            #establish a 'for' loop using i in range('increment') increment is the integer the user entered
                #we then append 1 random number for 'increment' amount of times using 'minNum' and 'maxNum' as our range
            #use .sort() to sort the list
            #print the original list and use list(set() to turn it into a set and get rid of duplicate items
            #use .sort() again then print 'numList' without duplicates
            #establish change as an input variable asking if the user would like to replay the function
            #if yes
                #uses 'del' to delete the items in 'numList'
                #runs the sort_list() function again
            #else set 'retry' to FALSE (this exits out of the loop)
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================

def sort_list():
    global retry
    while retry == True:
        try:
            numList = []
            increment = int(input('How many items would you like your list to have? '))
            print ('\nEnter a range of numbers you want to generate\n')
            minNum = int(input('Enter the min: '))
            maxNum = int(input('Enter the max: '))
    
            for i in range(increment):
                numList.append(random.randrange(minNum,maxNum,1))
            numList.sort()
            print ('----------------------------------------------------------------------')
            print ('\nhere is the original list\n', numList)
            numList = list(set(numList))
            numList.sort()
            print ('\nhere is the list without duplicates\n', numList, '\n')
            print ('----------------------------------------------------------------------')
            
            change = input('Would you like to replay this? enter y for yes: ')
            if change == 'y' or change == 'Y':
                del numList[:]
                sort_list()
            else:
                retry = False
        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')

#=============================================================  sorted_list function  ==============================================================================================
#define sorted_list() as a function
    #call global variable retry 
    #The while loop allows us to control how long to run the function with retry being our sentinel
        #establish a try catch method
            #create a list called 'notSortedList' and 'sortedList'
            #ask the user 'How many items would you like your list to have' using int(input() with increment being the variable
            #establish a 'for' loop using i in range('increment') increment is the integer the user entered
                #we then append each of the users numbers for 'increment' amount of times
            #use .sort() to sort 'sortedList' we will use this to compare the unsorted list to the sorted list to determine if it is true
            #if items in 'sortedList' are equal in sequence with 'notSortedList' (which is users input)
                #print 'numbers are sorted'
            #else
                #print the users orginal input saying that they are not sorted
                #print the sorted version
            #establish change as an input variable asking if the user would like to replay the function
            #if yes
                #uses 'del' to delete the items in 'sortedList' and 'notSortedList'
                #runs the sorted_list() function again
            #else set 'retry' to FALSE (this exits out of the loop)
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================

def sorted_list():
    global retry
    while retry == True:
        try:
            notSortedList = []
            sortedList = []
            increment = int(input('How many items would you like your list to have? '))
            print ('\n----------------------------------------------------------------------\n')
            
            for i in range(increment):
                a = int(input('Enter any number you like:'))
                notSortedList.append(a)
                sortedList.append(a)
            sortedList.sort()
            if sortedList[:] == notSortedList[:]:
                print ('----------------------------------------------------------------------')
                print ('\nThe numbers you entered are sorted\n')
                print ('----------------------------------------------------------------------')
            else:        
                print ('----------------------------------------------------------------------')
                print ('\nThe numbers you entered are not sorted\n', notSortedList)
                print ('\nHere is your sorted list\n', sortedList, '\n')
                print ('----------------------------------------------------------------------')
            
            change = input('Would you like to replay this? enter y for yes: ')
            if change == 'y' or change == 'Y':
                del notSortedList[:]
                del sortedList[:]
                sorted_list()
            else:
                retry = False
        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')

#=============================================================  sum_list function  ==============================================================================================
#define sum_list() as a function
    #call global variable retry 
    #The while loop allows us to control how long to run the function with retry being our sentinel
        #establish a try catch method
            #create a list called 'numList'
            #ask the user 'How many items would you like your list to have' using int(input() with increment being the variable
            #ask the user what they want they range of numbers using int(input() with 'minNum' and 'maxNum' being the variable
            #establish a 'for' loop using i in range('increment') increment is the integer the user entered
                #we then append 1 random number for 'increment' amount of times using 'minNum' and 'maxNum' as our range
            #use .sort() to sort the list
            #print 'numList'
            #use sum() to add the items in the list then print them
            #establish change as an input variable asking if the user would like to replay the function
            #if yes
                #uses 'del' to delete the items in 'numList'
                #runs the sum_list() function again
            #else set 'retry' to FALSE (this exits out of the loop)
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================

def sum_list():
    global retry
    while retry == True:
        try:
            numList = []
            increment = int(input('How many items would you like your list to have? '))
            print ('\nEnter a range of numbers you want to generate\n')
            minNum = int(input('Enter the min: '))
            maxNum = int(input('Enter the max: '))
                
            for i in range(increment):
                numList.append(random.randrange(minNum,maxNum,1))
            print ('----------------------------------------------------------------------')
            numList.sort()
            print ('\nhere is the original list not sorted\n', numList)
            print ('\nthe sum of the list is: ', sum(numList), '\n')
            print ('----------------------------------------------------------------------')
            
            change = input('Would you like to replay this? enter y for yes: ')
            if change == 'y' or change == 'Y':
                del numList[:]
                sum_list()
            else:
                retry = False
        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')

#=============================================================  reverse_list function  ==============================================================================================
#define reverse_list() as a function
    #call global variable retry 
    #The while loop allows us to control how long to run the function with retry being our sentinel
        #establish a try catch method
            #create a list called 'anyList'
            #ask the user 'How many items would you like your list to have' using int(input() with increment being the variable
            #establish a 'for' loop using i in range('increment') increment is the integer the user entered
                #we ask the user to enter a word or number using 'a' as the argument
                #we then append each of the users words/numbers for 'increment' amount of times into 'anyList'
            #print 'anyList'
            #use .reverse() to reverse the list
            #print 'anyList' (this time the order should be reversed)
            #establish change as an input variable asking if the user would like to replay the function
            #if yes
                #uses 'del' to delete the items in 'anyList'
                #runs the reverse_list() function again
            #else set 'retry' to FALSE (this exits out of the loop)
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================

def reverse_list():
    global retry
    while retry == True:
        try:
            anyList = []
            increment = int(input('How many items would you like your list to have? '))
            
            for i in range(increment):
                a = input('Enter any word or number you like: ')
                anyList.append(a)
            print ('----------------------------------------------------------------------')
            print ('\nhere is the original list\n', anyList)
            anyList.reverse()
            print ('\nthe sum of the list is: ', anyList, '\n')
            print ('----------------------------------------------------------------------')
                
            change = input('Would you like to replay this? enter y for yes: ')
            if change == 'y' or change == 'Y':
                del anyList[:]
                reverse_list()
            else:
                retry = False
        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')

#=============================================================  double_list function  ==============================================================================================
#define double_list() as a function
    #call global variable retry 
    #The while loop allows us to control how long to run the function with retry being our sentinel
        #establish a try catch method
            #create a list called 'numList' and 'numList2'
            #ask the user 'How many items would you like your list to have' using int(input() with 'increment' and 'increment2' being the variables
            #ask the user what they want they range of numbers using int(input() with 'minNum' and 'maxNum' being the variable
            #establish two 'for' loops using i in range('increment' and 'increment2') increment is the integer the user entered
                #we then append 1 random number for 'increment' or 'increment2' amount of times using 'minNum' and 'maxNum' as our range for both
            #use .sort() to sort both lists
            #print 'numList' and 'numList2'
            #create a third list called 'numList3' then add 'numList' and 'numList2' to concatenate the two lists into one
            #use .sort() to sort 'numList3'
            #print 'numList3'
            #establish change as an input variable asking if the user would like to replay the function
            #if yes
                #uses 'del' to delete the items in 'numList' 'numList2' 'numList3'
                #runs the double_list() function again
            #else set 'retry' to FALSE (this exits out of the loop)
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================
  
def double_list():
    global retry
    while retry == True:
        try:
            numList = []
            numList2 = []
            increment = int(input('How many items would you like list 1 to have? '))
            increment2 = int(input('How many items would you like list 2 to have? '))
            print ('\nEnter a range of numbers you want to generate\n')
            minNum = int(input('Enter the min: '))
            maxNum = int(input('Enter the max: '))
    
        
            for i in range(increment):
                numList.append(random.randrange(minNum,maxNum,1))
            for i in range(increment2):
                numList2.append(random.randrange(minNum,maxNum,1))
            numList.sort()
            numList2.sort()
            print ('----------------------------------------------------------------------')
            print ('\nhere is list 1\n', numList)
            print ('\nhere is list 2\n', numList2)
            numList3 = numList + numList2
            numList3.sort()
            print ('\nhere is list 1 and 2 combined\n', numList3)
            print ('----------------------------------------------------------------------')
            
            change = input('Would you like to replay this? enter y for yes: ')
            if change == 'y' or change == 'Y':
                del numList[:]
                del numList2[:]
                del numList3[:]
                double_list()
            else:
                retry = False
        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')

#=============================================================  main function  ==============================================================================================
#define main() as a function
    #call global variables run and retry
    #issue a try/catch statement starting with 'try'
    #The 'run' while loop allows us to control how long to run the function with run being our sentinel
        #establish a local variable 'choice' and set it to 0
        #establish 'choice' as a user int(input() asking what type of function he/she would like to run
        #we use multiple 'if' statements to deteremine which function the user wants to run
        #if 'choice' is 1 then it runs the first function being 'sort_list()'
            #set 'retry' to True to start the function with its replay loop
        #if 'choice' is 2 then it runs the second function being 'sorted_list()'
            #set 'retry' to True to start the function with its replay loop
        #if 'choice' is 3 then it runs the third function being 'sum_list()'
            #set 'retry' to True to start the function with its replay loop
        #if 'choice' is 4 then it runs the fourth function being 'reverse_list()'
            #set 'retry' to True to start the function with its replay loop
        #if 'choice' is 5 then it runs the fifth function being 'double_list()'
            #set 'retry' to True to start the function with its replay loop
        #if 'choice' is 6 then it exits and asks the user to hit ENTER to exit
        #else: if the user does not enter any one of these numbers then they are prompted to enter a number between 1 and 6
    #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
    #if triggered it prints out an error
#===========================================================================================================================================================

def main():
    global run
    global retry
    while run == True:
        try:
            choice = 0
            choice = int(input('\nPlease select what function to test\n\n(1)'
                               ' Generate a list of numbers and sort it with no duplicates.'
                               '\n\n(2) Enter a list and determines if it is sorted or not. '
                               '\n\n(3) Generate a list of numbers and finds the sum'
                               '\n\n(4) Create a list and reverse.'
                               '\n\n(5) Takes two lists and combines them.\n\n'
                               '(6) Exit\n\n---------------------------------'
                               '-----------------------------------------\n:'))
            if choice == 1:
                retry = True
                sort_list()
            if choice == 2:
                retry = True
                sorted_list()
            if choice == 3:
                retry = True
                sum_list()
            if choice == 4:
                retry = True
                reverse_list()
            if choice == 5:
                retry = True
                double_list()
            if choice == 6:
                input('Exit\nPress enter to exit.')
                run = False
            else:
                print ('You Need To Enter A Number Between 1 and 6')

        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')

#executes the entire program
main()
