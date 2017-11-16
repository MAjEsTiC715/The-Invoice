class CompanyStocks:

    def __init__(self, stockSym, comName, bPrice, cPrice, risk, shares, expectSale):
        self.__stockSym = stockSym
        self.__comName = comName
        self.__bPrice = bPrice
        self.__cPrice = cPrice
        self.__risk = risk
        self.__shares = shares
        self.__expectSale = expectSale


    def set_stockSym(self, stockSym):
        self.__stockSym = stockSym


    def set_comName(self, comName):
        self.__comName = comName


    def set_bPrice(self, bPrice):
        self.__bPrice = bPrice


    def set_cPrice(self, cPrice):
        self.__cPrice = cPrice


    def set_risk(self, risk):
        self.__risk = risk


    def set_shares(self, shares):
        self.__shares = shares


    def set_expectSale(self, expectSale):
        self.__expectSale = expectSale


    def get_stockSym(self):
        return self.stockSym


    def get_comName(self):
        return self.comName


    def get_bPrice(self):
        return self.bPrice


    def get_cPrice(self):
        return self.cPrice


    def get_risk(self):
        return self.risk


    def get_shares(self):
        return self.shares


    def get_expectSale(self):
        return self.expectSale


    def __str__(self):
        return "\n--------------------------------------------------------------------------\n" + \
               "Company Symbol: " + self.__stockSym + "\n" + \
               "Company Names: " + self.__comName + "\n" + \
               "Companys BUY; " + format(self.__bPrice, '.2f') + "\n" + \
               "CURRENT price : " + format(self.__cPrice, '.2f') + "\n" + \
               "Companys RISK %: " + format(self.__risk, '.2f') + "\n" + \
               "SHARES bought : " + format(self.__shares, '.2f') + "\n" + \
               "Expected Sales Value: " + format(self.expectSale, '.2f') + "\n" + \
               "--------------------------------------------------------------------------\n"









