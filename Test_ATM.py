import time
import datetime
import random
import sys
class ATM:
     print("""
          -------------------------------------------
          |                                         |
          | *** Welcom To Allied Bank Seervices *** |
          |                                         |
          -------------------------------------------
          """)
     account_holder = "shahzaib hassan"
     account_num = 1245
     account_pin = 1234
     Cvv =789
     expiry = 12122024
     current_balance = 50000
# ------------------------------------------------------------------------------------------------------------
     def account_detail(self):
       print("\nPlease Wait: ")
       time.sleep(3)   
       print("""
           |---------------------------------------|
           |            Account Detail             |
           |---------------------------------------|      
           """) 
       print(f"The Detail of Account is:\n{self.account_holder.title()}")
       print(f"Account number: {self.account_num}")
       print(f"Available Current Balance: {self.current_balance}")  
     def check_balance(self):
            print("\nPlease Wait: ")
            time.sleep(3)
            print("""
           |---------------------------------------|
           |            Check Balance              |
           |---------------------------------------|        
           """)
            print(f"Current Balance is: {self.current_balance}")
            self.receipt = input("Do you Want slip for curent balance: (yes/no) = ")
            if self.receipt == "yes":
                 print("Please Wait!")
                 time.sleep(4)
                 print(f"""
                      printing recipt
          **************************************
                       Allied Bank
                                                    
               Transaction number: {random.randint(1,1000)}            
                 {datetime.datetime.now()} 
                 
               Balance Inquiry::
               Account number: {self.account_num}                      
               Available Balance: {self.current_balance}    
                                                                      
                    Thank You for Usig
                     Allied Bank ATM                              
          **************************************         
                      """)
            else:
                 self.receipt == "no"
                 print("Pleas Wait! ")
                 time.sleep(4)
                 print(f"Current Balance is: {self.current_balance}")
                 print()
     def deposite(self):
          print("\nPlease Wait: ")
          time.sleep(3)
          print("""
           |---------------------------------------|
           |           Deposite Balance            |
           |---------------------------------------|        
           """)
          self.amount = int(input("Enter Amout To Deposite: "))
          self.current_balance = self.current_balance + self.amount
          print("Please Wait! Your amount is submitting into your account: ")
          time.sleep(5)
          print("\nAmount Sucessfuly added to your account: ")
          print(f"Current Balance is: {self.current_balance}")
          print()
     def withdraw(self):
          print("\nPlease Wait: ")
          time.sleep(3)
          print("""
           |---------------------------------------|
           |               Withdraw                |
           |---------------------------------------| 
               """)
          print("""
             |----------------------------------|
             |                                  |
             | 500          1000          2000  |     
             |                                  |
             | 50000        10000         15000 |
             |                                  |
             | 20000        25000         50000 |
             |                                  |
             |          Another Amount          |
             |----------------------------------|
               """)
          self.amount = int(input("Enter amount  for withdraw: "))
          self.receipt = input("Do you Want slip for Withdraw balance: (yes/no) = ")
          if self.receipt == "yes":
               print("\nPlease wait while your transaction is being processed.")
               time.sleep(4)
               print(f"""
                      Printing Reciept
          **************************************
                       Allied Bank 
                       
                 {datetime.datetime.now()} 
               Transaction is Sucessful.                            
               Transaction number: {random.randint(1,1000)}            
               Account Holder: {self.account_holder.title()}           
               Account number: {self.account_num}
               Transaction Amount PKR: {self.amount}                      
               Available Balance: Nu.{"********"}                              
                                                                  
                    Thank You for Usig
                     Allied Bank ATM                               
          **************************************         
                      """)
          else:
               self.receipt == "no"
               print("\nPlease wait while your transaction is being processed.")
               time.sleep(4)    
          self.current_balance = self.current_balance - self.amount
          print("\nTransaction is Successful. ")
          print(f"Current Balnace is: {self.current_balance}")                               
# ------------------------------------------------------------------------------------------------------------     
     def __init__(self):
          while True:
           self.input_user_name = input("Enter Account Holder Name: ")
           time.sleep(3)
           if self.input_user_name != self.account_holder:
                print("Invalid Name! Try Again")   
           else:      
                 self.input_user_num = int(input("\nInsert Your Card Here: "))
                 time.sleep(3)
                 if self.input_user_num != self.account_num:
                    print("Invalid Account Num! Try Again")
                 else:
                     self.input_user_pin = int(input("\nEnter Your PIN: "))
                     time.sleep(3)
                     if self.input_user_pin == self.account_pin:
                          print("""
                 Menu    
        ------------------------
        |                      |
        |   1. Account Detail  | 
        |   2. Check Balance   |
        |   3. Deposit         |
        |   4. Withdraw        |
        |   5. Exit            |
        |                      |
        ------------------------
           """)
                          break
                     else:
                       print("Invalid Pin! Try Again")                
     def trans(self): 
           while True:
               try:
                    self.option = int(input("\nSelect a number to proceed: "))
               except:
                    print("Error! Kindly Select number between: 1, 2, 3, 4, 5 only ")
               else:
                    if self.option == 1:
                         my_atm.account_detail()
                    elif self.option == 2:
                         my_atm.check_balance()   
                    elif self.option == 3:
                         my_atm.deposite() 
                    elif self.option == 4:
                         my_atm.withdraw() 
                    elif self.option == 5:
                         print("\nThanks for Choosing Allied Bank Services. Have a Great Day!")
                         sys.exit()                            
# ----------------------------------------------------------------------------------------------------------               
my_atm = ATM()
my_atm.trans()
              
          
     

    
    