import operator

# This example is to show how to sort a dict by its value - using operator
dict1 = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

print("dict1 :", dict1, type(dict1))
print("items :", dict1.items(), type(dict1.items()))

# sort using the value
dict1_sorted_as_list = sorted(dict1.items(), key=operator.itemgetter(1))

print("sorted:", dict1_sorted_as_list, type(dict1_sorted_as_list))

# re-create the dict; now dict ordering is as entered/created (i.e., as sorted above)
dict2 = dict(dict1_sorted_as_list)
print("dict2 :", dict2, type(dict2))

