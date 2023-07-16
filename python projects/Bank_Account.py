'''
    creating a New Account
    Account Holders Details
    Wthdraw Amount
    Deposit Amount
    Balance Inquiry
'''

print("------Welcome to our 'Idel Bank'------")

print("|Creating a New Account    -- press 1|")
print("|Account Holder Details    -- press 2|")
print("|Withdraw Amount           -- press 3|")
print("|Deposit Amount            -- press 4|")
print("|Balance Inquiry           -- press 5|")
print("|Quit/Exit                 -- press 6|")

print("--------------------------------------")

#Global Variable Declaration.....

'''
a=1
b=2
c=3
d=4
e=5
f=6
'''
while True:
    
        try:
            identity=list(input(" \n Create Your Pincode :"))
            long=len(identity)
            
            if long == 4:
                print(" \n      Pin code seted ...")
                break 
            
            else:
                print(" \n      ** !!'ERROE!!' Not Set **")   
        except:
            continue 


first= input(" \n Enter Your Request : ")
first1=first.lower()
first2=['creating a new account','account holder details','withdraw amount','deposit amount','balance inquiry','quit','exit']
#Creating a New User Account-----

def new_account():
    '''
    global uname
    global age
    global ph
    global address
    global pin
    global d1
    global acc1'''
    
    uname=input(" \n Enter Your Name : ") 
    
    print("\n      Hii",uname,"Welcome to Our Bank")
    
    while True:
        try:
            age=int(input("\n Enter Your Age :"))
            if age >= 18:
                print(" \n      ** You'r Eligible.. **",age)
                break
            
            else:
                
                print("\n      You'r Not Eligible For Creating a Account")
                print("\n      Try to Create a Joint Account or Student Account")
                new_account()
                
        except:
            continue
        
    
    while True:
        try:
            ph=list(input(" \n Enter Your Phone Number :"))
            length=len(ph)
            
            if length==10:
                print(" \n      phone Number seted")
                break
                
            else:
                print("\n     ** please Enter a Valid Number !! 'ERROR' **")
                print("\n     **like ! 10 digit Number !! **")
    
        except:
            continue         
    
    address=input(" \n Enter Your Valid Address :")

    while True:
    
        try:
            pin=list(input(" \n Enter Your Pincode :"))
            length1=len(pin)
            
            if length1 == 6:
                print(" \n      Pin code seted ...")
                break 
            
            else:
                print(" \n      ** !!'ERROE!!' Make a Correct code **")   
        except:
            continue 
            
    while True:
        try:
          
            dist=input(" \n Enter Your Distict name :")
            d1= dist.lower()
            d2=["ariyalur","chengalpattu","chennai","coimbatore","cuddalore","dharmapuri","dindigul","erode","kallakurichi","kancheepuram","karur",
                "krishnagiri","madurai","mayiladuthurai","nagapattinam","kanniyakumari","namakkal","perambalur","pudukottai","ramanathapuram","ranipet",
                "salem","sivagangai","tenkasi","thanjavur","theni","thiruvallur","thiruvarur","thoothukudi","trichirappalli","thirunelveli","tirupathur",
                "tiruppur","tiruvannamalai","nilgirisUdagamandalam","vellore","viluppuram",
                "virudhunagar"]
                
            if d1 in d2:
                print(" \n      Distict Setup Successfully ",dist)
                break
            else:
                print(" \n     **Something Wrong Plese Check Your Spling..!! **")
                
        except:
            continue
                
    while True:
        
        try:
        
            Account=input(" \n Enter Your Account Type :")
            acc1=Account.lower()
            acc2=["selfaccount","jointaccount","studentaccount"]
            
            if acc1 in acc2:
                print(" \n      Your Account Created Succesfully..")
                break
            else:
                print(" \n !!    ** ERROE'!! Something Wrong **",Account)
                print(" \n       |  Select One Account  |    ")
                print(" \n       |  Type selfaccount    |  or")
                print(" \n       |  Type jointaccount   |  or")
                print(" \n       |  Type studentaccount |    ")
        except:
            continue
            

