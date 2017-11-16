#========================================================  Documentation  ==================================================================================
#Program Starts and asks the user whether they want to count vowels or consonants or quit. The input value is stored as a "mode".
#If user provides input other than "consonant" or "vowel" or "quit", program interprets this as an error and re-asks for input.
#Program asks for a word.
#Depending on mode, the number of consonants or vowels are calculated and reported to the user.
#Program asks if another word is available. If so, steps 2 through 4 are repeated, otherwise continue to step 5.
#Average vowels per word or average consonants per word are reported to the user.
#Be sure to use comments for both structure of the program and documentation of the code.
#All code must completely be your own individual work product.
#===========================================================================================================================================================

#imports the random and re library
import random
import re

#set 'add' and 'run' as True (these will be used as global functions)
add = True
run = True

#========================================================  getVowel(v_dic) Function  ==================================================================================
#define getVowel(v_dic) as a function
    #call global variable 'add'
    #create variables v_num = 0 and v_List = all vowels (this can be considered our control variable to find vowels in certain words)
    #The while loop allows us to control how long to run the function with 'add' being our sentinel
        #establish a try catch method
            #ask the user 'How many words would you like to enter?' using int(input() with increment being the variable
            #establish a 'for' loop using w in range('increment') increment is the integer the user entered
                #we then ask the user to enter a word with 'v_Word' being the argument
                #establish an if statement using 're.match()' to check if the letters entered are not integers or any unknown character
                    #if true then convert 'v_Word' to all lower case letters using .lower() with 'v_Lower' being the new argument
                    #establish an if statement that checks if the users word now 'vLower' is in the list 'v_dic'
                        #if not in the list then we use .append() to put it into the list
                        #establish a for loop for v in 'vLower' to check for vowels in our 'v_List)
                            #if v is found in 'vLower' and 'v_List' then we add 1 to 'v_num'
                    #establish an else statement to catch if 'vLower' is in the list 'v_dic' (RESTARTS function if triggered)
                #establish an else statement to catch if 'v_Word' doesn't match a letter (RESTARTS function if triggered)
            #calculate the average vowels per word by dividing 'v_num' by 'increment' with 'v_avg' being the new variable
            #print the amount of words entered with the total vowels in all with the average using the .format() method
            #have the user press ENTER to go back to the main menu
            #set add = False to exit out of while loop
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================

def getVowel(v_dic):
    global add

    v_List = ('aeiouy')
    v_num = 0
    
    while add == True:
        try:
            increment = int(input('How many words would you like to enter? '))
            print ('--------------------------------------------------------------------------\n')
            for w in range(increment):
                v_Word = input('Enter a word: ')
                if re.match("^[a-zA-Z]*$", v_Word):
                    vLower = v_Word.lower()
                    if vLower not in v_dic:
                        v_dic.append(vLower)
                        for v in vLower:
                            if v in v_List:
                                v_num += 1
                    else:
                        print ('that word has already been used')
                        getVowel(v_dic)
                else:
                    print ('You entered an invalid number or added more than one word.')
                    getVowel(v_dic)
            print ('\n--------------------------------------------------------------------------\n')
            v_avg = v_num // increment
            print ('You entered', format(increment, '.0f'), 'words with', format(v_num, '.0f'), 'vowels\nYour average vowels per word is', format(v_avg, '.0f'))
            print ('\n--------------------------------------------------------------------------\n')
            input ('press ENTER to go to main menu')
            add = False
        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')

