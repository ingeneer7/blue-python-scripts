#Imports the random and string modules
import random
import string

#Generates the random characters and numbers as a unique name
def string_generator(size=12, string=string.ascii_letters + string.digits):    
    return ''.join(random.choice(string) for _ in range(size))
    
#Enables team members to input the department name as a unique name
department = input("What is the name of your department? Enter Here: ")

#List the department choices team members have
for _ in department:

    if department == "Marketing" or department.lower() == "marketing" :
        print("Department Verified ✔")
        break

    elif department == "Accounting" or department.lower() == "accounting" :
        print("Department Verified ✔")
        break

    elif department == "FinOps" or department.lower() == "finops" :
        print("Department Verified ✔")
        break

    else:
        print("⚠ Warning! ⚠ The department you have entered does not match in the system. Please try again.")
        exit()  

#The number of EC2 instances that team members can input
number = int(input("How many EC2 instances are needed? Enter the number: ")) 

if number < 0:    
    print("Enter a valid number: ") 
elif number > 0:    
    print("One Moment please....")

#Generates and prints the unique EC2 names at random
print("Results loading ██████████████]")

for _ in range(1, number + 1):    
    unique_name = department    
    EC2_unique_name = unique_name + "-" + string_generator()
    print("Your EC2 Instance's unique name is : ", EC2_unique_name)
