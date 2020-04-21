#   a117_grades.py
#   This code is incomplete.
my_courses = ["English", "Math", "CS"]

check_grades = True
while (check_grades):
    for course in my_courses:
        print()
        print("Enter your points for", course)
        points = int(input("Points -> "))
        if points >= 90:
            print("A")
        elif points >= 80:
            print("B")
        elif points