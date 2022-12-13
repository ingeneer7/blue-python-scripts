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

#Create Lists
fruit = ["strawberries","grapes","watermelon"]

#Create empty list by assigning [] to a variable
fruit = []

#Create empty list by using the list() constructor
fruit = list()

#Read Lists
fruit = ["strawberries","grapes","watermelon"]
print(fruit[1])

#Find the length of a list
len(fruit)

#Return the last value in a list using a negative index value
print(fruit[-1])

print(fruit[-2])

#Update Lists
fruit.append("apples")
print(fruit)

#Add an element at a specific point in the list using the index value with the insert() method
fruit.insert(2, "mangos")
print(fruit)

#Organizing a List

#Return information while retaining the original order of the list with the sorted() function
print(sorted(fruit))

print(fruit)

#Permanently sort the list using the sort() method
fruit.sort()
print(fruit)

#Reverse the order of a list with the reverse() method
fruit.reverse()
print(fruit)

#Delete Lists
del fruit[1]
print(fruit)

#Using the value after removing it from a list with the pop() method
favorite_fruit = fruit.pop()
print(favorite_fruit)

#Return any element with the pop() method by using the index value
fresh_fruit = fruit.pop(1)
print(fresh_fruit)

#Use the remove() method to specify the value of the element you want to remove
fruit.remove('mangos')
print(fruit)

#Determining Type

#Find out what type of data python has stored in a variable using the type() method
sample_variable = "My string"
print(type(sample_variable))

#Fix the TypeError by telling python to convert my_number to a string
my_number = 11
sample_string = "The number is "
print(sample_string + str(my_number))
