# Blank Line

shoplist = []
item = None

print("Welcome to the shop! Write here your products you are gonna to purchase! Type 'quit' if finished.\n")

# To make the list with an end, when finished, write "quit".

while item != "quit":
    item = input("Item: ")

# To avoid the appearence of "quit" of the list.
    
    if item != "quit":
        shoplist.append(item)

# Use index there. "i" is the index number, staring in 0. 
# The way the code is. Showcase a number of items distributed by index.

print("\nYour items are the following:")

for i in range(len(shoplist)):
    item = shoplist[i]
    print(f"{i}. {item}.")

# Replace a existing part of the list. 
# Index is the number of item you want to replace. newitem is the replaced item

index = int(input("There is a item you want to change? Write a Number that represents item's index: "))
newitem = input("Write your new item: ")

shoplist[index] = newitem

print("\nYour items are the following:")

for i in range(len(shoplist)):
    item = shoplist[i]
    print(f"{i}. {item}.")

# Remove a existing part of the list.

remove = int(input("There is a item you want to change? Write a Number that represents item's index: "))
shoplist.pop(remove)

print("\nYour items are the following:")

for i in range(len(shoplist)):
    item = shoplist[i]
    print(f"{i}. {item}.")