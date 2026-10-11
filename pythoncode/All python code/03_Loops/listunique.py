items = ["apple", "banana", "cherry", "apple", "date", "banana"]

unique_items = set()

for item in items:
    if item not in unique_items:
        print("duplicate item is:")
        break
    unique_items.add(item)