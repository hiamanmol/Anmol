# LIST

numbers = list(range(10, 101, 10))
print("1 numbers", numbers)
print(type(numbers))

numbers.append(30)
numbers.append(30)
numbers.append(40)
numbers.append(60)

print("2 numbers", numbers)
print("Sum:", sum(numbers))
print("MIN:", min(numbers))
print("Max:", max(numbers))
print("length:", len(numbers))

reverse_number = list(reversed(numbers))
print("reverse numbers:", reverse_number)

print("Index of 50", numbers.index(50))
print("Count of 30 is:", numbers.count(30))

data = [20, 40, 30, 10]
print("data is", data)
data.sort()
print("Data sorted:", data.sort())

names = ["anmol", "abhi", "tanvi", "yashi"]
names.sort()
print("names is:", names)
print("Min is:", min(names))
print("Max is:", max(names))
names.remove("tanvi")
data.remove(30)

#del names[2]

print(names)
print(data)

data = [10, 20, 30, 40]
# data.pop()
# data.pop(0)
# data.clear()

data.insert(2,77)
data.insert(len(data),99)
data.insert(-5,99)
print(data)