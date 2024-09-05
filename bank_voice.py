# This ATM a real world basic project is created using "Classes and Objects" in Python which has some actions performed in this project like...||
# if you entered awrong num and card details it  will ask you to enter again and again valid name card details
# and also if you entered 3 times wrong pin it will block your card and no actions to be performed after blocking card.
#  All Actions will be performed over Text to speech in this project.
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
import pyttsx3
class ATM:
     print("""
          -------------------------------------------
          |                                         |
          | *** Welcom To Allied Bank Services ***  |
          |                                         |
          -------------------------------------------
          """)
     text = "Welcom To Allied Bank Services"
     engine = pyttsx3.init()
     Voices = engine.getProperty("voices")
     engine.setProperty("voice", Voices[1].id)
     rate = engine.getProperty("rate")
     engine.setProperty("rate", 175)
     Volume = engine.getProperty("volume")
     engine.setProperty("volume", 1)
     engine.say(text)
     engine.runAndWait()
     
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
       self.text = "Please Wait"
       self.engine = pyttsx3.init()
       self.Voices = self.engine.getProperty("voices")
       self.engine.setProperty("voice", self.Voices[1].id)
       self.rate = self.engine.getProperty("rate")
       self.engine.setProperty("rate", 170)
       self.engine.say(self.text)
       self.engine.runAndWait() 
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
            self.text = "Please Wait"
            self.engine = pyttsx3.init()
            self.Voices = self.engine.getProperty("voices")
            self.engine.setProperty("voice", self.Voices[1].id)
            self.rate = self.engine.getProperty("rate")
            self.engine.setProperty("rate", 170)
            self.engine.say(self.text)
            self.engine.runAndWait() 
            time.sleep(3)
            print("""
           |---------------------------------------|
           |            Check Balance              |
           |---------------------------------------|        
           """)
            print(f"Current Balance is: {self.current_balance}")
            self.text = "Do you Want slip for curent balance: (yes or no)"
            self.engine = pyttsx3.init()
            self.Voices = self.engine.getProperty("voices")
            self.engine.setProperty("voice", self.Voices[1].id)
            self.rate = self.engine.getProperty("rate")
            self.engine.setProperty("rate", 170)
            self.engine.say(self.text)
            self.engine.runAndWait() 
            self.receipt = input("Do you Want slip for curent balance: (yes or no) = ")
            if self.receipt == "yes":  
               print("Please Wait!")
               self.text = "Please Wait"
               self.engine = pyttsx3.init()
               self.Voices = self.engine.getProperty("voices")
               self.engine.setProperty("voice", self.Voices[1].id)
               self.rate = self.engine.getProperty("rate")
               self.engine.setProperty("rate", 170)
               self.engine.say(self.text)
               self.engine.runAndWait() 
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
                 self.text = "Please Wait"
                 self.engine = pyttsx3.init()
                 self.Voices = self.engine.getProperty("voices")
                 self.engine.setProperty("voice", self.Voices[1].id)
                 self.rate = self.engine.getProperty("rate")
                 self.engine.setProperty("rate", 170)
                 self.engine.say(self.text)
                 self.engine.runAndWait() 
                 time.sleep(4)
                 print(f"Current Balance is: {self.current_balance}")
                 print()
                 
     def deposite(self):
          print("\nPlease Wait: ")
          self.text = "Please Wait"
          self.engine = pyttsx3.init()
          self.Voices = self.engine.getProperty("voices")
          self.engine.setProperty("voice", self.Voices[1].id)
          self.rate = self.engine.getProperty("rate")
          self.engine.setProperty("rate", 170)
          self.engine.say(self.text)
          self.engine.runAndWait() 
          time.sleep(3)
          print("""
           |---------------------------------------|
           |           Deposite Balance            |
           |---------------------------------------|        
           """)
          self.text = "Enter Amount to Deposite"
          self.Voices = self.engine.getProperty("voices")
          self.engine = pyttsx3.init()
          self.engine.setProperty("voice", self.Voices[1].id)
          self.rate = self.engine.getProperty("rate")
          self.engine.setProperty("rate", 170)
          self.engine.say(self.text)
          self.engine.runAndWait() 
          self.amount = int(input("Enter Amout To Deposite: "))
          self.current_balance = self.current_balance + self.amount
          print("Please Wait! Your amount is submitting into your account: ")
          self.text = "Please Wait! Your amount is submitting into your account"
          self.engine = pyttsx3.init()
          self.Voices = self.engine.getProperty("voices")
          self.engine.setProperty("voice", self.Voices[1].id)
          self.rate = self.engine.getProperty("rate")
          self.engine.setProperty("rate", 170)
          self.engine.say(self.text)
          self.engine.runAndWait() 
          time.sleep(5)
          print("\nAmount Sucessfuly added to your account: ")
          self.text = "Amount Sucessfuly added to your account"
          self.engine = pyttsx3.init()
          self.Voices = self.engine.getProperty("voices")
          self.engine.setProperty("voice", self.Voices[1].id)
          self.rate = self.engine.getProperty("rate")
          self.engine.setProperty("rate", 170)
          self.engine.say(self.text)
          self.engine.runAndWait() 
          print(f"Current Balance is: {self.current_balance}")
          print()
          
     def withdraw(self):
          print("\nPlease Wait: ")
          self.text = "Please Wait"
          self.engine = pyttsx3.init()
          self.Voices = self.engine.getProperty("voices")
          self.engine.setProperty("voice", self.Voices[1].id)
          self.rate = self.engine.getProperty("rate")
          self.engine.setProperty("rate", 170)
          self.engine.say(self.text)
          self.engine.runAndWait() 
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
          self.text = "Enter Amount for Withdraw"
          self.engine = pyttsx3.init()
          self.Voices = self.engine.getProperty("voices")
          self.engine.setProperty("voice", self.Voices[1].id)
          self.rate = self.engine.getProperty("rate")
          self.engine.setProperty("rate", 170)
          self.engine.say(self.text)
          self.engine.runAndWait() 
          self.amount = int(input("Enter amount  for withdraw: "))
          while True:
           if self.amount > self.current_balance:
                break
           else:
               print("Incorrect Amount! please try again Amount is high enter low amount: ")
               self.text = "Incorrect Amount! please try again Amount is high enter low amount"
               self.engine = pyttsx3.init()
               self.Voices = self.engine.getProperty("voices")
               self.engine.setProperty("voice", self.Voices[1].id)
               self.rate = self.engine.getProperty("rate")
               self.engine.setProperty("rate", 170)
               self.engine.say(self.text)
               self.engine.runAndWait() 
     
           self.text = "Do you Want slip for Withdraw balance: (yes or no)"
           self.engine = pyttsx3.init()
           self.Voices = self.engine.getProperty("voices")
           self.engine.setProperty("voice", self.Voices[1].id)
           self.rate = self.engine.getProperty("rate")
           self.engine.setProperty("rate", 170)
           self.engine.say(self.text)
           self.engine.runAndWait() 
           self.receipt = input("Do you Want slip for Withdraw balance: (yes or no) = ")
           if self.receipt == "yes":
               print("\nPlease wait while your transaction is being processed..............")
               self.text = "Please wait while your transaction is being processed............"
               self.engine = pyttsx3.init()
               self.Voices = self.engine.getProperty("voices")
               self.engine.setProperty("voice", self.Voices[1].id)
               self.rate = self.engine.getProperty("rate")
               self.engine.setProperty("rate", 170)
               self.engine.say(self.text)
               self.engine.runAndWait() 
               time.sleep(4)
               print("\nPlease Take your Card Back.")
               self.text = "Please Take Your Card Back"
               self.engine = pyttsx3.init()
               self.Voices = self.engine.getProperty("voices")
               self.engine.setProperty("voice", self.Voices[1].id)
               self.rate = self.engine.getProperty("rate")
               self.engine.setProperty("rate", 170)
               self.engine.say(self.text)
               self.engine.runAndWait() 
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
               self.text = "Please wait while your transaction is being processed........"
               self.engine = pyttsx3.init()
               self.Voices = self.engine.getProperty("voices")
               self.engine.setProperty("voice", self.Voices[1].id)
               self.rate = self.engine.getProperty("rate")
               self.engine.setProperty("rate", 170)
               self.engine.say(self.text)
               self.engine.runAndWait()
               time.sleep(2)
               print("\nPlease Take your Card Back.")
               self.text = "Please Take Your Card Back"
               self.engine = pyttsx3.init()
               self.Voices = self.engine.getProperty("voices")
               self.engine.setProperty("voice", self.Voices[1].id)
               self.rate = self.engine.getProperty("rate")
               self.engine.setProperty("rate", 170)
               self.engine.say(self.text)
               self.engine.runAndWait() 
               time.sleep(4)    
           self.current_balance = self.current_balance - self.amount
           print("\nTransaction is Successful. ")
           self.text = "Transaction is Sucessful"
           self.engine = pyttsx3.init()
           self.Voices = self.engine.getProperty("voices")
           self.engine.setProperty("voice", self.Voices[1].id)
           self.rate = self.engine.getProperty("rate")
           self.engine.setProperty("rate", 170)
           self.engine.say(self.text)
           self.engine.runAndWait() 
           print(f"Current Balnace is: {self.current_balance}") 
           
          # another transaction
           self.text = "Do you Want another transactoin? (yes or no)"
           self.engine = pyttsx3.init()
           self.Voices = self.engine.getProperty("voices")
           self.engine.setProperty("voice", self.Voices[1].id)
           self.rate = self.engine.getProperty("rate")
           self.engine.setProperty("rate", 170)
           self.engine.say(self.text)
           self.engine.runAndWait()
           self.another_transaction = input("\nDo you Want another transactoin? (yes or no) = ")
           if self.another_transaction == "yes":
               self.text = "Enter Amount for another transaction"
               self.engine = pyttsx3.init()
               self.Voices = self.engine.getProperty("voices")
               self.engine.setProperty("voice", self.Voices[1].id)
               self.rate = self.engine.getProperty("rate")
               self.engine.setProperty("rate", 170)
               self.engine.say(self.text)
               self.engine.runAndWait()
               self.amount = int(input("\nEnter Amount for another transaction: "))
               self.text = "Do you Want slip for Withdraw balance: (yes or no)"
               self.engine = pyttsx3.init()
               self.Voices = self.engine.getProperty("voices")
               self.engine.setProperty("voice", self.Voices[1].id)
               self.rate = self.engine.getProperty("rate")
               self.engine.setProperty("rate", 170)
               self.engine.say(self.text)
               self.engine.runAndWait()
               self.receipt = input("\nDo you Want slip for Withdraw balance: (yes or no) = ")
               if self.receipt == "yes":
                print("\nPlease wait while your transaction is being processed............")
                self.text = "Please wait while your transaction is being processed"
                self.engine = pyttsx3.init()
                self.Voices = self.engine.getProperty("voices")
                self.engine.setProperty("voice", self.Voices[1].id)
                self.rate = self.engine.getProperty("rate")
                self.engine.setProperty("rate", 170)
                self.engine.say(self.text)
                self.engine.runAndWait()
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
                self.text = "Please wait while your transaction is being processed"
                self.engine = pyttsx3.init()
                self.Voices = self.engine.getProperty("voices")
                self.engine.setProperty("voice", self.Voices[1].id)
                self.rate = self.engine.getProperty("rate")
                self.engine.setProperty("rate", 170)
                self.engine.say(self.text)
                self.engine.runAndWait()
                time.sleep(4)    
                print("PLease Take Your Card Back")
                self.text = "Please Take Your Card Back"
                self.engine = pyttsx3.init()
                self.Voices = self.engine.getProperty("voices")
                self.engine.setProperty("voice", self.Voices[1].id)
                self.rate = self.engine.getProperty("rate")
                self.engine.setProperty("rate", 170)
                self.engine.say(self.text)
                self.engine.runAndWait()
                self.current_balance = self.current_balance - self.amount
                print(f"Current Balnace is: {self.current_balance}") 
                print("\nTransaction is Successful. ")
                self.text = "Transaction is Successful."
                self.engine = pyttsx3.init()
                self.Voices = self.engine.getProperty("voices")
                self.engine.setProperty("voice", self.Voices[1].id)
                self.rate = self.engine.getProperty("rate")
                self.engine.setProperty("rate", 170)
                self.engine.say(self.text)
                self.engine.runAndWait()          
           else:
             self.another_transaction == "no"
             print("Take Your Card Back: Thanks for using Allied Bank Services")
             self.text = "Take Your Card Back: Thanks for using Allied Bank Services"
             self.engine = pyttsx3.init()
             self.Voices = self.engine.getProperty("voices")
             self.engine.setProperty("voice", self.Voices[1].id)
             self.rate = self.engine.getProperty("rate")
             self.engine.setProperty("rate", 170)
             self.engine.say(self.text)
             self.engine.runAndWait()
             sys.exit()  
                       
     def change_pin(self):
          print("\nPlease Wait: ")
          self.text = "Please Wait"
          self.engine = pyttsx3.init()
          self.Voices = self.engine.getProperty("voices")
          self.engine.setProperty("voice", self.Voices[1].id)
          self.rate = self.engine.getProperty("rate")
          self.engine.setProperty("rate", 170)
          self.engine.say(self.text)
          self.engine.runAndWait()
          time.sleep(3)
          print("""
           |---------------------------------------|
           |               Change PIN              |
           |---------------------------------------| 
               """)
          self.text = "Enter your old Pin"
          self.engine = pyttsx3.init()
          self.Voices = self.engine.getProperty("voices")
          self.engine.setProperty("voice", self.Voices[1].id)
          self.rate = self.engine.getProperty("rate")
          self.engine.setProperty("rate", 170)
          self.engine.say(self.text)
          self.engine.runAndWait()  
          self.input_old_pin = int(input("\nEnter Your Old Pin: "))
          if self.input_old_pin == self.pin:
            time.sleep(4)
            print("\n***Please enter your new PIN***:") 
            self.text = "Please enter your new pin"
            self.engine = pyttsx3.init()
            self.Voices = self.engine.getProperty("voices")
            self.engine.setProperty("voice", self.Voices[1].id)
            self.rate = self.engine.getProperty("rate")
            self.engine.setProperty("rate", 170)
            self.engine.say(self.text)
            self.engine.runAndWait()    
            self.new_pin = int(input("\nEnter your new pin: "))
            self.text = "Please enter your new pin to confirm"
            self.engine = pyttsx3.init()
            self.Voices = self.engine.getProperty("voices")
            self.engine.setProperty("voice", self.Voices[1].id)
            self.rate = self.engine.getProperty("rate")
            self.engine.setProperty("rate", 170)
            self.engine.say(self.text)
            self.engine.runAndWait()
            self.confirm_new_pin = int(input("\nplease enter your new pin to confirm: "))
            if self.confirm_new_pin == self.new_pin:
               time.sleep(3)
               print("Conratulation! your New Pin has been updated:")
               self.text = "congratulation your new pin has been updated"
               self.engine = pyttsx3.init()
               self.Voices = self.engine.getProperty("voices")
               self.engine.setProperty("voice", self.Voices[1].id)
               self.rate = self.engine.getProperty("rate")
               self.engine.setProperty("rate", 170)
               self.engine.say(self.text)
               self.engine.runAndWait()
            else:
                 self.confirm_new_pin != self.new_pin
                 time.sleep(3)
                 print("invalid pin! Pin not matched please try again.")
                 self.text = "invalid pin! Pin not matched please try again"
                 self.engine = pyttsx3.init()
                 self.Voices = self.engine.getProperty("voices")
                 self.engine.setProperty("voice", self.Voices[1].id)
                 self.rate = self.engine.getProperty("rate")
                 self.engine.setProperty("rate", 170)
                 self.engine.say(self.text)
                 self.engine.runAndWait()   
          else:
               sys.exit()
