# Blank Line

# Question with multiple awnsers:

favcol = input("\nWhat is your favorite color?: ")

if favcol.lower() == "red":
    print("\nYeah, i like the color red too, that's also my favorite.")
if favcol.lower() == "blue":
    print("\nI like blue too, you got nice tastes")
if favcol.lower() == "beige":
    print("\nWow, pretty not common likes, i like that color too")
if favcol.lower() != "red" or "blue" or "beige":
    print("\nYou got pretty good likes, but those colors are not for me though")
input("\nPress enter to continue: ")

# Numbers

num1 = float(input("\nWrite the first number:"))
num2 = float(input("\nWrite the second number:"))

if num1 > num2:
    print(f"\n{num1} is greater than {num2}.")
    print(f"\n{num2} is less than {num1}.")
else:
    print(f"\n{num2} is greater than {num1}.")
    print(f"\n{num1} is less than {num2}.")
if num1 == num2:
    print("\nBoth numbers are equal.")
else:
    print("\nBoth numbers are different")