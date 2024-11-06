people = [
    "Stephanie 36",
    "John 15",
    "Emily 56",
    "Gretchen 54",
    "Noah 53",
    "Penelope 32",
    "Michael 45",
    "Jacob 23"
]

youngest_age = 9999
oldest_age = -1
youngest_name = ""
oldest_name = ""


for person_line in people:

    parts = person_line.split()
    name = parts[0]
    age = int(parts[1])

    if age < youngest_age:

        youngest_age = age
        youngest_name = name

        if age > oldest_age:

            oldest_age = age
            oldest_name = name


# Outside of the loop, so we are all done now
print(f"The youngest person is: {youngest_name} with an age of {youngest_age}\nThe oldest person is: {oldest_name} with an age of {oldest_age}")