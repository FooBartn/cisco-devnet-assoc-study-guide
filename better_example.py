def getFullName(person):
    return f'{person["firstName"]} {person["lastName"]}'

people = [
    {
        "firstName": "John",
        "lastName": "Carpenter",
        "occupation": "Director"
    },
    {
        "firstName": "Madeleine",
        "lastName": "L'Engle",
        "occupation": "Author"
    }
]

print(getFullName(people[0]))
print(getFullName(people[1]))