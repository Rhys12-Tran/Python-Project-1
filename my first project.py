"""
Today I will write my first programming project!
"""

# 1 Bún Bò, 2 Vietnamese, 3 beef
story = " %s is a general name for %s dishes featuring vermicelli rice noodles (bún)" \
" and beef (bò). The most famous variations are Bún bò Huế, a spicy %s and pork noodle soup, and Bún bò Nam Bộ, a beef noodle salad."

# story started 
print("The game is starting...")

# Now ask the user type the missing words
Food = input("Enter a Vietnamese dish:")
Country = input("Enter a contry: ")
Meat = input("Enter a type of meat:")

# Run code
print(story%(Food, Country, Meat))