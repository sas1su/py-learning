# https://www.programiz.com/python-programming/list
# create a list
fruits = ['banana', 'apple', 'cherry']
print(fruits)
# Access list
# index
print(fruits[1])
print(fruits[-1])
# slice
print(fruits[:]) # entire list
print(fruits[1:2]) # from 1 except 2
print(fruits[1:3]) # from 1 except 3
print(fruits[:-1]) # except -1

# add one item by append
fruits.append("orange")
print(fruits)
# several item by extend
veg = ['cabage', 'carrot', 'potato']
fruits.extend(veg)
print(fruits)

# list concatenation
conc = veg + fruits
print(conc)
# list repeat
print( veg * 3)

print("insert in desired location and sliced insert")
odd = [1, 3, 11]
odd.insert(2, 5)
print(odd)
# same index will be squezed with same slice index
# with [3:4]  , odd[4] 11 will be replaced with 9
odd[3:3] = [7, 9]
print(odd)

# remove : given item
# pop : remove item on index or last index and return item
# del : remove entire list and return item
odd.remove(3)
print(odd)
print(odd.pop(2))
print(odd.pop())
#del odd
#print(odd)

print("Remove by assigning empty slice")
odd[2:4] = []
print(odd)

print("Even array")
even = [2, 4, 6, 8, 10, 8]
print("even", even)
even.reverse()
print(even)

print(even.count(8))
even.sort()
print(even)