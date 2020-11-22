"""tuples may have paranthesys or not"""

#tuple with paranthesys, recommanded for redability reasons
plane1 = ("Airbus", "319", 200)
print(plane1)


#tuple without paranthesys - recognized as tuples because comma has been encountered
plane2 = "Airbus", "A380", 500
print(plane2)


#tuples are immutable, cannot change anything from a tuple but create and assign another value
plane2 = "Boeing" ,"777", 380
print(plane2)

print(plane2[0])

#THIS CANNOT WORK!!! Cannot assign a value to an item of the tuple - immutability
plane2[0] = "Airbus"