#========================================================  getConsonant(c_dic)  ==================================================================================
#define getConsonant(c_dic) as a function
    #call global variable 'add'
    #create variables c_num = 0 and c_List = all consonants (this can be considered our control variable to find vowels in certain words)
    #The while loop allows us to control how long to run the function with 'add' being our sentinel
        #establish a try catch method
            #ask the user 'How many words would you like to enter?' using int(input() with increment being the variable
            #establish a 'for' loop using w in range('increment') increment is the integer the user entered
                #we then ask the user to enter a word with 'c_Word' being the argument
                #establish an if statement using 're.match()' to check if the letters entered are not integers or any unknown character
                    #if true then convert 'c_Word' to all lower case letters using .lower() with 'cLower' being the new argument
                    #establish an if statement that checks if the users word now 'cLower' is in the list 'c_dic'
                        #if not in the list then we use .append() to put it into the list
                        #establish a for loop for v in 'cLower' to check for vowels in our 'c_List)
                            #if c is found in 'cLower' and 'c_List' then we add 1 to 'c_num'
                    #establish an else statement to catch if 'cLower' is in the list 'c_dic' (RESTARTS function if triggered)
                #establish an else statement to catch if 'c_Word' doesn't match a letter (RESTARTS function if triggered)
            #calculate the average consonants per word by dividing 'c_num' by 'increment' with 'c_avg' being the new variable
            #print the amount of words entered with the total consonants in all with the average using the .format() method
            #have the user press ENTER to go back to the main menu
            #set add = False to exit out of while loop
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================

def getConsonant(c_dic):
    global add
    
    c_List = ('bcdfghjklmnpqrstvwxz')
    c_num = 0

    while add == True:
        try:
            increment = int(input('How many words would you like to enter? '))
            print ('--------------------------------------------------------------------------\n')
            for w in range(increment):
                c_Word = input('Enter a word: ')
                if re.match("^[a-zA-Z]*$", c_Word):
                    cLower = c_Word.lower()
                    if cLower not in c_dic:
                        c_dic.append(cLower)
                        for c in cLower:
                            if c in c_List:
                                c_num += 1
                    else:
                        print ('that word has already been used')
                        getConsonant(c_dic)
                else:
                    print ('You entered an invalid number or added more than one word.')
                    getConsonant(c_dic)
            print ('\n--------------------------------------------------------------------------\n')
            c_avg = c_num // increment
            print ('You entered', format(increment, '.0f'), 'words with', format(c_num, '.0f'), 'vowels\nYour average vowels per word is', format(c_avg, '.0f'))
            print ('\n--------------------------------------------------------------------------\n')
            input ('press ENTER to go to main menu')
            add = False
        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')
                    
#========================================================  vowel_check(v_dic)  ==================================================================================
#define vowel_check(v_dic) as a function
    #call global variable 'add'
    #The while loop allows us to control how long to run the function with 'add' being our sentinel
        #establish a try catch method
            #ask user if they would like see their previous list
            #if yes then check if there is anything in the list
                #if 'v_dic' == [] then print that there are no words in the list
                #else: print the list and ask the user if they would like to change some information
                    #if it is y then it asks user if they want to add or delete an item from the vowel list
                        #if the input was 'delete' then we ask how many words would they like to delete
                        #if the number of items entered was greater than or equal to the length of 'v_div'
                            #use the del function to delete all the items in the list
                            #then print 'all words have been deleted
                        #if the input was 'add' then we print the current list
                        #ask the user how many words they would like to add
                        #establish a for loop with a in range of the user input 'add_i'
                            #then ask user to enter a new word
                            #use re.match() to verify that the letters are not integers
                            #if it does match then continue and check if the word is not in 'v_dic'
                                #if true then append 'add_lower' to the list 'v_dic'
                        #establish an else statement to catch if 'add_lower' is in the list 'v_dic' (RESTARTS function if triggered)
                #establish an else statement to catch if 'add_item' doesn't match a letter (RESTARTS function if triggered)
                #prints revised list and asks user to press ENTER to go back to main menu
            #establish two more else statements to catch if 'del_option' is the wrong input (exits out of loop if triggered)
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================

