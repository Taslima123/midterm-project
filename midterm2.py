print("Welcome to the Prudent Healthcare Hospital")
print("Lets start with registration process")

users = {}
status = ""

if status != "q":
    status = input("Are you a registered user? y/n?  ")

    if status == "n": #create new login
         createLogin = input("Create login name: ")

         if createLogin in users: # check if login name exist in the dictionary
             print ("Login name already exist!\n")
         else:
             createPassw = input("Create password: ")
             users[createLogin] = createPassw # add login and password      rough.py:17
             print("\nUser created!\n")

    elif status == "y": #login the user
        login = input("Enter login name with surename: ")

        if login in users:
           passw = input("Enter password: ")


           if login in users and passw in users: # login matches password

                print ("Login successful!\n")

        else:

            print("User match")
            print("continue with appointment")
#This is appointment taking process.
print("Take an Appointment")
print("List of Specialists")
print("1. Doctor A")
print("2. Doctor B")
print("3. Doctor C")
print("4. Doctor D")
# This is for Doctor A
select_doctor = input("Choose your doctor")
if select_doctor == "1":
        print("Doctor A \n a. 10AM-11AM \n b.12AM-1PM \n c. 2PM-3PM")
        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 10AM-11:30AM")
        elif your_time == "b":
            print("b. 12AM-1:30PM")
        elif your_time == "c":
            print("c. 2PM-3:30PM")
        else:
            print("Not available")
#This is for Doctor B
elif select_doctor == "2":
        print("Doctor B \n a. 10:30AM-11:30AM\n b. 12:30PM-1:30PM \n c. 2:30PM-3:30PM")
        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 10:30AM-11:30AM")
        elif your_time == "b":
            print("b. 12:30PM-1:30PM")
        elif your_time == "c":
            print("c. 2:30PM-3:30PM")
        else:
            print("Not available")
#This is for Doctor C
elif select_doctor == "3":
        print("Doctor C \n a. 11AM-12AM \n b. 1PM-2PM \nc. 3PM-4:30PM")
        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 11AM-12AM")
        elif your_time == "b":
            print("b. 1PM-2PM")
        elif your_time == "c":
            print("c. 3PM-4:30PM")
        else:
            print("Not available")
#This is for Doctor D
elif select_doctor == "4":
        print("Doctor D \n a. 1:30PM-2:30AM \n b. 3:30PM-4:30PM \n c. 4:30PM-5:30PM")
        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 1:30PM-2:30AM")
        elif your_time == "b":
            print("b. 3:30PM-4:30PM")
        elif your_time == "c":
            print("c. 2:30PM-3:30PM")
        else:
            print("Not available")
else:
    print("Doctor not available")

#This is for patient information recording in bill and Hospital's database
print(" patient's details in bill")
detail=input("Enter your name")
print(detail)
address=input("Enter your address")
print("address")
age=input("Enter your age")
print("age")
gender=input("Enter your gender ")
print("Gender")
disease=input("Enter your disease ")
print("disease")
contact=input("Enter your contact number")
print("contact ")
doctor=input("Enter the name of the doctor you had choosed")
print("doctor")
print("THANK YOU!!!")

#This is for payment process
print("For cash Enter C")
print("For credit Enter L")
payment = input("finish the payment")
if payment=="C":
    print("payment done by cash")
    recebill = input("Please enter the receipt for the bill:-")
    print(recebill)
    print("Thank you")

elif payment=="L":
     print("payment done by credit")
     crebill = input("Please enter the credit card number")
     print(crebill)
     print("Thank you")
else:
    print("not paid and go for payment")
    print("Thank You")

#For Exit
print("Loged Out")