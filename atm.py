class atm(object):
    def __init__(self, pin, cardNum):
        self.pin = pin
        self.cardNum = cardNum

    def cashWithdrawl(self):
        print("CashWithdrawl succesful")

    def balanceEquiry(self):
        print("You haveas much as you want in your bank account")

    def depositMoney(self):
        print("Deposit succesful")
    
    def accountActivity(self):
        print("The recipt shows your account activity for the past 24 hours")
