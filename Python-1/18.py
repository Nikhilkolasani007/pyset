'''18) Create two set and write a program to find the union, intersection, and difference between them.'''
# Define two sets
set1 = {1, 2, 3, 4, 5, 5}
set2 = {4, 5, 6, 7, 8}
a = list(set(set1))
print(set(a))
# Union (All unique elements from both sets)
union_set = set1.union(set2)  
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection (Common elements)
intersection_set = set1.intersection(set2)  
print("Intersection:", intersection_set)  # Output: {4, 5}

# Difference (Elements in set1 but not in set2)
difference_set1 = set1.difference(set2)  
print("Difference (set1 - set2):", difference_set1)  # Output: {1, 2, 3}

# Difference (Elements in set2 but not in set1)
difference_set2 = set2.difference(set1)  
print("Difference (set2 - set1):", difference_set2)  # Output: {8, 6, 7}

'''
union_set = set1 | set2
intersection_set = set1 & set2
difference_set1 = set1 - set2
difference_set2 = set2 - set1


'''