# Input lists
keys_list = [4, 6, 8, 9]
values_list = [4, 6, 6, 5, 8, 10, 4, 9, 8, 10, 1]

# Initialize an empty dictionary
count_dict = {}

# Loop through the keys_list and count occurrences in values_list
for key in keys_list:
    count_dict[key] = values_list.count(key)

# Print the final dictionary
print(count_dict)
