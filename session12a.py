names = "john,anmol,jim,abhi"

# INDEXING
print(len(names))
print(names[2])
print(names[-4])

# SLICING
print(names[1:5])

# MULTIPLICITY
new_names = names*2
print(new_names)

# CONCATINATON
print(names, id(names))
names = names + ",kia"
print(names, id(names))

print(names)

# MEMBERSHIP TESTING
print("kia" in names)
