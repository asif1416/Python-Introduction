noOfDays = int(input("Enter total number of working days: "))
noOfAbsent = int(input("Enter number of days absent: "))

per=(noOfDays-noOfAbsent)/noOfDays*100

print("Your attendance is ",per)
if per <75 :
     print("You are not eligible for exams")
else:
     print("You are eligible for writing exam")