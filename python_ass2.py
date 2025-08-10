my_list = []

# Append values to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting 15 at the second position of the list
my_list.insert(1, 15)

# Extending the list
my_list.extend([50, 60, 70])

# Removing the last element
my_list.pop()

# sorting the list in ascending order
my_list.sort()

# Find and print the index of 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)