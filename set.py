# Set
john_followers = {"anmol", "abhi", "tanvi"}
print(john_followers, type(john_followers))

numbers = list(range(10, 101, 10))
print(numbers, type(numbers))

numbers = set(numbers)
print("numbers now:", numbers)
print("numbes type:", type(numbers))

numbers.add(10)
numbers.add(100)
numbers.add(200)
numbers.add(20)

print("numbers after add:", numbers)
numbers.pop()
numbers.pop()
print("numbers after pop:", numbers)

numbers.remove(50)
numbers.discard(40)
numbers.discard(30)
print("numbers after remove:", numbers)

john_followers = {"anmol","abhi","tan","jim"}
jake_followers = {"anmol","abhi","fam","pet"}

print(john_followers)
print(jake_followers)

followers=john_followers.intersection(jake_followers)
print("followers",followers)

print("issubset",john_followers.issubset(jake_followers))
print("issuperset",john_followers.issuperset(jake_followers))

A = {1, 2, 3, 4, 5, 6}
B = {7, 8, 9, 10}
C = A-B
print("C is:", C)
D = A & B
print("D is",D)
E=A^B
print("E is:",E)
F=A|B
print("F is:",F)
G=A.symmetric_difference(B)
print("G is:",G)
A.clear()
