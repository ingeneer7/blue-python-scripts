#Variables in Strings
firstname = "India"
surname = "Rogers"

print(f"My first name is {firstname}. My family name is {surname}")

#Number Variables in strings
my_int = 77
sentence = "The total comes to: "

print(sentence + str(my_int))

#Creating, Reading, Updating and Deleting values in Dictionaries

#Create Dictionaries
user = {"first_name":"Natalee"}
print(user)

#Read Dictionaries
user = {"first_name":"Natalee"}
print(user["first_name"])

#Update Dictionaires

#Add a key-value
user["family_name"] = "McCain"
print(user)

#Modify a value
user["family_name"] = "Rogers"
print(user)

#Delete a Key-Value Pair
del user["family_name"]
print(user)

#Creating, Reading, Updating and Deleting elements in a list
