# pow2 using list comprehension
pow2 = [2 ** x for x in range(10)]
print(pow2)

print("Comprehension with if statement")
pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)

print("Comprehension with more for")
stmt = [x+y for x in ["python ", "c "] for y in ["progm", "lang"]]
print(stmt)

print("List membershipt test")
fruits = ['apple', 'banana', 'orange']

if 'orange' in fruits:
    print('I bought orange')

if 'pinapple' not in fruits:
    print("I did not buy Pinapple")

print("Iterating List")
for fruit in fruits:
    print("I love ", fruit)