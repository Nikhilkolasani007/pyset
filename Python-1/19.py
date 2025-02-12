def remove_key(d, key):
    """
    Removes a key-value pair from the dictionary if the key exists.

    :param d: Dictionary from which the key needs to be removed
    :param key: Key to be removed
    :return: Updated dictionary
    """
    if key in d:  # Check if key exists
        del d[key]  # Remove key-value pair
    return d

# Example dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Remove key 'b'
updated_dict = remove_key(my_dict, 'b')
print(updated_dict)  # Output: {'a': 1, 'c': 3}
