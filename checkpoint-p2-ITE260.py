def average(a, b, c):
    return (a + b + c) / 3


student = int(input("How many students will be processed? "))

if student < 3:
    student = 3

for i in range(student):
    print()
    print("Student: ", i + 1)

    name = input("Enter your  name: ")
    a = float(input("Activity 1: "))
    b = float(input("Activity  2: "))
    c = float(input("Activity 3: "))

    result = average(a, b, c)

    if result >= 90:
        status = "Excellent"
    elif result >= 80:
        status = "Very Good"
    elif result >= 75:
        status = "Passed"
    else:
        status = "Failed"
        
    print()
    print("Name:", name)
    print("Activity1:", a)
    print("Activity2:", b)
    print("Activity3:", c)
    print()
    print("Average:", result)
    print("Status:", status)