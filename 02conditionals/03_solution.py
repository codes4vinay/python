score = 101

if score > 100:
    print("Invalid Score")
    exit()
    
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "E"
elif score >= 33:
    grade = "Pass"
else:
    grade = "Fail"
    
print("Grade of student is : ",grade)