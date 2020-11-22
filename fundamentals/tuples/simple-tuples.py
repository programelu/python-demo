"""tuples may have paranthesys or not"""

#tuple with paranthesys, recommanded for redability reasons
plane1 = ("Airbus", "319", 200)
print(plane1)


#tuple without paranthesys - recognized as tuples because comma has been encountered
plane2 = "Airbus", "A380", 500
print(plane2)



print(plane2[0])

#Tuples with only one element MUST be defined with a comma. Below there is NOT a tuple, it's just a string
tup1 = ("Streets of Philadelphia")
print(tup1)

#Comma MUST be added even if there's only one element! Now we have a tuple as we've added a comma
tup1 = ("Streets of Philadelphia",)
print(tup1)


#access hour minute second and calculate the total seconds in the day from time_tuple = (hour, minute, second)
time_tuple = (9, 16, 11)
total_sec = time_tuple[0] * 3600 + time_tuple[1] * 16 + time_tuple[2]
print(f"Seconds in the day: {total_sec}")


#Tuples are immutable! But cotained objects ca be modified
student_tuple = ("Amanda", [17, 20 , 22])
print(student_tuple)
student_tuple[1][2] = 55
#the list object at position 1 will be modified, it's second element is changed to 55
print(student_tuple)


#tuples are immutable, cannot change anything from a tuple but create and assign another value
plane2 = "Boeing" ,"777", 380
print(plane2)

#THIS CANNOT WORK!!! Cannot assign a value to an item of the tuple - immutability
plane2[0] = "Airbus"

