students = [
("Tea", 100),
("Ana", 12),
("Marija", 56),
("Aleksandar", 92),
("Milan", 78),
("Ivan", 45)
]

def test_points(points=0):
    if points <= 50:
        return False
    else:
        return True

def passedstudents(students):
    tally = 0
    list1 = []
    for student in students:
        if test_points(student[1]):
            list1.append(student[0])
            tally += 1
    list1.sort()
    return list1, tally

def fix(students, increase):
    fixed = []
    for student in students:
        value = student[1]
        if not test_points(student[1]):
            value += increase
        fixed.append((student[0], value))
    return fixed

def precentile(student1):
    tally = 0
    listunused, passed = passedstudents(student1)
    for student in students:
        tally += 1
    precent = passed / tally * 100
    return precent

precent = precentile(students)
a = fix(students, 5)
precent2 = precentile(a)
print(f"Precent differences before and after fixes {precent2 - precent}")