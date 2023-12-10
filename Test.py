sorted_list = [1, 2, 3, 4, 5]
unsorted_list = [3, 2, 5, 1, 4]

print(sorted(sorted_list))
print(sorted(unsorted_list))

if unsorted_list == sorted(unsorted_list) is True:  # Checks to see if list is sorted yet.
    print("is sorted")
else:
    print("is not sorted")
