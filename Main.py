welcome_banner = """
                Welcome to the List Workout!
    In this app, you'll need to create lists based off of
    the prompts below and display the correct item from 
    each list to answer the prompt.
"""

print(welcome_banner)


# Create a list of the 8 planets in our solar system (in order from closest to the
# sun to farthest from the sun)

planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']

# Display the list of planets
print(f"Here are all the planets: {planets}")

# Display "There are 8 planets in our solar system". Use the function that
# tells you how many items are in a list to do this.
planets = len(planets)

# For the next set of challenges, you'll need to use the correct index
# number of each planet as you display information about them.



# Display "We live on planet Earth".
print("We live on planet Earth")

# Display "The closest planet to the sun is Mercury".
print("The closest planet to the sun is Mercury")

# Display "The farthest planet from the sun is Neptune".
print("The farthest planet from the sun is Neptune")

# Display "The great red spot is on Jupiter".
print("The great red spot is on Jupiter")




# Add a conditional statement that displays
# "Pluto is in our planets list" if Pluto is in the list of planets
# It should display "Pluto is NOT in our planets list" otherwise.


question = (input("Is Pluto in our planets list? Type yes or no "))

if question == "yes" :
    print("Pluto is now in our planets list.")

    
if question == "no" :
    print("Pluto is not in our planets list.")





# Add Pluto to the end of the planets list.


# Add a conditional statement that displays
# "Pluto has been added to the planets list" if Pluto is in the list of planets
# It should display "Pluto has not been added to the planets list" otherwise.


print("Nevermind, let's remove Pluto from the list of planets.")

# Remove Pluto from the planets list

# Add a conditional statement that displays
# "Pluto has been removed from the planets list" if Pluto is not in the list of planets
# It should display "Pluto is still in the planets list" otherwise.