def vowel_check(v_dic):
    global add
    while add == True:
        try:
            viewPrev = input('Welcome to Vowel Check!\nIf you would like to see your previous list enter yes: ')
            viewPrev.lower()
            if viewPrev == 'yes':
                if v_dic == []:
                    print ('----------------------------------------------------------------------\n')
                    print ('uh oh! you have not entered any words yet')
                    input ('press ENTER to go to main menu')
                    add = False
                else:
                    print ('\n----------------------------------------------------------------------\n')
                    print (v_dic)
                    print ('\n----------------------------------------------------------------------\n')
                    change = input('Would you like to change some info? enter y for yes: ')
                    print ('\n----------------------------------------------------------------------\n')
                    if change == 'y' or change == 'Y':
                        del_option = input('Do you want to ADD or DELETE words from your list: ')
                        del_lower = del_option.lower()
                        print ('\n----------------------------------------------------------------------\n')
                        if del_lower == 'delete':
                            print ('Here is your current list:\n', v_dic)
                            delete_i = int(input('How many would you like to delete: '))
                            if delete_i >= len(v_dic):
                                del v_dic[:]
                                print ('\n----------------------------------------------------------------------\n')
                                print ('All words have been deleted from the list')
                            else:
                                for i in range(delete_i):
                                    print ('\n----------------------------------------------------------------------\n')
                                    item = input('Which word would you like to delete? ')
                                    v_dic.remove(item)
                                    print ('Here is your revised list:\n', v_dic)
                                    print ('\n----------------------------------------------------------------------\n')
                            input ('press ENTER to go to main menu')
                            add = False
                        elif del_lower == 'add':
                            print ('\n----------------------------------------------------------------------\n')
                            print ('Here is your current list:\n', v_dic)
                            print ('\n----------------------------------------------------------------------\n')
                            add_i = int(input('How many would you like to add: '))
                            for a in range(add_i):
                                add_item = input('Enter the new word you would like to add: ')
                                if re.match("^[a-zA-Z]*$", add_item):
                                    add_lower = add_item.lower()
                                    if add_lower not in v_dic:
                                        v_dic.append(add_lower)
                                    else:
                                        print ('You already entered that word')
                                        vowel_check(v_dic)
                                else:
                                    print ('You entered an invalid number or added more than one word.')
                                    vowel_check(v_dic)
                            print ('\n----------------------------------------------------------------------\n')
                            print ('Here is your revised list:\n', v_dic)
                            input ('press ENTER to go to main menu')
                            add = False
                        else:
                            print ('\n----------------------------------------------------------------------\n')
                            print ('Sorry you entered an invalid word, bringing you back to the menu')
                            print ('\n----------------------------------------------------------------------\n')
                            add = False
            else:
                add = False
        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')

#========================================================  consonant_check(c_dic)  ==================================================================================
#define consonant_check(c_dic) as a function
    #call global variable 'add'
    #The while loop allows us to control how long to run the function with 'add' being our sentinel
        #establish a try catch method
            #ask user if they would like see their previous list
            #if yes then check if there is anything in the list
                #if 'c_dic' == [] then print that there are no words in the list
                #else: print the list and ask the user if they would like to change some information
                    #if it is y then it asks user if they want to add or delete an item from the consonant list
                        #if the input was 'delete' then we ask how many words would they like to delete
                        #if the number of items entered was greater than or equal to the length of 'c_div'
                            #use the del function to delete all the items in the list
                            #then print 'all words have been deleted
                        #if the input was 'add' then we print the current list
                        #ask the user how many words they would like to add
                        #establish a for loop with a in range of the user input 'add_i'
                            #then ask user to enter a new word
                            #use re.match() to verify that the letters are not integers
                            #if it does match then continue and check if the word is not in 'c_dic'
                                #if true then append 'add_lower' to the list 'v_dic'
                        #establish an else statement to catch if 'add_lower' is in the list 'c_dic' (RESTARTS function if triggered)
                #establish an else statement to catch if 'add_item' doesn't match a letter (RESTARTS function if triggered)
                #prints revised list and asks user to press ENTER to go back to main menu
            #establish two more else statements to catch if 'del_option' is the wrong input (exits out of loop if triggered)
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================

