students ={'aditya':'95','jidnyasa':'80','utkarsh':'70','Alice':'60'}

stud = input('enter the students name : ')
if stud in students:
    print("{}'s Marks:{} ".format(stud, students.get(stud)))
else:
    print('student not found')