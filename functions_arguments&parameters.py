#Functions

#A Simple Function
# Wite a function that prints blue cohort
def blue_cohort():
    print('blue cohort')

# This line calls (runs) the function
blue_cohort()

#Returning information from a function
# A function that returns hello world
def blue_cohort():
    return 'blue cohort'

# Assign the hello_world() function to a variable.
bootcamp = blue_cohort()
print(bootcamp)

#Using SourceLanguageCode and TargetLanguageCode

import boto3

client = boto3.client('translate')

#### Add the new text below this line ####

def translate_text(): # declare the function using def, name, braces for parameters and a colon  
    response = client.translate_text(
        Text='On the road to becoming a Cloud DevOps Engineer', # Assigning the value of the string to the variable Text
        SourceLanguageCode='en', # We are using a two letter language code from the documentation (en = English)
        TargetLanguageCode='fr' # We use a second two letter language code from the documentation (fr = French)
    )


#Output the response of SourceLanguageCode and TargetLanguageCode
import boto3

client = boto3.client('translate')

def translate_text(): 
    response = client.translate_text(
        Text='On the road to becoming a Cloud DevOps Engineer', 
        SourceLanguageCode='en', 
        TargetLanguageCode='fr' 
    )
#### Add the new text below this line ####
    print(response) # this code is inside the function and will print the contents of the variable 'response' 

translate_text() # This line will call our function. Without it, python will not do anything.

#Using the main() function
import boto3

client = boto3.client('translate')

def translate_text():
    response = client.translate_text(
        Text='On the road to becoming a Cloud DevOps Engineer',
        SourceLanguageCode='en',
        TargetLanguageCode='fr'
    )
    print(response) # this code is inside the function and will print the contents of the variable 'response'

def main():
    translate_text()

if __name__=="__main__":
    main()
    
#Arguments

#Step 1: Positional Arguments
#Create a new file in Cloud9
import boto3

def translate_text():
    client = boto3.client('translate')
    response = client.translate_text(
        Text='On the road to becoming a Cloud DevOps Engineer', 
        SourceLanguageCode='en', 
        TargetLanguageCode='fr' 
    )
    print(response) 

def main():
    translate_text()

if __name__=="__main__":
    main()
    
#Amend the function to have some positional arguments:
import boto3

def translate_text(text, source_language_code, target_language_code): # we define the positional arguments in the ()
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text, # we remove the hard coded value
        SourceLanguageCode=source_language_code, # we used the positional argument instead
        TargetLanguageCode=target_language_code
    )
    print(response) 

def main():
    translate_text('On the road to becoming a Cloud DevOps Engineer','en','fr') # we provide the value for the arguments when we call the function in the correct positional order.

if __name__=="__main__":
    main()
    
#Step 2: Keyword Arguments
#Create a new file 
import boto3

def translate_text(text, source_language_code, target_language_code): 
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text, 
        SourceLanguageCode=source_language_code, 
        TargetLanguageCode=target_language_code
    )
    print(response) 

def main():
    translate_text('On the road to becoming a Cloud DevOps Engineer','en','fr')

if __name__=="__main__":
    main()

#Modify the function to use keyword arguments
import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

def main():
    translate_text(Text='On the road to becoming a Cloud DevOps Engineer',SourceLanguageCode='en',TargetLanguageCode='fr')

if __name__=="__main__":
    main()
    
#Use dictionaries as keyword arguments
import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###

kwargs={
    "Text":"On the road to becoming a Cloud DevOps Engineer",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr"
    }

def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()
