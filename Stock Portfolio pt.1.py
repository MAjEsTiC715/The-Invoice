#========================================================  Documentation  ==================================================================================
#The first dictionary, called Names, maps the stock symbol to the company name (example: "GM" maps to "General Motors").
#The second dictionary, called Prices, maps the stock symbol to a list of 2 floating point numbers corresponding to the buy price
    #(the price the user paid for the stock) and the current market price (the price the user could sell the stock for today).
#The third dictionary, called Exposure, maps the stock symbol to a list of 2 floating point numbers, corresponding to the number of shares purchased,
#and the risk associated with holding onto the stock
    #(i.e. How likely the stock is to gain value in the future). The risk associated with holding onto the stock should be a percentage
    #(the stock is high risk so the exposure value would be .5 or the stock is low risk so the exposure value would be .05)
#Your program should have the following functions:
    #addName - Asks the user for a Stock Symbol and Name pairing then adds it to the Names dictionary.
    #addPrices - Takes a Stock Symbol as an input parameter,
        #then asks the user for the Buy price and the Current price of the corresponding stock, adding them to the Prices dictionary.
    #addExposure - Takes a Stock Symbol as an input parameter,
        #then asks the user for the Risk and Shares of the corresponding stock, adding them to the Exposure dictionary.
    #addStock - Calls addName, addPrices, and addExposure to add a new stock to the portfolio.
    #This should have no parameters but should create 2 stocks which means 2 entries in each dictionary with the key in each dictionary being the stock symbol. 
        #Then, the program should display all the information for each stock.
#Be sure to use comments for both structure of the program and documentation of the code.
#All code must completely be your own individual work product.
#===========================================================================================================================================================

import re #import the 're' library

add = True #establish 'add' and 'run' as global variables
run = True

name = {} #establish 3 dictionaries 
price = {}
exposure = {}

stockSym = '' #stockSym is the key for all dictionaries

#========================================================  main() function ========================================================================================
#define main() as a function
    #call global variable 'add' and 'run'
    #The while loop allows us to control how long to run the function with 'run' being our sentinel
        #establish a try catch method
            #establish a local variable 'mode' and set it to 0
            #establish 'mode' as a user int(input() asking what type of function he/she would like to run
            #we use multiple 'if' statements to deteremine which function the user wants to run
            #if 'mode' is 1 then it runs the first function being 'addName(name)'
                #set 'add' to True to start the function with its replay loop
            #if 'mode' is 2 then it runs the second function being 'addPrices(price)'
                #set 'add' to True to start the function with its replay loop
            #if 'mode' is 3 then it runs the third function being 'addExposure(exposure)'
                #set 'add' to True to start the function with its replay loop
            #if 'mode' is 4 then it runs the fourth function being 'addStock(name, price, exposure)'
                #set 'add' to True to start the function with its replay loop
            #if 'mode' is 5 then it runs the fourth function being 'findStock(name, price, exposure)'
                #set 'add' to True to start the function with its replay loop
            #if 'mode' is 6 then it exits and asks the user to hit ENTER to exit
            #else: if the user does not enter any one of these numbers then they are prompted to enter a number between 1 and 6
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================

def main():
    global run
    global add

    while run == True:
        try:
            mode = 0
            mode = int(input('\nPlease select what function to test\n\n(1)'
                               ' Enter your Stock Symbol and Company Name.'
                               '\n\n(2) Enter company buy price and current price of corresponding stock.\n\n'
                               '(3) Enter the risk and shares of corresponding stock.\n\n'
                               '(4) Add a brand new stock.\n\n'
                               '(5) Find an existing stock.\n\n'
                               '(6) Exit (You will see a full list of all stock info)\n\n---------------------------------'
                               '-----------------------------------------\n:'))
            if mode == 1:
                add = True
                addName(name)
            if mode == 2:
                add = True
                addPrices(price)
            if mode == 3:
                add = True
                addExposure(exposure)
            if mode == 4:
                add = True
                addStock(name, price, exposure)
            if mode == 5:
                add = True
                findStock(name, price, exposure)
            if mode == 6:
                input('Exit\nPress enter to exit.')
                print ('\n--------------------------------------------------------------------------\n',
                       'Company Names: ', name, '\n',
                       'Companys BUY, CURRENT price : ', price, '\n',
                       'Companys RISK %, SHARES bought : ', exposure, '\n',
                       '--------------------------------------------------------------------------\n')
                      
                run = False
            else:
                print ('You Need To Enter A Number Between 1 and 5')

        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')
            
