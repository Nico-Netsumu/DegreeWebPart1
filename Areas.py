# Blank Line

# Prices of meals and other stuff.
# childme = child meal    # adultme = adult meal    # childso = child soda    # adultso = adult soda

childme = float(input("\nWhat is the price of the child meal?: "))
adultme = float(input("\nWhat is the price of the adult meal?: "))
childso = float(input("\nWhat is the price of the child soda? (for every pair of childs, you get a soda): "))
adultea = float(input("\nWhat is the price of the adult tea?  (for every pair of adults, you get a tea) : "))

# Imagine there is a combo where; for example, if you come with a adult to purchase a soda for -
# their 4 kids. They are gonna to pay just the half of the price for 2 sodas (a fair size of course).

# Number of childs/adults.
# childqa = number of childs    # adultqa = number of adults

childqa = int(input("\nHow many childs are there?: "))
adultqa = int(input("\nHow many adulds are there?: "))

# Results (#1)
# totaln1 = Subtotal amount
sodatea = int((childso / 2) + (adultea / 2))
totaln1 = float((childme * childqa) + (adultme * adultqa) + sodatea)

print(f"\n\nSubtotal: ${totaln1:.2f}")

# Taxes
# taxrate = tax rate sales (of course)    # saletax = Subtotal amount with tax rate sales

taxrate = float(input("\nWhat is the sales tax rate?: "))
saletax = float(totaln1 * taxrate / 100)

# Results (#2)
# totaln2 = The total payment overall

totaln2 = totaln1 + saletax

print(f"\n\nSales Tax: ${saletax:.2f}")
print(f"Total: ${totaln2:.2f}")

# Payment
# payment = the total amount you are gonna pay    # totaln3 = your change

payment = float(input("\nHow much you are gonna to pay?: "))
totaln3 = payment - totaln2

print(f"\n\nChange: ${totaln3:.2f}\n")

# If a error happens, use txt instead.