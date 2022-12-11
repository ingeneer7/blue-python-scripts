#Imports the random and string modules
import random
import string

#Generates the random characters and numbers as a unique name
def string_generator(size=12, string=string.ascii_letters + string.digits):    
    return ''.join(random.choice(string) for str in range(size))
    
#Enables team members to input the department name as a unique name
team_department = input("What is the name of your department? Enter Here: ")

#List the department choices team members have
for str in team_department:

    if team_department == "Marketing" or team_department.lower() == "marketing" :
        print("Department Verified ✔")
        break

    elif team_department == "Accounting" or team_department.lower() == "accounting" :
        print("Department Verified ✔")
        break

    elif team_department == "FinOps" or team_department.lower() == "finops" :
        print("Department Verified ✔")
        break

    else:
        print("⚠ Warning! ⚠ The department you have entered does not match in the system. Please try again.")
        exit()  

#The number of EC2 instances that team members can input
ec2_amount = int(input("How many EC2 instances are needed? Enter the number: ")) 

if ec2_amount < 0:    
    print("You must enter a valid number")
    exit()
    
elif ec2_amount > 0:    
    print("One Moment please....")

#Generates and prints the unique EC2 names at random
print("Results loading ██████████████]")

for str in range(1, ec2_amount + 1):    
    instance_name = team_department    
    EC2_random_name = instance_name + "-" + string_generator()
    print("Your EC2 name has been generated : ", EC2_random_name)
