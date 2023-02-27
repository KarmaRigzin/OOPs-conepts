import random

students = ["Anita","Pema","Dorji","Karma"]

# function
def group(group_number, students):
    return f"Group {group_number} captain {students[group_number-1][:5]}"

print(students)

#students
for i in range(1, len(students)+1):
    print(group(i, students))
