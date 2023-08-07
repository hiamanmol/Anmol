# For EACH OR ENHANCED FOR LOOP

data = list(range(10,101,10))
print("Data :",data)

# for idx in range(len(data)):
#     print(data[idx])

data = set(data)
# elements can be named of any choice
for elements in data:
    print(elements)

student={
    "name":"anmol",
    "roll no":21,
}
print("dictionary data...")

items=student.items()
for item in items:
    # print (itmes)
    print(item[0], item[1])

print("Dictionary keys :")
keys = student.keys()
for key in keys:
    print(key)
print("Dictionary key and values")
for key in
