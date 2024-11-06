# Blank Lines

# Ignore this.

reset = 0

# Open this data.

with open("life-expectancy.csv") as linecontent:
    
    # Useful tools for later.
    
    maxlifex = -1
    minlifex = 99999999999999
    maxcntry = ""
    mincntry = ""
    maxsyear = -1
    minsyear = 99999999999999
    worldave = None
    
    # Load groups of str data.

    for line in linecontent:
        
        line = line.strip()
        parts = line.split(",")
        if parts[2] != "Year" != "Life expectancy (years)":
            if parts[3] != "Life expectancy (years)":
                cname = parts[0]
                years = int(parts[2])
                lifex = float(parts[3])

# Data for minimal and maximum

        if line != "Entity,Code,Year,Life expectancy (years)":

            if lifex < minlifex:

                minsyear = years
                minlifex = lifex
                mincntry = cname

            if lifex > maxlifex:

                maxsyear = years
                maxlifex = lifex
                maxcntry = cname

# Display Results.

print(f"The overall max life expectancy is: {maxlifex} from {maxcntry} in {maxsyear}.")
print(f"The overall min life expectancy is: {minlifex} from {mincntry} in {minsyear}.")

# I need help there.

newyear = int(input("Write a Year, for info in life expectancy (Take in mind not many years are aviable on this sheet): "))

if newyear == years:
    for line in linecontent:
        
        line = line.strip()
        parts = line.split(",")
        if parts[2] != "Year" != "Life expectancy (years)":
            if parts[2] == int(newyear):
                if parts[3] != "Life expectancy (years)":
                    newlifex = float(parts[3])
        
print (newlifex)
            

