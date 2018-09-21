# remove duplicates from an array
# using a set

array = ["Alex", "John", "Mary", "Steve", "John", "Steve"]

set = set(array)
new_array = list(set)
array = new_array
print(array)

# FIND LARGEST ELEMENT
# using max method

array_find_largest = [1,4,8,9,22,13,18]

largest = max(array_find_largest)

print(largest)

#using a complicated ascending list
#
# array_ascending = []
#
# while array_find_largest:
#     min = array_find_largest[0]
#     for index in array_find_largest:
#         if(index < min):
#             min = index
#     array_ascending.append(min)
#     array_find_largest.remove(min)
#
# for index in array_ascending:
#     largest = array_ascending[(len(array_ascending) -1)]
#
# print(largest)

# FINDIG SMALLEST ELEMENT

array_find_smallest = [1,4,8,9,22,13,18]
smallest = min(array_find_smallest)

print(smallest)
