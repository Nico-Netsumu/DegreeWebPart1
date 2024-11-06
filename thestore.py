# Blank Line

# Needed information. "goback" is self explanatory, return to the beggining.

thecart = ["0"]
item = None
prodcost = [0]
costs = 0

goback = 0
asktheuser = ["0", "Add a new item.", "Your cart content.", "Remove a item.", "Compute the total.", "Quit. ---->"]
askme = None

# Intro 

print("\nWelcome to MyStore! What do you want?\n")

asktheuser.append(askme)

while goback != 1:

    for i in range(len(asktheuser)):
        askme = asktheuser[i]
        if askme != "0":
            if askme != None:
                print(f"{i}. {askme}")

    selected = int(input("\nWrite the index for the corresponding option: "))
    
    # Add a new item.

    if selected == int(1):

        newitem = item = input("\nWrite the item you want to purchase, cancel by writing 'quit': ")
    
        if item != "quit":
            thecart.append(item)
            costs = float(input("\nHow much cost your product? (Don't add $ or similar money signs): "))
            input(f"\nYour item, '{newitem}', has a cost of ${costs:.2f}. Press Enter to return. ")
            prodcost.append(costs)
            print("\nWelcome back! Need something more?\n")
            goback = 0   
    
        else:
            thecart.append(item)
            input("\nCanceled purchase, go back to the menu pressing Enter. ")
            print("\nWelcome back! Need something more?\n")
            goback = 0

    # Your cart content.
    
    if selected == int(2):
        
        print("\nThis is your cart:")
        
        for j in range(len(thecart)):
            item = thecart[j]
            if item != "0":
                if costs != 0:
                    costs = prodcost[j]
                    print(f"{j}. {item} - {costs:.2f}")
        
        print("")
        input("Press Enter to return. ")
        print("\nWelcome back! Need something more?\n")
        goback = 0

    # Remove item

    if selected == int(3):

        for j in range(len(thecart)):
            item = thecart[j]
            if item != "0":
                if costs != 0:
                    costs = prodcost[j]
                    print(f"{j}. {item} - {costs:.2f}")
        
        remove = int(input("\nWrite by index, the item you want to remove. (use '999' if you want to cancel): "))
        
        if remove != 999:
        
            thecart.pop(remove)
            prodcost.pop(remove)
            input(f"\nYour item has successfully been removed of your cart. Press Enter to continue.")
            print("\nWelcome back! Need something more?\n")
            goback = 0

        else:
            input("\nCanceled purchase, go back to the menu pressing Enter. ")
            print("\nWelcome back! Need something more?\n")
            goback = 0

    
    # Compute the total.
    
    if selected == int(4):
        
        runntot = 0
        for costs in prodcost:
            
            runntot += costs
        print(f"\nYour total amount is {runntot:.2f}.")
        
        input("Press Enter to go back to the beggining. ")
        print("\nWelcome back! Need something more?\n")
        goback = 0

    # Quit!

    if selected == int(5):
        print("\nThanks for using our program!")
        goback = 1
    
    # in case typo occurrs in menu