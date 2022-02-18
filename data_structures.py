# DICTIONARY

# note: a key can be a string or an integer
dictionary_1 = {"user_id":123, "name":"janson", "location":"(1.11, -11.111)"}
print(dictionary_1)

# adding a dictionary
dictionary_1["position"] = "web developer"
print("adding a key-value pair = ", dictionary_1)

dictionary_2 = {"user_id":456, "name":"jefferson", "location":"(2.22, -22.222)"}
print(dictionary_2["user_id"])

# catching an error in a dictionary
try:
    print(dictionary_2["position"])
except KeyError:
    print("error: not found")

# another way of printing a dictionary
print(dict([("jan", 123), ("jeff", 456), ("jet", 789)]))
# or
print(dict(jan=123, jeff=456, jet=789))

# LIST
fruits = ["apple", "grapes", "mango"]
print("example = ", fruits)

# .insert()
fruits.insert(2, "banana")
print("this is insert = ", fruits)

# .append()
fruits.append("melon")
print("this is append = ", fruits)

# .pop()
print("this is pop = ", fruits.pop())
print("this is pop = ", fruits)

# .reverse()
fruits.reverse()
print("this is reverse = ", fruits)

# .count()
print("this is count of apple = ", fruits.count("apple"))

# .copy()
fruits_2 = fruits.copy()
print("this is fruits_2 from copy = ", fruits_2)

# .extend()
fruits_3 = ["orange", "watermelon", "coconut"]
fruits.extend(fruits_3)
print("this is extend = ", fruits)
# or
# print("this is extend = ", fruits + fruits_3)

# .sort()
fruits.sort()
print("this is sort = ", fruits)

# .remove()
fruits.remove("apple")
print("this is remove = ", fruits)

# .clear()
fruits.clear()
print("this is clear = ", fruits)

# .index()
janson = ['siy', 'Pasig', 'siy', 27]

# note: will stop upon first occurence
print("this is simple indexing = ", janson.index('siy'))

# note: ignored 'siy' under index 0 because you told it to start at index 1
print("this is targeted indexing = ", janson.index('siy', 1))

jeff = [1, 2, 1, 1, 3, 4, 1]

# note notes: started to look for 1 from index 4 to 7 then returned the index number of the first occurence
print("this is range indexing = ", jeff.index(1, 4, 7))