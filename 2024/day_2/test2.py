levels = [1, 3, 3, 4, 5]

# Find the index of the specific 3 to remove
# index_to_remove = levels.index(3)  # This finds the first occurrence of 3
levels.pop(1)

print(levels)  # Output: [1, 3, 4, 5]
