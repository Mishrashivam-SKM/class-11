#PROJECT CLASS 11

import random
x=1
y=2
amount=0.0

'Personal details'

#NAME details :-
full_name = input("Enter Your Full name.")
father_guardian_husband_name = input("Enter your father/guardian/huband name.")
mother_name = input("Enter your mother name.")

#residential address:-
residential_address = input("Enter your residential address")
landmark_address = input("Enter your near by landmark")
village_city_address = input("Enter your village/city name.")
district_city_address = input("Enter your district name.")
state_address = input("Enter your your state name.")
pincode_address = input("Enter your pincode.")
concatinated_address = "" #baadme dekhenge

#number:-
telephone_number = input("Ener your telephone number") #later on convert it into string by checking its type
contact_number= input("Enter your contact number")

#PD:- MAM SE PUCHNA HAI!
sex = {'a':'male' , 'b':'female' , 'c':'other'}
for i in sex:
    print(i ,'=', sex[i])

sex_user = input("Enter your choice.") 
if sex_user in sex :
    print(sex[sex_user])
else :
    print("Wrong input") #back ka option ya yahi pe loop

date_of_birth = input("Enter your date of birth in DD/MM/YYYY form (Enter with slashes)")

occupation = {'a':'Govt / PSB' , 'b':'Private' , 'c': 'Buisness' , 'd': ' Self employed' , 'e': ' Student' , 'f':'Labourer' , 'g':'Unemployed' ,}
for i in occupation:
    print(i,'=',occupation[i])

occupation_user=input("Enter your choice.")
if occupation_user in occupation:
    print(occupation[occupation_user])
else:
    print("Wrong input")

category_user=input("Enter your category")










'AAPKA ACCOUMT OPEN KARRE HAI'
print("Types of accounts :-")
print("Current & Savings")
input_of_account= input('Enter "current" for opening Current Account & ENTER "Savings" for opening savings account')


if input_of_account.lower()=="current":
    print("We have two categories:-")
    print('Enter 1. for " Zero balance" & 2. for "Quarterly balance "')
    current_input= int(input("Enter your choice"))
    if current_input==x :
        print("Zero balance acc")
    elif current_input==y:
        
        print("Quarterly balance account")
    else:
        print("Wrong input")

elif input_of_account.lower()=="savings":
    print("We have two categories:-")
    print('Enter 1. for " Zero balance" & 2. for "Quarterly balance "')
    savings_input= int(input("Enter your choice"))
    if savings_input==x:
        print("Zero balance acc")
    elif savings_input==y:
        
        print("Quarterly balance account")
    else:
        print("Wrong input")

if (input_of_account.lower()=="current" and current_input==x) or (input_of_account.lower()=="savings" and savings_input==x) :
        
    answer=input("Do you want to deposit ?Enter 'yes' to continue and 'no' to quit")
    if answer.lower()=='yes':
    
   
        amount_input_zero = float(input("Enter the amount u want to deposit."))
        amount = amount + amount_input_zero
        


    elif answer.lower() == 'no':
        print("Thank you")

    else:
        print("Error")

elif (input_of_account.lower()=="current" and current_input==y) or (input_of_account.lower()=="savings" and savings_input==y):
    print("You need to deposit minimum balance of 2,500.00 rupees for setting up your account Or your the created account will be fined/deleted T&C apply. ")
    amount_input_quaterly = float(input("ENTER THE AMOUNT YOU WOULD LIKE TO DEPOSIT."))
    if amount_input_quaterly >= 2500 :
        amount = amount + amount_input_quaterly
    else:
        print("You are fined 500 rupees")
        amount = amount-500
        
else :
    print("Wrong input")



#Account number
j = random.randint(123456789,999999999)
print(j)


#ATM Pin
ans2 = input("Do you want to generate atm card? Enter 'yes' and 'no' to quit")
while(True):
    if ans2.lower()=='yes':
        ATM_Pin = input("Enter your ATM Pin of 4 digits")
        if len(ATM_Pin)== 4:
        
            b = input("Re-enter your pin")
            if ATM_Pin == b:
                print("Your account number is :", j)
                print("Your pin is ", b)
                break
            else:
                print("wrong pin")
                continue


print("Name of the account holder :" , full_name)
print("Address:" , residential_address )
print("Phone number :" , contact_number)
print("D.O.B. :" , date_of_birth)
print("Your account number: " , j)
print("Account balance:" , amount)

