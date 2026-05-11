#class Person:
#    city = "Pune"

Person = type("Person", (), {"city": "Pune"})

print(Person, Person.city)