#========================================================  addName(name) Function  ==================================================================================
#define addName(name) as a function
    #call global variable 'add' and 'stockSym'
    #The while loop allows us to control how long to run the function with 'add' being our sentinel
        #establish a try catch method
            #get user input for the companys stock symbol using 'stockSym'
            #re.match checks for lower and upper case letters for 'stockSym'
                #if true then ask for users input for the companys name (else print an error and restart the function)
                #repeat re.match
                    #if true add comNam to the dictionary 'name' with 'stockSym' being the key
                    #set add = False which exits out of the loop
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================

def addName(name):
    global stockSym
    global add
    
    while add == True:
        try:
            print ('\n--------------------------------------------------------------------------\n')
            stockSym = input('Enter your companys stock symbol: ')
            if re.match("^[a-zA-Z\s]*$", stockSym):
                comName = input('Enter your companys name: ')
                print ('\n--------------------------------------------------------------------------\n')
                if re.match("^[a-zA-Z\s]*$", comName):
                    name[stockSym] = comName
                    add = False
                else:
                    print ("Error! Only letters a-z allowed!")
                    addName(name)
            else:
                print ("Error! Only letters a-z allowed!")
                addName(name)
        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')

#========================================================  addPrices(price) Function  ==================================================================================
#define addPrices(price) as a function
    #call global variable 'add' and 'stockSym'
    #create a list called 'p_list'
    #get user input for the companys stock symbol using 'stockSym'
    #re.match checks for lower and upper case letters for 'stockSym'
        #if true then ask for users input for the companys name (else print an error and restart the function)
            #The while loop allows us to control how long to run the function with 'add' being our sentinel
            #establish a try catch method
                #ask user to enter a float for company buy price
                #if the input is >= 0 then ask for the current price (else: print error, del p_list, restart function)
                    #if the input is >= 0 then append 'b_price' and 'c_price' to 'p_list' (else: print error, del p_list, restart function)
                    #add 'p_list' to the dictionary 'price' with the key being 'stockSym'
            #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
            #if triggered it prints out an error
#===========================================================================================================================================================

def addPrices(price):
    global stockSym
    global add

    p_list = []

    stockSym = input('Enter your companys stock symbol to add stock: ')
    if re.match("^[a-zA-Z\s]*$", stockSym):
        while add == True:
            try:
                print ('\n--------------------------------------------------------------------------\n')
                b_price = float(input('Enter a buy price for your companys stock: '))
                if b_price >= 0:
                    c_price = float(input('Enter current price for your companys stock: '))
                    print ('\n--------------------------------------------------------------------------\n')
                    if c_price >= 0:
                        p_list.append(format(b_price, '.2f'))
                        p_list.append(format(c_price, '.2f'))
                        price[stockSym] = p_list
                        price[stockSym] = p_list
                        add = False
                    else:
                        print ('Enter a Positive Integer')
                        del p_list[:]
                        addPrices(price)
                else:
                    print ('Enter a Positive Integer')
                    del p_list[:]
                    addPrices(price)
            except ValueError:
                print ('That is not a valid input')
            except UnboundLocalError:
                print ('That is not a valid input')
    else:
        print ("Error! Only letters a-z allowed!")
        addPrices(price)

#========================================================  addExposure(exposure) Function  ==================================================================================
#define addExposure(exposure) as a function
    #call global variable 'add' and 'stockSym'
    #create a list called 'e_list'
    #The while loop allows us to control how long to run the function with 'add' being our sentinel
        #establish a try catch method
            #ask user to enter a float for company risk percentage
            #if the input is >= 0 and <= 100 then risk /= 100 and ask user for shares (else: print error, del e_list, restart function)
                #if the input is >= 0 then append 'risk' and 'shares' to 'e_list' (else: print error, del e_list, restart function)
                #add 'e_list' to the dictionary 'price' with the key being 'stockSym'
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================

