#ATM withdrawal process
choice = 1
accountBalance = int(input("Enter the Account Balance"))
while choice == 1:
     withdrawalBalance = int(input("Enter the Withdrawal Amount"))

     if accountBalance < withdrawalBalance :
         print("Insufficient Balance")
     elif withdrawalBalance % 10 != 0 :
         print("Amount Must be a multiple of 10")
     else:
           remainingBalance = accountBalance - withdrawalBalance
           print("Transaction Successfull \n Remaining Account Balance is ", remainingBalance)
           accountBalance = remainingBalance
           choice = int(input("Do you Want to continue \n 1. Yes    2. No"))
else:
  print("Thankyou Visit Again...")