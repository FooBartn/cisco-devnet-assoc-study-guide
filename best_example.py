class Person:
  def __init__(self, firstName, lastName, occupation):
    self.firstName = firstName
    self.lastName = lastName
    self.occupation = occupation

  def getFullName(self):
      return f'{self.firstName} {self.lastName}'

people = []
people.append(Person('John', 'Carpenter', 'Director'))
people.append(Person('Madeleine', "L'Engle", 'Author'))

print(people[0].getFullName())
print(people[1].getFullName())