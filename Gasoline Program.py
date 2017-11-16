#DOCUMENTATION*********************************************************************************************
#Your receipt should show the following information:                                                      *

#Display the station name and location                                                                    *
#Date of the receipt is being issued/given
#Type of Gas
#Number of Gallons of Gas (a number that is displayed to three decimal places)
#Cost per gallon (this should be a number that is formatted as US currency)
#Total Cost (this should be a number that is formatted as US currency)
#Your receipt program must:

#Use at least three literals.
#Use at least three variables.
#The number of gallons, cost per gallon, and total cost should all be displayed on one line.
#Use the str.format() method to format all of your output.
#Display all required information in a way that is well organized and easy to read.
#Be sure to use comments for both structure of the program and documentation of the code.
#************************************************************************************************
print ("""  /$$$$$$                                /$$ /$$                           /$$$$$$$                                                               
 /$$__  $$                              | $$|__/                          | $$__  $$                                                              
| $$  \__/  /$$$$$$   /$$$$$$$  /$$$$$$ | $$ /$$ /$$$$$$$   /$$$$$$       | $$  \ $$ /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$/$$$$ 
| $$ /$$$$ |____  $$ /$$_____/ /$$__  $$| $$| $$| $$__  $$ /$$__  $$      | $$$$$$$//$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$|____  $$| $$_  $$_  $$
| $$|_  $$  /$$$$$$$|  $$$$$$ | $$  \ $$| $$| $$| $$  \ $$| $$$$$$$$      | $$____/| $$  \__/| $$  \ $$| $$  \ $$| $$  \__/ /$$$$$$$| $$ \ $$ \ $$
| $$  \ $$ /$$__  $$ \____  $$| $$  | $$| $$| $$| $$  | $$| $$_____/      | $$     | $$      | $$  | $$| $$  | $$| $$      /$$__  $$| $$ | $$ | $$
|  $$$$$$/|  $$$$$$$ /$$$$$$$/|  $$$$$$/| $$| $$| $$  | $$|  $$$$$$$      | $$     | $$      |  $$$$$$/|  $$$$$$$| $$     |  $$$$$$$| $$ | $$ | $$
 \______/  \_______/|_______/  \______/ |__/|__/|__/  |__/ \_______/      |__/     |__/       \______/  \____  $$|__/      \_______/|__/ |__/ |__/
                                                                                                        /$$  \ $$                                 
                                                                                                       |  $$$$$$/                                 
                                                                                                        \______/

************************************************************************************************************************************************************""")
import sys #To stop code execution in Python you import the sys object. After this you can then call the exit() method to stop the program running

#Right here we will begin the input process of the program

month = input("What is the month: ") #this input statement asks the user what the month is
day = int(input("What is the day: ")) #this input statement asks the user what the day is
year = int(input("What is the year: ")) #this input statement asks the user what the year is
station_Name = input("What is the name of the gas station: ") #this input statement asks the user what the gas station name is
station_Location = input("Where is it located: ") #this input statement asks the user where the location of the gas station is
gas_Type = input("Is is premium, non-premium, or diesel: ") #this input statement asks the user what type of gas the user wants based on these 3 choices
number_Gallons = float(input("How many gallons are you getting: ")) #this input statement asks the user how many gallons he is getting
cost_Per_Gallon= float(input("What is the cost per gallon: ")) #this input statement asks the user what the price per gallon is

#After all the information was inputed we then move to the calculation process
#this if statment asks if the input for day is <=0 or >31 ; if so then the program is stopped and prints that an invalid day was entered
if (day <= 0 or day > 31):
    print ("Sorry you have entered an invalid day, thank you")
    sys.exit('number was equal or less than 0')
# this elif will proceed if the previous if statement was false
# this elif again asks if the input for year is <=0 or >9999 : if so then the program is stopped and prints that an invalid year was entered
elif (year <= 0 or year > 9999):
    print ("Sorry you have entered an invalid year, thank you")
    sys.exit('number was equal or less than 0')
# this last elif statement asks if number_Gallons and cost_Per_Gallon >= 0 ; if so then we continue with the program and print the information provided
# if not then we move to the else statement to which then the program is stopped and prints that an invalid number of gallons or price per gallon was entered
elif (number_Gallons and cost_Per_Gallon >= 0):
    total_Price = float(number_Gallons * cost_Per_Gallon)

#We have finished the calculation process, from here depending if the previous elif was true. we now output the information that we have provided
    
    print ("")
    print ("############################################################################")
    print ("")
    # I use Pythons string.format method in order to take integers and floats that have been
    # stored in the code and prints it as a string with either no decimal points or 2 decimal points
    # the {} in the "" can indicate what you want, here i useed "{:.0f}
    #f meaning float and :.0 meaning no decimals
    print ("Todays date is " + month + " {:.0f}".format(day) + ", {:.0f}".format(year))
    print ("Gas station: " + station_Name)
    print ("Location: " + station_Location)
    print ("You chose " + gas_Type + " as your primary gas type")
    # here below i use {:.2f}.format() to indicate what variable I want to convert into a float with 2 decimal places
    print ("{:.3f}".format(number_Gallons) + " gallons of gas for ${:.2f}".format(cost_Per_Gallon) + ", that comes out to a total of: ${:.2f}".format(total_Price))
    print ("")
    print ("##############################################################################")
    print ("")
    print ("Thank you, come again")
else:
    print ("Sorry you have entered an invalid number within your number of gallons or price per gallon, thank you")
    sys.exit('number was equal or less than 0')

#this else statement only is active when the previous elif statement is proven false ; this uses a sys.exit which closes the program because of the error.
    

