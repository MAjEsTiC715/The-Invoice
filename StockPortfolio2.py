import re
import CompanyStocks

add = True
run = True

FILENAME = 'companyStocks.dat'

def main():
    global run
    global add

    mystocks = load_stocks()

    while run == True:
        try:
            mode = 0
            mode = int(input('\nPlease select what function to test\n\n(1)'
                               ' Add Stock.'
                               '\n\n(2) Find Stock.\n\n'
                               '(3) Exit\n\n---------------------------------'
                               '-----------------------------------------\n:'))
            
            if mode == 1:
                addStock(mystocks)
            if mode == 2:
                findStock(mystocks)
            if mode == 3:
                input('Exit\nPress enter to exit.')
                run = False
            else:
                print ('You Need To Enter A Number Between 1 and 5')

        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')


def load_stocks():
    try:
        input_file = open(FILENAME, 'rb')
        stocks_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        stocks_dct = {}

    return stocks_dct


def addStock(mystocks):
    stockSym = input('Enter your companys stock symbol: ')
    comName = input('Enter your companys name: ')
    bPrice = float(input('Enter a buy price for your companys stock: '))
    cPrice = float(input('Enter current price for your companys stock: '))
    risk = float(input('Enter your risk percentage: '))
    shares = float(input('Enter the amount of shares you would like: '))

    expectSale = ((cPrice - bPrice) - risk * cPrice) * shares

    entry = CompanyStocks.CompanyStocks(stockSym, comName, bPrice, cPrice, risk, shares, expectSale)


    if stockSym not in mystocks:
        mystocks[stockSym] = entry
        print ('The entry has been added.')
    else:
        print ('That Stock Symbol already exists')

def findStock(mystocks):

    stockSym = input('Enter the Stock Symbol of company to pull up the data: ')

    print (mystocks.get(stockSym, 'That stock is not found'))

def GetSale(mystocks, stockSym, cPrice, bPrice, risk, shares, expectSale):
    current = mystocks.get(stockSym, cPrice)
    buy = mystocks.get(stockSym, bPrice)
    riskPercent = mystocks.get(stockSym, risk)
    share = mystocks.get(stockSym, shares)

    expectSale = ((current - buy) - riskPercent * current) * share
    return expectSale
main()
