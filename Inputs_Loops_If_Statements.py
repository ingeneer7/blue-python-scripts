# Inputs

# Step 1: User input from the console
# Provide user input when the program is run and pass this to the function
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

# Use  input() function to prompt the user with a message and then wait for them to provide input
import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###

text = input("What language are you translating to: ")
source_language_code = input("Provide the two letter source language code: ")
target_language_code = input("Provide the two letter target language code: ") 

def main():
    translate_text(
        Text=text,
        SourceLanguageCode=source_language_code,
        TargetLanguageCode=target_language_code
        )

if __name__=="__main__":
    main()
# Run the command: python name_of_your_file.py

# Step 2: CLI Arguments
# Using a method of passing parameters via the Command Line Interface (CLI)
import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###

text = input("What language are you translating to: ")
source_language_code = input("Provide the two letter source language code: ")
target_language_code = input("Provide the two letter target language code: ") 

def main():
    translate_text(
        Text=text, 
        SourceLanguageCode=source_language_code,
        TargetLanguageCode=target_language_code
        )

if __name__=="__main__":
    main()

# Using argparse to input arguments from the CLI
# import argparse # argparse is a built in python package, we add it with an import statement
import boto3

# Define the parser variable to equal argparse.ArgumentParser()
parser = argparse.ArgumentParser(description="Provides translation between one source language and another of the same set of languages.")

# Add each of the arguments using the parser.add_argument() method
parser.add_argument(
    '--text',
    dest="Text",
    type=str,
    help="The text to translate. The text string can be a maximum of 5,000 bytes long. Depending on your character set, this may be fewer than 5,000 characters",
    required=True
    )

parser.add_argument(
    '--source-language-code', 
    dest="SourceLanguageCode", 
    type=str, 
    help="The language code for the language of the source text. The language must be a language supported by Amazon Translate.",
    required=True
    )

parser.add_argument(
    '--target-language-code',
    dest="TargetLanguageCode",
    type=str,
    help="The language code requested for the language of the target text. The language must be a language support by Amazon Translate.",
    required=True
    )

# # This will inspect the command line, convert each argument to the appropriate type and then invoke the appropriate action.
args = parser.parse_args()

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

def main():
    # vars() is an inbuilt function which returns a dictionary object
    translate_text(**vars(args))

if __name__=="__main__":
    main()
Run the command: python name_of_your_file.py --text "we are learning python on AWS" --source-language-code en --target-language-code fr

Step3: Step 3: Input from a file
Input data from a file
Create a python file and add the following code:
def open_input(file):
    with open(file, 'r') as f:
        text = f.read() #We use read() to read the actual contents of the file
        print(text)

def main():
    open_input("text.txt")

if __name__=="__main__":
    main()

# Create a text file and add text you want it to pull from that file:
# "The Quick Brown Fox"

# Step 4: JSON
# Use json.loads() & json.dumps() to input and output JSON from strings and into strings
import json

# This uses a json string as an input 

json_string = """
{
    "Input":[
        {
        "Text":"On the road to becoming a Cloud DevOps Engineer",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr",
        "Required": true
        }
    ]
}
"""

def main():
    json_input = json.loads(json_string)
    print(json_input)

if __name__=="__main__":
    main()

# Using json.dumps() with an added parameter to format the string with indentation
import json

# This uses a json string as an input 

json_string = """
{
    "Input":[
        {
        "Text":"On the road to becoming a Cloud DevOps Engineer",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr",
        "Required": true
        }
    ]
}
"""

def main():
    json_input = json.loads(json_string)
    indented_format = json.dumps(json_input, indent=2)
    print(indented_format)

if __name__=="__main__":
    main()

Navigating a JSON Structure with nesting
import json

# This uses a json string as an input 

json_string = """
{
    "Input":[
        {
        "Text":"On the road to becoming a Cloud DevOps Engineer",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr",
        "Required": true
        }
    ]
}
"""
# Modify below this line
def main():
    json_input = json.loads(json_string)
    text = json_input['Input'][0]['Text']
    source_language_code = json_input['Input'][0]['SourceLanguageCode']
    target_language_code = json_input['Input'][0]['TargetLanguageCode']
    print(text, source_language_code, target_language_code)

if __name__=="__main__":
    main()

Use json.load() & json.dump() to input and output JSON from files and into files
#Create a json file and the following text to it:
import json

# This uses a json string as an input 

json_string = """
{
    "Input":[
        {
        "Text":"On the road to becoming a Cloud DevOps Engineer",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr"
        }
    ]
}

"""

# #Add the following code to the python file:
# Standard Imports
import argparse
import json

# 3rd Party Imports
import boto3

# Arguments
parser = argparse.ArgumentParser(description="Provides translation  between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid json",
    required=True)

args = parser.parse_args()

# Functions
def open_input():
    with open(args.filename) as file_object:
        contents = json.load(file_object)
        return contents['Input'][0]

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

# Main Function - use to call other functions
def main():
    kwargs = open_input()
    translate_text(**kwargs)

if __name__ == "__main__":
    main()
# #Run the command: python name_of_your_file.py --file translate_input.json

# Loops

# Step 1: Simple Loops
# Create a list and assign it to a variable, as well as create a for loop
fruit = ['strawberries','grapes','watermelon']

for item in fruit:
    print(f'The best fruit now is {item}')
    
# #Use a loop as a counter to create a list of numbers and assign it to a variable
numbers = [0,1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    print(f'The next number is {number}')

# Use the range() function as a counter for sequence of numbers 
for number in range(10):
  print(f'The next number is {number}')

# Use the range() method to start counting at 1
for number in range(1,10):
    print(f'The next number is {number}')

# Use the range() function to count only odd numbers or even numbers
for number in range(1,10,2):
    print(f'The next number is {number}')

# Step 2: Looping over JSON
# Looping over Dictionaries and JSON