def consonant_check(c_dic):
    global add
    while add == True:
        try:
            viewPrev = input('Welcome to Consonant Check!\nIf you would like to see your previous list enter yes: ')
            viewPrev.lower()
            if viewPrev == 'yes':
                if c_dic == []:
                    print ('----------------------------------------------------------------------\n')
                    print ('uh oh! you have not entered any words yet')
                    input ('press ENTER to go to main menu')
                    add = False
                else:
                    print ('\n----------------------------------------------------------------------\n')
                    print (c_dic)
                    print ('\n----------------------------------------------------------------------\n')
                    change = input('Would you like to change some info? enter y for yes: ')
                    print ('\n----------------------------------------------------------------------\n')
                    if change == 'y' or change == 'Y':
                        del_option = input('Do you want to ADD or DELETE words from your list: ')
                        del_lower = del_option.lower()
                        print ('\n----------------------------------------------------------------------\n')
                        if del_lower == 'delete':
                            print ('Here is your current list:\n', v_dic)
                            delete_i = int(input('How many would you like to delete: '))
                            if delete_i >= len(c_dic):
                                del c_dic[:]
                                print ('\n----------------------------------------------------------------------\n')
                                print ('All words have been deleted from the list')
                            else:
                                for i in range(delete_i):
                                    print ('\n----------------------------------------------------------------------\n')
                                    item = input('Which word would you like to delete? ')
                                    c_dic.remove(item)
                                    print ('Here is your revised list:\n', c_dic)
                                    print ('\n----------------------------------------------------------------------\n')
                            input ('press ENTER to go to main menu')
                            add = False
                        elif del_lower == 'add':
                            print ('\n----------------------------------------------------------------------\n')
                            print ('Here is your current list:\n', c_dic)
                            print ('\n----------------------------------------------------------------------\n')
                            add_i = int(input('How many would you like to add: '))
                            for a in range(add_i):
                                add_item = input('Enter the new word you would like to add: ')
                                if re.match("^[a-zA-Z]*$", add_item):
                                    add_lower = add_item.lower()
                                    if add_lower not in c_dic:
                                        c_dic.append(add_lower)
                                    else:
                                        print ('You already entered that word')
                                        consonant_check(c_dic)
                                else:
                                    print ('You entered an invalid number or added more than one word.')
                                    consonant_check(c_dic)
                            print ('\n----------------------------------------------------------------------\n')
                            print ('Here is your revised list:\n', c_dic)
                            input ('press ENTER to go to main menu')
                            add = False
                        else:
                            print ('\n----------------------------------------------------------------------\n')
                            print ('Sorry you entered an invalid word, bringing you back to the menu')
                            print ('\n----------------------------------------------------------------------\n')
                            add = False
            else:
                add = False
        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')

#========================================================  main() function ========================================================================================
#define main() as a function
    #call global variable 'add' and 'run'
    #creat two list v_dic for the words entered for vowels function
    #and c_dic for the words entered for consonants function (these will be used as local variables
    #The while loop allows us to control how long to run the function with 'run' being our sentinel
        #establish a try catch method
            #establish a local variable 'mode' and set it to 0
            #establish 'mode' as a user int(input() asking what type of function he/she would like to run
            #we use multiple 'if' statements to deteremine which function the user wants to run
            #if 'mode' is 1 then it runs the first function being 'getVowel(v_dic)'
                #set 'add' to True to start the function with its replay loop
            #if 'mode' is 2 then it runs the second function being 'getConsonant(c_dic)'
                #set 'add' to True to start the function with its replay loop
            #if 'mode' is 3 then it runs the third function being 'vowel_check(v_dic)'
                #set 'add' to True to start the function with its replay loop
            #if 'mode' is 4 then it runs the fourth function being 'consonant_check(c_dic)'
                #set 'add' to True to start the function with its replay loop
            #if 'mode' is 5 then it exits and asks the user to hit ENTER to exit
            #else: if the user does not enter any one of these numbers then they are prompted to enter a number between 1 and 6
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================

def main():
    global run
    global add

    v_dic = []
    c_dic = []
    
    while run == True:
        try:
            mode = 0
            mode = int(input('\nPlease select what function to test\n\n(1)'
                               ' Enter a series of words and calculates the total and average vowels per word.'
                               '\n\n(2) Enter a series of words and calculates the total and average consonants per word.\n\n'
                               '(3) Display and change list entered for calculating VOWELS.\n\n'
                               '(4) Display and change list entered for calculating CONSONANTS.\n\n'
                               '(5) Exit\n\n---------------------------------'
                               '-----------------------------------------\n:'))
            if mode == 1:
                add = True
                getVowel(v_dic)
            if mode == 2:
                add = True
                getConsonant(c_dic)
            if mode == 3:
                add = True
                vowel_check(v_dic)
            if mode == 4:
                add = True
                consonant_check(c_dic)
            if mode == 5:
                input('Exit\nPress enter to exit.')
                run = False
            else:
                print ('You Need To Enter A Number Between 1 and 5')

        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')


#executes the entire program    
main()
