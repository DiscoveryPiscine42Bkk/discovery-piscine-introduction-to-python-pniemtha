original_array = [2, 8, 9, 48, 8, 22, -12, 2]
print(original_array)

transformed_set = set()

for x in original_array:
    if x == 2:
        transformed_set.add(24)
    elif x in [8, 9, 48]:
        transformed_set.add(x + 2)

print(transformed_set)