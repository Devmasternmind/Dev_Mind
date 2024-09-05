# This ATM a real world basic project is created using "Classes and Objects" in Python which has some actions performed in this project like...||
# if you entered awrong num and card details it  will ask you to enter again and again valid name card details
# and also if you entered 3 times wrong pin it will block your card and no actions to be performed after blocking card.
#  This is just code performed  without voice. 
# 1).
# You can check your account details by pressing given option for chech card details.
# 2).
# You can check your current Balance.
# 3).
# You can deposite Balance to your account.
# 4).
# You can withdraw Blance. and some other acations has performed in this section.
# 5).
# you can Change your pin.

import time
import datetime
import random
import sys
class ATM:
     print("""
          -------------------------------------------
          |                                         |
          | *** Welcom To Allied Bank Services ***  |
          |                                         |
          -------------------------------------------
          """)     
     # Account info
     # -----------------------------------
     account_holder = "shahzaib hassan"
     account_num = 1245
     pin = 1234
     current_balance = 50000
     # ----------------------------------
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
            self.receipt = input("Do you Want slip for curent balance: (yes or no) = ")
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
          while True:
           print("\nPlease Wait: ")
           time.sleep(1)
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
           self.input_option = "cancel"
           self.amount = int(input("Enter amount  for withdraw: "))
           if self.amount > self.current_balance:
               time.sleep(2)
               print("insufficient amount! try again your amount is high please enter low amount")
               time.sleep(2)
               self.amount = int(input("\nEnter amount  for withdraw: "))
               if self.amount > self.current_balance:
                time.sleep(2)
                print("insufficient amount! try again your amount is high please enter low amount")
                self.exit = input("Do you want to exit this transaction? Press Cancel Button = ")
                if self.exit == self.input_option:
                     time.sleep(4)
                     print("please take your card back")
                     sys.exit()
           elif self.amount < self.current_balance:
                self.amount = int(input("Enter amount  for withdraw: "))
           self.receipt = input("Do you Want slip for Withdraw balance: (yes or no) = ")
           if self.receipt == "yes":
             print("\nPlease wait while your transaction is being processed..............")
             time.sleep(4)
             print("\nPlease Take your Card Back.")
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
                print("\nPlease wait while your transaction is being processed...........")
                time.sleep(2)
                print("\nPlease Take your Card Back.")  
                self.current_balance = self.current_balance - self.amount
                print("\nTransaction is Successful. ")
                print(f"Current Balnace is: {self.current_balance}") 
           
          # another transaction
          # while True:
           self.another_transaction = input("\nDo you Want another transactoin? (yes or no) = ")
           if self.another_transaction == "yes":
                 self.amount = int(input("\nEnter Amount for another transaction: "))
               #   if self.amount > self.current_balance:
               #      break    
               #   else:
               #      print("insufficient amount! try again your amount is high please enter low amount")    
                 self.receipt = input("\nDo you Want slip for Withdraw balance: (yes or no) = ")
                 if self.receipt == "yes":
                  print("\nPlease wait while your transaction is being processed............")
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
                  print("\nPlease wait while your transaction is being processed...............")
                  time.sleep(4)    
                  print("PLease Take Your Card Back")
                  self.current_balance = self.current_balance - self.amount
                  print(f"Current Balnace is: {self.current_balance}") 
                  print("\nTransaction is Successful. ")         
           else:
            self.another_transaction == "no"
            print("Take Your Card Back: Thanks for using Allied Bank Services")
            sys.exit()  
                       
     def change_pin(self):
          print("\nPlease Wait: ")
          time.sleep(3)
          print("""
           |---------------------------------------|
           |               Change PIN              |
           |---------------------------------------| 
               """)  
          self.input_old_pin = int(input("\nEnter Your Old Pin: "))
          if self.input_old_pin == self.pin:
            time.sleep(4)
            print("\n***Please enter your new PIN***:")    
            self.new_pin = int(input("\nEnter your new pin: "))
            self.confirm_new_pin = int(input("\nplease enter your new pin to confirm: "))
            if self.confirm_new_pin == self.new_pin:
               time.sleep(3)
               print("Conratulation! your New Pin has been updated:")
            else:
                 self.confirm_new_pin != self.new_pin
                 time.sleep(3)
                 print("invalid pin! Pin not matched please try again.")  
          else:
               sys.exit()
# ------------------------------------------------------------------------------------------------------------ 
# Method for enter and match account holder name     
     def __init__(self):
          while True:  
           self.input_user_name = input("Enter Account Holder Name: ") 
           time.sleep(2)       
           if self.input_user_name == self.account_holder:
                break
           else:
                print("Invalid Name! Try Again")   
#  --------------------------------------------------------------------------------------------------------------
#  Method for insert card and match account holder num            
     def insert_card_num(self):
          while True:     
           self.input_user_num = int(input("\nInsert Your Card Here: "))
           time.sleep(3)
           if self.input_user_num == self.account_num:
                break
           else:
            print("Invalid Account Num! Try Again")
#  ----------------------------------------------------------------------------------------------------------- 
# Method for enter pin and match pin and also block card after three attempts                         
     def enter_pin(self): 
          self.min_i = 1
          self.max_i = 4
          while self.min_i < self.max_i:
           self.input_user_pin = int(input("\nEnter Your 4 digit Pin: "))
           if self.input_user_pin == self.pin:
                time.sleep(3)
                print( """
          _____________________________________________________________________________________ 
         |-------------------------------------------------------------------------------------|   
         |                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
         |    |==============================|            |=============================|      |
         |    |  1.    Account Detail        |            |  2.    Check Balance        |      | 
         |    |==============================|            |=============================|      |
         |                                                                                     | 
         |                                                                                     |
         |    |==============================|            |=============================|      |
         |    |  3.    Depisite Balance      |            |  4.   Withdraw Balance      |      |
         |    |==============================|            |=============================|      |
         |                                                                                     |
         |                                                                                     |        
         |    |==============================|            |=============================|      |
         |    |  5.      Change PIN          |            |  6.        Exit             |      |
         |    |==============================|            |=============================|      |
         |                                                                                     |  
         |_____________________________________________________________________________________|
         |-------------------------------------------------------------------------------------|
          """) 
                return True
           else:
                self.min_i = self.min_i + 1
                if self.min_i < self.max_i:
                    time.sleep(3)
                    print("Invalid pin please try again")
                    print(f"you have {self.max_i - self.min_i} tries are left")
                    
          print("invalid pin! Your card has been blocked due to enter 3 times invalid Pin.")
          time.sleep(3)
          print("\nPlease Take your Card back.")
          sys.exit()   
# ------------------------------------------------------------------------------------------------------------------
# Method to perform atm transaction and other actions                      
     def trans(self): 
           while True:
               try:
                   self.option = int(input("\nSelect a number to proceed: "))
               except:
                    print("Error! Kindly Select number between: 1, 2, 3, 4, 5 only")
                       
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
                         my_atm.change_pin()      
                    elif self.option == 6:
                         print("\nThanks for Choosing Allied Bank Services. Have a Great Day!")
                         sys.exit()                            
# ----------------------------------------------------------------------------------------------------------               
my_atm = ATM()
my_atm.insert_card_num()
my_atm.enter_pin()
my_atm.trans()
              
