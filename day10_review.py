items = [5, 3, 9, 3, 7]

items.append(1)
items.remove(3)
print(items) # 5, 9, 3, 7, 1

last = items.pop()
print(last) # 1
print(items) #  5, 9, 3, 7

print(sorted(items)) # 3, 5, 7, 9
print(items) # 5, 9, 3, 7

print(items[1:3]) # 9, 3
print(items.count(3)) # 1
print(set(items)) # 5, 9, 3, 7
print(max(items) - min(items)) # 6