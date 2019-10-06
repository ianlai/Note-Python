class Student:
    count = 0
    def __init__(self, id, name, isSpecial=False):
        self.id   = id      # instance variable 
        self.name = name
        self.isSpecial  = isSpecial
        Student.count += 1
    def __str__(self):
        if self.isSpecial is True:
            return "* id: " + str(self.id) + "  " + "name: " + self.name 
        else:
            return "  id: " + str(self.id) + "  " + "name: " + self.name 
    def __gt__(self, s):
        return self.id > s.id

studentList = [
    Student(9, "aaaaaaa"),
    Student(5, "ccc", True),
    Student(8, "bb"),
    Student(2, "eee", True),
    Student(1, "ddd"),
    Student(10, "1000"),
    Student(15, "1555"),
    Student(4, "444"),
    Student(3, "333"),
    Student(7, "777"),
]

# arbitrary order 
for student in studentList:
    print(student)

# sorted by id 
for student in sorted(studentList):
    print(student)