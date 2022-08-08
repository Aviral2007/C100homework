class ATM(object):
    def __init__(self,bank,cashMethod,withdrawl):
        self.bank = bank
        self.cashMethod = cashMethod
        self.withdrawl = withdrawl
    
    def start(self):
        print("Enter Pin")
    
    def stop(self):
        print("Amount Given")
    
    def accelerating(self):
        print("Bzzzzzzzz...")
    
    def change_gear(self, gear_type):
        print("pin entered ")

Account = ATM("SBI","green","ATM",250)
print(Account.start())
print(Account.change_gear())
print(Account.accelerating())
print(Account.stop())
