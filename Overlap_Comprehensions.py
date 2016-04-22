"""
Take two lists, say for example these two:
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
"""

import random

a = set(random.sample(range(1, 31), 18))
b = set(random.sample(range(1, 31), 15))
common_list_a = a.difference(b)
common_list_b = b.difference(a)
result_overlap = [i for i in a if i in b]
all_product = [x*y for x in common_list_a for y in common_list_b]
custom_list = [x for x in all_product if x % 5 == 0]

print(a)
print(b)
print(result_overlap)
print(all_product)
print(custom_list)