def addExposure(exposure):
    global stockSym
    global add
    
    e_list = []
    
    while add == True:
        try:
            print ('\n--------------------------------------------------------------------------\n')
            risk = float(input('Enter your risk percentage: '))
            if risk >= 0 and risk <= 100:
                risk /= 100
                shares = float(input('Enter the amount of shares you would like: '))
                print ('\n--------------------------------------------------------------------------\n')
                if shares >= 0:
                    e_list.append(format(risk, '.2f'))
                    e_list.append(format(shares, '.2f'))
                    exposure[stockSym] = e_list
                    add = False
                else:
                    print ('Enter a Positive Integer')
                    del e_list[:]
                    addExposure(exposure)
            else:
                print ('You need to enter a percentage between 0 and 100')
                del e_list[:]
                addExposure(exposure)
        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')

#========================================================  addStock(name, price, exposure) Function  ==================================================================================
#define addStock(name, price, exposure) as a function
    #call global variable 'add' and 'stockSym'
    #The while loop allows us to control how long to run the function with 'add' being our sentinel
        #establish a try catch method
            #execute addName(name)
            #set add = True to continue the loop
            #for 'stockSym' in the dict 'name'
                #if 'stockSym' is in the dict 'price' then proceed (else: execute addPrices(price) and addExposure(exposure)
                    #if 'stockSym' is in the dict 'exposure' then continue (else: execute addExposure(exposure), set add = True)
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================

def addStock(name, price, exposure):
    global stockSym
    global add
    
    while add == True:
        try:
            addName(name)
            add = True
            for stockSym in name:
                if stockSym in price:
                    if stockSym in exposure:
                       continue
                    else:
                        addExposure(exposure)
                        add = True
                else:
                    addPrices(price)
                    add = True
                    addExposure(exposure)
                    add = False
        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')

#========================================================  findStock(name, price, exposure) Function  ==================================================================================
#define findStock(name, price, exposure) as a function
    #call global variable 'add' and 'stockSym'
    #The while loop allows us to control how long to run the function with 'add' being our sentinel
        #establish a try catch method
            #print all stock companys
            #for 'stockSym' in the dict name locating keys
                #print 'stockSym'
            #for 'stockSym' in the dict price locating keys
                #if 'stockSym' is also in name
                    #continue with the function
                #else
                    #print 'stockSym'
            #get user input for the companys stock symbol using 'stockSym'
            #re.match checks for lower and upper case letters for 'stockSym'
                #if true then use .get() and get all items from all dictionaries (else print an error and restart the function)
                #ask user to press ENTER
                #set add = False and exit loop
        #the except statements are there to catch if an invalid integer is entered for the int(input() arguments
        #if triggered it prints out an error
#===========================================================================================================================================================

def findStock(name, price, exposure):
    global stockSym
    global add

    while add == True:
        try:
            print ('Here are all the stock companys so far:')
            for stockSym in name.keys():
                print (stockSym)
            for stockSym in price.keys():
                if stockSym in name:
                    continue
                else:
                    print (stockSym)
            stockSym = input('Enter the Stock Symbol of company to pull up the data: ')
            if re.match("^[a-zA-Z\s]*$", stockSym):
                print ('\n--------------------------------------------------------------------------\n')
                print ('Company Name: ', name.get(stockSym, 'Company Name Not Found'), '\n')
                print ('Companys BUY, CURRENT price : ',price.get(stockSym, 'Company Stock Costs Not Found'), '\n')
                print ('Companys RISK %, SHARES bought : ',exposure.get(stockSym, 'Company Exposure Not Found'), '\n')
                print ('--------------------------------------------------------------------------\n')
                input ('press ENTER to go to main menu')
                add = False
            else:
                print ("Error! Only letters a-z allowed!")
                findStock(name, price, exposure)
        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')


#executes the entire program    
main()

