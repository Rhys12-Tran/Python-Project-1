"""
Simple Python Mad Libs Game
"""
# Function to get user input
# Follow the answers (place, name, adjective, noun, verb, number, adjective, name, verb, place, number)
Story = "Today I went to the {} with my friend {}. We saw a {} {} that wanted to {}. It cost {} dollars!"\
        "Once upon a time, a {} {} named {} decided to {} in the {}. Everyone cheered {} times."

# Get user inputs
place1 = input("Enter a place: ")
name1 = input("Enter a name: ")
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
number1 = input("Enter a number: ")
adjective2 = input("Enter another adjective: ")
name2 = input("Enter another name: ")
verb2 = input("Enter another verb: ")
place2 = input("Enter another place: ")
number2 = input("Enter another number: ")
# print the story with user inputs 
print(Story.format (place1, name1, adjective1, noun1, verb1, number1, adjective2, noun1, name2, verb2, place2, number2))