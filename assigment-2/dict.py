# 1. Add a new key-value pair to an existing dictionary
d = {"a": 10, "b": 20}
d["c"] = 30
print("1. Dictionary after adding new key-value pair:", d)


# 2. Access a key that does not exist in a dictionary
# Using get() avoids KeyError
d2 = {"x": 100}
value = d2.get("y")
print("2. Accessing non-existing key returns:", value)


# 3. Function that returns keys with values greater than 50
def keys_with_values_greater_than_50(d):
    result = []
    for key, value in d.items():
        if value > 50:
            result.append(key)
    return result


sample_dict = {"a": 40, "b": 60, "c": 80}
print("3. Keys with values greater than 50:",
      keys_with_values_greater_than_50(sample_dict))


# 4. Iterate over both keys and values of a dictionary
d3 = {"name": "Alice", "age": 25}
for key, value in d3.items():
    print("4.", key, ":", value)


# 5. Function that merges two dictionaries
def merge_dictionaries(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print("5. Merged dictionary:", merge_dictionaries(dict1, dict2))
