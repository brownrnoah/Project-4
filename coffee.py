"""
Noah Brown
CS 1410-602
March, 14th 2020
Project 4 CoffeeMachine
"""

#Coffee Machine class, houses the commands and initializes the cashbox and selector classes.
class CoffeeMachine():
    def __init__(self):
        self.cashBox = CashBox()
        self.selector = Selector(self.cashBox)

    def oneAction(self):
        while(True):
            print("\tPRODUCT LIST: all 35 cents, except bouillon (25 cents)")
            print("\t1 = black, 2 = white, 3 = sweet, 4 = white & sweet, 5 = bouillon")
            print("\t\tSample commands: insert 25, select 1.")
            command = input(">>> Your Command: ").lower().split()

            if command[0] == "insert":
                #call cashBox and let it do all the work
                self.cashBox.deposit(int(command[1]))
            elif command[0] == "select":
                #call selector and let it do all the work
                self.selector.select(int(command[1]))
            elif command[0] == "cancel":
                #return any money already deposited
                self.cashBox.returnCoins()
            elif command[0] == "quit":
                #return any money already deposited
                if self.cashBox.credit > 0:
                    self.cashBox.returnCoins()
                break
            else:
                #Error, invalid command, priint message for user
                print("Invalid command")


    def totalCash(self):
        #output total cash
        print("Total cash: $" + '{:.2f}'.format(self.cashBox.totalReceived))

#Cashbox class that keeps track of credit and total received totals, allows for deposits, returning coins, removing cash, and checking if you have enough cash for a purchase.
class CashBox():
    def __init__(self):
        self.credit = 0
        self.totalReceived = 0.0

    def deposit(self, amount):
        if amount != 5 and amount != 10 and amount != 25 and amount != 50:
            print("INPUT ERROR >>>")
            print("We only take half-dollars, quarters, dimes, and nickels.")
            self.returnCoins()
            print()
        else:
            self.credit += amount
            print("Depositing " + str(amount) + " cents. You have " + str(self.credit) + " cents credit.")
            print()

    def returnCoins(self):
        print("Returning " + str(self.credit) + " cents.")
        self.credit = 0
        print()

    def haveYou(self, amount):
        if self.credit >= amount:
            return True
        else:
            return False

    def deduct(self, amount):
        self.credit -= amount
        self.totalReceived += (amount * .01)
        if self.credit > 0:
            self.returnCoins()
        else:
            print()
        
    def total(self):
        return self.credit

#The selector class that makes the product set, and has the functionality to select those products.
class Selector():
    def __init__(self, cashBox):
        self.cashBox = cashBox
        self.products = []
        self.SetProducts()

    def SetProducts(self):
        self.products.append(Product("Black", 35, "\tDispensing Cup\n\tDispensing Coffee\n\tDispensing Water"))
        self.products.append(Product("White", 35, "\tDispensing Cup\n\tDispensing Coffee\n\tDispensing Cream\n\tDispensing Water"))
        self.products.append(Product("Sweet", 35, "\tDispensing Cup\n\tDispensing Coffee\n\tDispensing Sugar\n\tDispensing Water"))
        self.products.append(Product("White & Sweet", 35, "\tDispensing Cup\n\tDispensing Coffee\n\tDispensing Cream\n\tDispensing Sugar\n\tDispensing Water"))
        self.products.append(Product("Bouillon", 25, "\tDispensing Cup\n\tDispensing Coffee\n\tDispensing Cream\n\tDispensing Water"))

    def select(self, index):
        if self.cashBox.haveYou(self.products[index -1].getPrice()) == False:
            print("Sorry. Not enough money deposited.")
            print()
        else:
            self.products[index -1].make()
            self.cashBox.deduct(self.products[index - 1].getPrice())

#Product class that gets product prices, and makes them.
class Product():
    def __init__(self, name, price, recipe):
        self.name = name
        self.price = price
        self.recipe = recipe

    def getPrice(self):
        return self.price

    def make(self):
        print("making " + self.name + ":")
        print(self.recipe)

#Initiating the coffee machine object and running it.
def main():
    cm = CoffeeMachine()
    cm.oneAction()
    cm.totalCash()

if __name__ == "__main__":
    main()