# ------------------------------------------------------------------------------------------------------------ 
# Method for enter and match account holder name     
     def __init__(self):
          while True:
           self.text = "Enter Account Holder Name"   
           self.engine = pyttsx3.init()
           self.Voices = self.engine.getProperty("voices")
           self.engine.setProperty("voice", self.Voices[1].id)
           self.rate = self.engine.getProperty("rate")
           self.engine.setProperty("rate", 170)
           self.engine.say(self.text)
           self.engine.runAndWait()   
           self.input_user_name = input("Enter Account Holder Name: ")        
           if self.input_user_name == self.account_holder:
                break
           else:
                print("Invalid Name! Try Again")
                self.text = "Invalid Name! Try Again"
                self.engine = pyttsx3.init()
                self.Voices = self.engine.getProperty("voices")
                self.engine.setProperty("voice", self.Voices[1].id)
                self.rate = self.engine.getProperty("rate")
                self.engine.setProperty("rate", 170)
                self.engine.say(self.text)
                self.engine.runAndWait()    
#  --------------------------------------------------------------------------------------------------------------
#  Method for insert card and match account holder num            
     def insert_card_num(self):
          while True:
           self.text = "Insert Your Card Here"
           self.engine = pyttsx3.init()
           self.Voices = self.engine.getProperty("voices")
           self.engine.setProperty("voice", self.Voices[1].id)
           self.rate = self.engine.getProperty("rate")
           self.engine.setProperty("rate", 170)
           self.engine.say(self.text)
           self.engine.runAndWait()      
           self.input_user_num = int(input("\nInsert Your Card Here: "))
           time.sleep(3)
           if self.input_user_num == self.account_num:
                break
           else:
            print("Invalid Account Num! Try Again")
            self.text = "Invalid Account Number Try Again"
            self.engine = pyttsx3.init()
            self.Voices = self.engine.getProperty("voices")
            self.engine.setProperty("voice", self.Voices[1].id)
            self.rate = self.engine.getProperty("rate")
            self.engine.setProperty("rate", 170)
            self.engine.say(self.text)
            self.engine.runAndWait() 
