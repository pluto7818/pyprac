# ----------------------------------------
# OOP Program: Student Class
# ----------------------------------------

class Student:
    def __init__(self, std_id, std_name, python, r, stat, excel, powerbi):
        # Instance variables
        self.std_id = std_id
        self.std_name = std_name
        self.python = python
        self.r = r
        self.stat = stat
        self.excel = excel
        self.powerbi = powerbi

    # Method 1: Display student details
    def student_detail(self):
        print("\n--- Student Details ---")
        print("Student ID:", self.std_id)
        print("Student Name:", self.std_name)
        print("Python:", self.python)
        print("R:", self.r)
        print("Statistics:", self.stat)
        print("Excel:", self.excel)
        print("PowerBI:", self.powerbi)

    # Method 2: Calculate result
    def student_result(self):
        total = self.python + self.r + self.stat + self.excel + self.powerbi
        percent = total / 5

        # Grade calculation
        if percent >= 75:
            grade = "A"
        elif percent >= 60:
            grade = "B"
        elif percent >= 50:
            grade = "C"
        else:
            grade = "F"

        # Pass/Fail condition
        result = "PASS" if percent >= 50 else "FAIL"

        print("\n--- Result ---")
        print("Total Marks:", total)
        print("Percentage:", percent)
        print("Grade:", grade)
        print("Result:", result)


# ----------------------------------------
# Taking input from user
# ----------------------------------------

std_id = input("Enter Student ID: ")
std_name = input("Enter Student Name: ")

python = int(input("Enter marks in Python: "))
r = int(input("Enter marks in R: "))
stat = int(input("Enter marks in Statistics: "))
excel = int(input("Enter marks in Excel: "))
powerbi = int(input("Enter marks in PowerBI: "))

# Create object
s1 = Student(std_id, std_name, python, r, stat, excel, powerbi)

# Call methods
s1.student_detail()
s1.student_result()

# ----------------------------------------
# End of Program
# ----------------------------------------