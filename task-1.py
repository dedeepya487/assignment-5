
students={"Alice":95,"Bob":85,"Charlie":78,"David":92,"Eva":88}
name=input("Enter student name: ")
if name in students:
    print(f"{name}'s score is {students[name]}")
else:
    print("Student not found.")