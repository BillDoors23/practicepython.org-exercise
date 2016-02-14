name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
copies = int(input("Number of copies you want to print out: "))


if age >= 100:
    print(copies * (name + " You're too old!\n"))
elif age <= 99:
    year_age = str((2016 - age) + 100)
    print(copies * (name + ", you will turn 100 at year " + year_age + ".\n"))
