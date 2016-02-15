a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
my_list = []
for i in a:
    if i < 5:
        my_list.append(i)
    else:
        print(my_list, "elements containing this list is smaller than 5.\n\n\n")
        break

#Extras:

print(a)
choice = int(input("Choose a number in the list: "))

for i in a:
    if choice not in a:
        print("Choice should be in the list.")
        break
    elif choice > i:
        my_list.append(i)
    else:
        print(my_list, ",elements containing this list is smaller than", choice)
        break
