student = {"Name" : "Aditya" ,
     "Roll_number":127,
     "Standard" :10,
     "Marks":92}

print(f"Before modify{student}")
student["Marks"] = 89
student.update({"Marks": 77})
student["Phoneno"] = 849400505
print(f"after Modify {student}")



