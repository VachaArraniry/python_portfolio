fruits = ["apple", "durian", "strawberry", "orange"] # list literal

print(len(fruits))

fruits.append("kiwi") # add an item to the list

print(len(fruits))

print(fruits[1])

# get orange from the list
print(fruits[3])

# get the last fruit from the list
print(fruits[-1]) # simple version
print(fruits[len(fruits)-1]) # mathematical version

# add an item to a specific index
fruits.insert(2, 'rambutan')

print(fruits)

# for loop
for item in fruits:
    print(item.upper())