def account_holder():

    uname = input(" \n Enter Your Name :")
    age = int(input(" \n Enter Your Age :"))
    ph  = int(input(" \n Enter Your ph Number :"))
    while True:
    
        try:
         
            acc_no = list(input(" \n Enter Your Account Number :"))
            length2=len(acc_no)
            
            if length2 == 16:
                print(" \n      Account Number Confirmed ...")
                break 
            
            else:
                print(" \n      ** !!'ERROE!!' Make a 16 digit code **")   
        except:
            continue 
    
            
    print(f" \n Account Holder Details                  ")
    print(f" -------------------------------------------")
    print(f"  \n Your Name           :{uname}           ")
    print(f"  \n Your Age            :{age}             ")
    print(f"  \n Your Phone Number   :{ph}              ")
    print(f"  \n Your Account Number :{acc_no}          ")
    print(f"--------------------------------------------")
    

def withdraw():
    
    while True:
        
        try:
            wpin=list(input("Enter Your pin : "))
            if wpin == identity:
                print(" \n      Pin Identified ...")
                break 
            
            else:
                print(" \n      ** !!'ERROE!!' Please Check Your Pin **")   
        except:
            continue 
    
    while True:
        
        try: 
            acc_no1 = list(input(" \n Enter Your Account Number :"))
            length4=len(acc_no1)
            
            if length4 == 16:
                print(" \n      Account Number Confirmed ...")
                break 
            
            else:
                print(" \n      ** !!'ERROE!!' Make a 16 digit code **")   
        except:
            continue 
            
    wamount=input("\n Enter Your Withdraval Amount : ")

    print(" \n    Your Amount Transfered Successfully ...")
        
    
def deposit():

    while True:
    
        try:
            dpin=list(input("Enter Your pin : "))
            
            if dpin == identity:
                print(" \n      Pin Identified ...")
                break 
            
            else:
                print(" \n      ** !!'ERROE!!' Please Check Your Pin **")   
        except:
            continue 
            
    name=input(" \n Enter Your Name : ")

    while True:
        
        try: 
            acc_no2 = list(input(" \n Enter Your Account Number :"))
            length5=len(acc_no2)
            
            if length5 == 16:
                print(" \n      Account Number Confirmed ...")
                break 
            
            else:
                print(" \n      ** !!'ERROE!!' Make a 16 digit code **")   
        except:
            continue 
    
    ammount=int(input(" \n Enter Your Deposit Amount : ")) 
    
    print(" \n    Ammount Deposit Succesfully...")

def balance_inquiry():

    while True:
        
        try:
            wpin=list(input("Enter Your pin : "))
            if wpin == identity:
                print(" \n      Pin Identified ...")
                break 
            
            else:
                print(" \n      ** !!'ERROE!!' Please Check Your Pin **")   
        except:
            continue
        

    a=int(input(" \n Enter Your Deposited Amount : "))

    b=int(input(" \n Enter Your Withdraval  Amount : "))

    print("\n  Your Blance Amount : ",a-b)


if first1 =='creating a new account' or first=='1':
    print(" \n   Create a Account ...")
    new_account()
elif first1 =='account holder details'  or first == '2':   
    print(" \n   Check Your Details ...")
    account_holder()
elif first1 == 'withdraw amount' or first == '3':   
    print(" \n   Withdraw Your Ammount ...")
    withdraw()
elif first1 == 'deposit amount' or first == '4':   
    print(" \n   Deposit Your Ammount ...")
    deposit()
elif first1 == 'balance inquiry' or first == '5':   
    print(" \n balance_inquiry   ...")
    balance_inquiry()
elif first1 == 'quit' or first1 == 'exit' or first == '6':   
    print(" \n Exit   ...")
    while True:
        try:
            break
        except:
            continue
            new_account()
    
else:
    print("!! ERROR Page Not Available.. !!")
    
    
