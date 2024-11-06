# Blank Line

# Identify list(friends) and list's content(myfrend).

friends = []
myfrind = None

# Use this to name friends. Up until you write end.

while myfrind != "end":
    myfrind = input("Name a friend, type 'end' when done: ")
    
# Write this, so "end" will not be part of the list of friends too.

    if myfrind != "end":
        friends.append(myfrind)

# Showcase the list.

print("\nMy friends are:\n")

for myfrind in friends:
    print(myfrind)