num = int(input("Enter a number: "))
check = int(input("Enter a divisor for your num(dividend): "))

if(num % 4 == 0):
    print(num, " is divisible by 4!")
elif(num % 2 == 0):
    print(num ,  " is EVEN!")
else:
    print(num , " is ODD!")

if (num % check == 0):
    print(num, "%", check, "is divided without a remainder.")
else:
    print(num, "%", check, "is divided with a remainder.")
