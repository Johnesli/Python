'''
    creating a New Account
    Account Holders Details
    Wthdraw Amount
    Deposit Amount
    Balance Inquiry
'''

print("------Welcome to our 'Idel Bank'------")

print("|Creting a New Account     -- press 1|")
print("|Account Holder Details    -- press 2|")
print("|Withdraw Amount           -- press 3|")
print("|Deposit Amount            -- press 4|")
print("|Balance Inquiry           -- press 5|")
print("|Quit/Exit                 -- press 6|")

print("--------------------------------------")

#Global Variable Declaration.....

a=1
b=2
c=3
d=4
e=5
f=6

#Creating a New User Account-----

def new_account():
    uname=input("Enter Your Name : ") 
    print("\n Hii",uname,"Welcome to Our Bank")
    
    age=int(input("\n Enter Your Age :"))
    if age <= 18:
        print(" \n You'r Not Eligible For Creating a Account")
        print("\n Try to Create a Joint Account or Student Account")
        
    else:
        print(" \n You'r Eligible..",age)
    
    ph=int(input(" \n Enter Your Phone Number :"))
    if ph==10:
        print(" \n phone Number seted")

    else:
        print(" \n Enter a Valid Number :")
        print("\n like ! 10 digit Number")
    
    address=input(" \n Enter Your Valit Address :")

    while True:
        try:
            pin=int(input(" \n Enter Your Pincode"))
            if pin >= :
                print(" \n  Pin code seted ...")
                break
            else:
                print(" \n Make a Correct code")
        except:
            continue
        
    Account=input(" \n Enter Your Account Type :")
    acc1=selfaccount
    acc2=joinaccount
    acc3=studentaccount
    
    acc1=Account.lower()                                   #Converting Account Into Lower case
    acc2=Account.lower()
    acc3=Account.lower()
    
    if Account == acc1 or Account == acc2 or Account == acc3:
        print(" \n Enter a Valid Account Type..")
 
            

    dist=input(" \n Enter Your Distict name :")

    print(" \n Your Account Created Succesfully ")

new_account()

    


        
    
       
        
        
        
    
        
    
    
    
new_account()    
    
