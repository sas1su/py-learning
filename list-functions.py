# all return true if all true and true for empty list
l = [1, 2, 3, 4]
print(all(l))
print("any ", any(l))
# With 0, false
l = [1, 2 , 0]
print(all(l))
print("any ", any(l))
#with empty string, false
l = [1, 2, '']
print(all(l))
print("any", any(l))
# empty list
l = []
print(all(l), any(l))

l = [2, 4, 3, 1]
print("length:", len(l))
print("Max:", max(l))
print("min:", min(l))

print("sorted:", sorted(l))
print("sume:", sum(l))

s = ['sum', 'umesh', 'me']
print("Stringsum:", max(s))

