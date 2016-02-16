input = input("Input a palindrome words: ")
var = []

for i in input:
    var.append(i)

if var == var[::-1]:
    print(input.upper() + " is palindrome!\n")
    print("\tINPUT")
    print(var)
    print("\tREVERSED")
    print(var[::-1])
else:
    print(input.upper() + " is not a palindrome!\n")
    print("\tINPUT")
    print(var)
    print("\tREVERSED")
    print(var[::-1])
