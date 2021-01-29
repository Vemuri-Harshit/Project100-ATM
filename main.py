
class Atm:
    def __init__(self, user, password, deposit_money):
        self.user = user
        self.password = password
        self.deposit_money = deposit_money
        # self.withdraw_money = withdraw_money

    def createAccount(self): 
        print("Hello " + self.user + " Thank you for Loggin In with the password " + self.password + " With Depositing " + self.deposit_money)

    def take_money(self, withdraw_money):
        self.withdraw_money = withdraw_money

        if self.deposit_money > self.withdraw_money :
            print("Hello, You have Withdrawed " + self.withdraw_money + " Now, you have " + str(int(self.deposit_money) - int(self.withdraw_money)) + " Left in your Account")  
            self.deposit_money = str(int(self.deposit_money) - int(self.withdraw_money)) 

        else: 
            print("You Are Withdrawing More than What is in your Account")

    def deposit_more_money(self, more_deposited_money):
        self.more_deposited_money = more_deposited_money

        self.deposit_money = str(int(self.deposit_money) + int(self.more_deposited_money)) 

        print("You Deposited " + self.more_deposited_money )

        print("Now You Have " + self.deposit_money + " In Your Account")


    def money_in_account(self):
        print("You have " + self.deposit_money +  " In Your Account")




harshit = Atm("Harshit", "Harshit123", "50000")

harshit.createAccount()
harshit.take_money("30000")
harshit.money_in_account()
harshit.deposit_more_money("70000")
harshit.money_in_account()