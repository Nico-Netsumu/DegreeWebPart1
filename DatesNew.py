# Blank Lines

# Ignore this.

reset = 0

# Open this data.

with open("life-expectancy.csv") as linecontent:

    maxlifex = -1
    minlifex = 99999999999999
    maxcntry = ""
    mincntry = ""
    maxsyear = -1
    minsyear = 99999999999999
    worldave = None

    for line in linecontent:
        line = line.strip()
        parts = line.split(",")
        
        if parts[2] != "Year" and parts[2] != "Life expectancy (years)":
            if parts[3] != "Life expectancy (years)":
                cname = parts[0]
                years = int(parts[2])
                lifex = float(parts[3])

                if lifex < minlifex:
                    minsyear = years
                    minlifex = lifex
                    mincntry = cname

                if lifex > maxlifex:
                    maxsyear = years
                    maxlifex = lifex
                    maxcntry = cname

print(f"\nThe overall max life expectancy is: {maxlifex} from {maxcntry} in {maxsyear}.")
print(f"The overall min life expectancy is: {minlifex} from {mincntry} in {minsyear}.")


newyear = int(input("\nWrite a Year, for info in life expectancy (Take in mind not many years are aviable on this sheet): "))

maxlifexyear = -1
minlifexyear = 99999999999999
maxcntryyear = ""
mincntryyear = ""

with open("life-expectancy.csv") as linecontent:
    for line in linecontent:
        line = line.strip()
        parts = line.split(",")
        if parts[2] == str(newyear):
            lifex = float(parts[3])
            if lifex > maxlifexyear:
                maxlifexyear = lifex
                maxcntryyear = parts[0]
            if lifex < minlifexyear:
                minlifexyear = lifex
                mincntryyear = parts[0]

print(f"\nThis is the info from the year {newyear}:")
print(f"The max life expectancy was in {maxcntryyear} with {maxlifexyear}.")
print(f"The min life expectancy was in {mincntryyear} with {minlifexyear}.")