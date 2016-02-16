input = input("Input a palindrome words: ")
var = []

for i in input:
    var.append(i)

if var == var[::-1]:                                    #"".join() make [a, b, c] to abc
    print(input.upper() + " is palindrome!\n")                          
    print("\tINPUT")
    print("".join(var))
    print("\tREVERSED")
    print("".join(var[::-1]))
else:
    print(input.upper() + " is not a palindrome!\n")
    print("\tINPUT")
    print("".join(var))
    print("\tREVERSED")
    print("".join(var[::-1]))
