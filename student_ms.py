
try:
    f = open("student.txt", "a")
    f.close()
    print("student.txt is ready!")
except:
    print("Cannot create student.txt!")

def add_student():
    roll = input("Enter Roll Number: ").replace(" ", "")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ").replace(" ", "")

    line = roll + "," + name + "," + marks + "\n"

    f = open("student.txt", "a")
    f.write(line)
    f.close()

    print("Student Added Successfully!")

def view_students():
    f = open("student.txt", "r")
    data = f.readlines()
    f.close()

    if len(data) == 0:
        print("No Records!")
        return

    print("\n--- Student List ---")
    for line in data:
        print(line)
def search_student():
    r = input("Enter Roll to Search: ").replace(" ", "")
    found = False

    f = open("student.txt", "r")
    data = f.readlines()
    f.close()

    for line in data:
        line = line.replace("\r", "")   

        c1 = line.find(",")
        roll = line[:c1]

        if roll == r:
            print("Student Found:", line)
            found = True

    if not found:
        print("Student Not Found!")
def delete_student():
    r = input("Enter Roll to Delete: ").replace(" ", "")
    deleted = False

    f = open("student.txt", "r")
    data = f.readlines()
    f.close()

    new_data = ""

    for line in data:
        c1 = line.find(",")
        roll = line[:c1]

        if roll != r:
            new_data += line
        else:
            deleted = True

    f = open("student.txt", "w")
    f.write(new_data)
    f.close()

    if deleted:
        print("Record Deleted!")
    else:
        print("Roll Not Found!")
def update_student():
    r = input("Enter Roll to Update: ").replace(" ", "")
    updated = False

    f = open("student.txt", "r")
    data = f.readlines()
    f.close()

    new_data = ""

    for line in data:
        c1 = line.find(",")
        roll = line[:c1]

        if roll == r:
            name = input("Enter New Name: ")
            marks = input("Enter New Marks: ").replace(" ", "")
            new_data += r + "," + name + "," + marks + "\n"
            updated = True
        else:
            new_data += line

    f = open("student.txt", "w")
    f.write(new_data)
    f.close()

    if updated:
        print("Record Updated!")
    else:
        print("Roll Not Found!")
def calculate_avg_topper():
    f = open("student.txt", "r")
    data = f.readlines()
    f.close()

    if len(data) == 0:
        print("No Records!")
        return

    total = 0
    count = 0
    top_name = ""
    top_marks = -1

    for line in data:
        c1 = line.find(",")
        c2 = line.find(",", c1 + 1)

        name = line[c1+1:c2]
        marks_text = line[c2+1:]

        marks_text = marks_text.replace("\n", "")
        marks_text = marks_text.replace("\r", "")   # <-- MAIN FIX

        marks = int(marks_text)

        total += marks
        count += 1

        if marks > top_marks:
            top_marks = marks
            top_name = name

    avg = total / count

    print("Class Average:", avg)
    print("Topper:", top_name, "Marks:", top_marks)
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Avg & Topper")
    print("7. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        view_students()
    elif ch == "3":
        search_student()
    elif ch == "4":
        update_student()
    elif ch == "5":
        delete_student()
    elif ch == "6":
        calculate_avg_topper()
    elif ch == "7":
        break
    else:
        print("Invalid Choice!")
