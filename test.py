print("This is to test the same git situation but in python format.")
print("Just input your name and age for the test to run. Thanks!")

name = input("Enter your first name: ")
age = float(input("Enter your age: "))

if age < 18:
    print("Thank you, " + name + " but you're not eligible for to use this platform.")
else:
    print("Thank you, " + name + ", for you are eligible for this platform.")