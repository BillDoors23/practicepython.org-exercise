dividend = int(input("Input a number to divide: "))
my_list = []

for i in range(1, dividend):
    if dividend % i == 0:
        my_list.append(i)

print(my_list)
