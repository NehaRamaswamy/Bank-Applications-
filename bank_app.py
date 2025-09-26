#create a class
class Swiss_Bank:
    IFSC = 'swiss2025'
    Branch_code = 1
    Location = 'Bangalore'

    #creation of constructor using __init__(self) (self is mandatory args)
    def __init__(self,name,acc_no,mob_no,bal,pin):
        self.name = name
        self.acc_no = acc_no
        self.mob_no = mob_no
        self.bal = bal
        self.pin = pin
        
    # Create a method to display the details of the users and it is the object method
    def Details(self):
        print(f'Name : {self.name} \nAccount Num : {self.acc_no} \nMobile No : {self.mob_no}')

    # Create an other method for checking the balance it is also one object method 
    def Check_Bal(self):
        count = 3
        while count != 0:
            print(f'Numbers of attempts are {count}')
            if self.Take_Password() == self.pin:
                print(f'Available Balance is {self.bal}')
                print('Transcation Successful')
                break
            else:
                print("Invalid pin")
                count -= 1
        else:
            print('Try after 24 hours')

    # Create a method for the Deposit in the bank and it is one object method
    def Deposite(self):
        count = 3
        while count != 0:
            print(f'Numbers of attempts are {count}')
            if self.Take_Password() == self.pin:
                money = int(input('Enter the amount to deposite: '))
                if 100 <= money <= 40000:
                    if money % 100 == 0:
                        self.bal += money
                        print('Money added successfully')
                        print('Transcation done')
                        break
                    else:
                        print('Check the denominations')
                else:
                    print("Invalid amount")
            else:
                print('Invalid Pin')
                count -= 1
        else:
            print('Try after 24 hours')

    # Create a method for the withdraw amount from the bank and it is one object method 
    def Withdrawn(self):
        count = 3
        while count != 0:
            print(f'The number of attempts are {count}')
            if self.Take_Password() == self.pin:
                money = int(input('Enter the amount to withdraw: '))
                if money <= self.bal:
                    if 100 <= money <= 20000:
                        if money % 100 == 0:
                            self.bal -= money
                            print('Amount debited Successfully')
                            print('Transcation done')
                            break
                        else:
                            print('Check the denominations')
                    else:
                        print('Invalid Amount')
                else:
                    print('In-sufficient')
            else:
                print('Invalid pin')
                count -= 1
        else:
            print('Try after 24 hours')

    # Create a method for accessing the class variables here we access the location and change that location 
    # and it is one class method for that reason declare one decorator '@classmethod' cls is mandatory args
    @classmethod
    def Change_Loc(cls):
        cls.Location = 'USA'

    # Create a method for generate the password and use those password at the time of transcations 
    # Static method is used for create method and decorator also used '@static method' no args needed
    @staticmethod
    def Take_Password():
        password = int(input('Enter the 4 - digits pin : '))
        return password

# create the object for class , The object can be create any number
customer1 = Swiss_Bank('Asha',200034560001,9876543211,1209000,1111)
customer2 = Swiss_Bank('Daivamsh',200034560002,9889762134,203000,2222)
customer3 = Swiss_Bank('Raj',200034560003,8979680321,3021000,3333)

# Accessing the class method, Object method using the objects which are created above and static method cannot be access here 
print('Details')
customer1.Details()
print('Deposite')
customer1.Deposite()
print('Check Bal')
customer1.Check_Bal()
print('Withdraw')
customer1.Withdrawn()
print('Change Location')
customer1.Change_Loc()
print('Details')
customer1.Details()

print('------------------')

print('Details')
customer2.Details()
print('Deposite')
customer2.Deposite()
print('Check Bal')
customer2.Check_Bal()
print('Withdraw')
customer2.Withdrawn()
print('Change Location')
customer2.Change_Loc()
print('Details')
customer2.Details()

print('------------------')

print('Details')
customer3.Details()
print('Deposite')
customer3.Deposite()
print('Check Bal')
customer3.Check_Bal()
print('Withdraw')
customer3.Withdrawn()
print('Change Location')
customer3.Change_Loc()
print('Details')
customer3.Details()