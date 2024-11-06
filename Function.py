# Blank Line

# Defines a code, DEF is all the coding that you can use it later

def display_regular(message):
    print(message)

def display_uppercase(message):
    # This could be done on one line, without creating a new variable new_message
    new_message = message.upper()
    print(new_message)

def display_lowercase(message):
    new_message = message.lower()
    print(new_message)

# The regular flow of the program starts here...
user_message = input("What is your message? ")

# Pass this variable to each of the functions above to do their work
display_regular(user_message)
display_uppercase(user_message)
display_lowercase(user_message)


import math

def compute_area_square(side):
    return side * side

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * radius * radius


# The main program starts here...
shape = ""

while shape != "quit":
    shape = input("What shape do you have? ")

    # Convert it to lower case once, so we don't have to keep converting it
    shape = shape.lower()

    if shape == "square":
        side = float(input("What is the length of the side? "))
        area = compute_area_square(side)
        print(f"The area is {area}")
    elif shape == "rectangle":
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        area = compute_area_rectangle(length, width)
        print(f"The area is {area}")
    elif shape == "circle":
        radius = float(input("What is the radius? "))
        area = compute_area_circle(radius)
        print(f"The area is {area}")