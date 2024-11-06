# Blank Line

# First open the files.

with open("files.txt") as filecontent:
    
    for line in filecontent:

        line = line.strip()
        parts = line.split(",")
        
        name = parts[0]
        notes = float(parts[1])

        bonus = notes + 3

        print(f"{name} - Note: {notes}, With adittional bonus: {bonus}")