#  ----------------------------------------------------------------------------------------------------------- 
# Method for enter pin and match pin and also block card after three attempts                         
     def enter_pin(self): 
          self.min_i = 1
          self.max_i = 4
          while self.min_i < self.max_i:
           self.text = "Enter your 4 digit Pin"
           self.engine = pyttsx3.init()
           self.Voices = self.engine.getProperty("voices")
           self.engine.setProperty("voice", self.Voices[1].id)
           self.rate = self.engine.getProperty("rate")
           self.engine.setProperty("rate", 170)
           self.engine.say(self.text)
           self.engine.runAndWait() 
           self.input_user_pin = int(input("\nEnter Your 4 digit Pin: "))
           if self.input_user_pin == self.pin:
                time.sleep(3)
                print("""
                 Menu    
        ------------------------
        |                      |
        |   1. Account Detail  | 
        |   2. Check Balance   |
        |   3. Deposit         |
        |   4. Withdraw        |
        |   5. Change Pin      | 
        |   6. Exit            |
        |                      |
        ------------------------
           """) 
                return True
           else:
                self.min_i = self.min_i +1
                if self.min_i < self.max_i:
                    print(f"Invalid pin please try again")
                    self.text = "Invalid pin please Try Again"
                    self.engine = pyttsx3.init()
                    self.Voices = self.engine.getProperty("voices")
                    self.engine.setProperty("voice", self.Voices[1].id)
                    self.rate = self.engine.getProperty("rate")
                    self.engine.setProperty("rate", 170)
                    self.engine.say(self.text)
                    self.engine.runAndWait() 
                    print(f"you have {self.max_i - self.min_i} tries are left")
          print("invalid pin! Your card has been blocked due to enter 3 times invalid Pin please take your card back.")
          time.sleep(3)
          self.text = "invalid pin! Your card has been blocked due to enter 3 times invalid Pin please take your card back"
          self.engine = pyttsx3.init()
          self.Voices = self.engine.getProperty("voices")
          self.engine.setProperty("voice", self.Voices[1].id)
          self.rate = self.engine.getProperty("rate")
          self.engine.setProperty("rate", 170)
          self.engine.say(self.text)
          self.engine.runAndWait() 
          sys.exit()
# ------------------------------------------------------------------------------------------------------------------
# Method to perform atm transaction and other actions                      
     def trans(self): 
           while True:
               try:
                   self.text = "Please Select a number to proceed"
                   self.engine = pyttsx3.init()
                   self.Voices = self.engine.getProperty("voices")
                   self.engine.setProperty("voice", self.Voices[1].id)
                   self.rate = self.engine.getProperty("rate")
                   self.engine.setProperty("rate", 170)
                   self.engine.say(self.text)
                   self.engine.runAndWait() 
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
                         self.text = "Thanks for Choosing Allied Bank Services. Have a Great Day"
                         self.engine = pyttsx3.init()
                         self.Voices = self.engine.getProperty("voices")
                         self.engine.setProperty("voice", self.Voices[1].id)
                         self.rate = self.engine.getProperty("rate")
                         self.engine.setProperty("rate", 170)
                         self.engine.say(self.text)
                         self.engine.runAndWait() 
                         sys.exit()                            
# ----------------------------------------------------------------------------------------------------------               
my_atm = ATM()
my_atm.insert_card_num()
my_atm.enter_pin()
my_atm.trans()
              
